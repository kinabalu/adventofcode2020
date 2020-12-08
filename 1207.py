def read_input():
    with open('12_07_input.txt') as reader:
        return [line.strip() for line in reader]


def dfs(visited, graph, node):
    count = 1
    if node not in visited:
        if type(graph[node]) is dict:
            for neighbor in graph[node]:
                count += graph[node][neighbor] * dfs(visited, graph, neighbor)

            visited.add(count)

    return count


def find_contains(rules, bag_color, contained_rules = []):
    for rule in rules:
        if type(rules[rule]) is dict and bag_color in rules[rule]:
            contained_rules.append(rule)
            find_contains(rules, rule, contained_rules)
    return contained_rules


def main():
    rules = read_input()

    bag_rules = {}

    for rule in rules:
        split_rule = rule.split('contain')

        bag_color = split_rule[0][:-6]

        contain_colors = split_rule[1].split(',')

        if bag_color not in bag_rules:
            bag_rules[bag_color] = {}

        for color_option in contain_colors:
            just_color = color_option.strip()[0:color_option.find('bag')-2]

            if just_color == 'no other':
                bag_rules[bag_color] = 0
                continue
            bag_count = int(just_color[0])

            just_color = just_color[2:]

            bag_rules[bag_color][just_color] = bag_count

    contained_rules = []

    find_contains(bag_rules, 'shiny gold', contained_rules)
    unique_rules = set(contained_rules)
    print("total bags that can contain shiny gold: %d" % len(unique_rules))

    visited = set()
    print("Total bags: %d" % (dfs(visited, bag_rules, 'shiny gold') - 1))


if __name__ == '__main__':
    main()
