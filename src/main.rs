use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut numbers: Vec<i32> = Vec::new();

    for s in contents.lines() {
        numbers.push(s.parse::<i32>().unwrap());
    }

    let numbers_len = numbers.len();

    let mut final_number_2: i32 = 0;
    let mut final_number_3: i32 = 0;

    for number in &numbers {

        for x in 1..numbers_len {
            let next_number: i32 = numbers[x];

            if number + next_number == 2020 {
                final_number_2 = number * next_number
            }

            for y in 2..numbers_len {
                if(number + numbers[x] + numbers[y] == 2020) {
                    final_number_3 = number + numbers[x] + numbers[y];
                }

            }
        }

    }

    println!("2 numbers to 2020 final number: {}", final_number_2)
    println!("3 numbers to 2020 final number: {}", final_number_3)



}