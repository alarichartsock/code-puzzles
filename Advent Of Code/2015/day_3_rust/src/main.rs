use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::collections::HashSet;

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("in.txt")?;
    
    // Create a buffered reader
    let reader = BufReader::new(file);

    let mut whole_path = String::from("");
    let mut santa_path = String::from("");
    let mut robo_path = String::from("");

    // Read the file line by line
    for line in reader.lines() {
        match line {
            Ok(line_content) => { 
                for (i,c) in line_content.chars().enumerate() {
                    whole_path.push(c);

                    if i % 2 == 0 {
                        robo_path.push(c)
                    } else {
                        santa_path.push(c)
                    }
                }
            }  
            Err(e) => {
                eprintln!("Error reading line: {}", e);
            }
        }
    }

    let part1_solution:usize = travel(whole_path).len();

    println!("Answer to part 1: {}", part1_solution );

    let mut robo_sol: HashSet<(i32,i32)> = travel(robo_path); 
    let sant_sol: HashSet<(i32,i32)> = travel(santa_path);

    robo_sol.extend(sant_sol);    

    let part2_solution:usize = robo_sol.len();

    println!("Answer to part 2: {}", part2_solution);

    Ok(())
}

fn travel(path:String) -> HashSet<(i32,i32)> {
    let mut unique_locations: HashSet<(i32,i32)> = HashSet::new();

    unique_locations.insert((0,0));

    let mut x:i32 = 0;
    let mut y:i32 = 0;

    for c in path.chars() {
        if c == '^' {
            y += 1
        } else if c == 'v' {
            y -= 1
        } else if c == '>' {
            x += 1
        } else if c == '<' {
            x -= 1
        } 
        unique_locations.insert((x,y));
    }

    return unique_locations
}