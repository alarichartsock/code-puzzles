use std::fs::File;
use std::io::{self, Read};

fn main() -> io::Result<()> {
    // Read the input from a file
    let mut file = File::open("in.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    // Calculate the final floor
    let final_floor = calculate_floor(&contents);

    // Print the result
    println!("The final floor is: {}", final_floor);

    Ok(())
}

fn calculate_floor(instructions: &str) -> i32 {
    let mut floor = 0;
    let mut pos = 0;
    let mut found_basement = false;

    for c in instructions.chars() {
        pos += 1;
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => (), // Ignore any other characters
        }
        // Part 2
        if (floor == -1) && (found_basement == false){
            
            print!("Santa is in the floor at position {} \n", pos);
            found_basement = true;
        }
    }

    // Part 1
    floor
}