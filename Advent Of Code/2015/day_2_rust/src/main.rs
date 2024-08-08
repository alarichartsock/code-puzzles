use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("in.txt")?;
    
    // Create a buffered reader
    let reader = BufReader::new(file);

    let mut res_paper = 0;
    let mut res_ribbon = 0; 

    // Read the file line by line
    for line in reader.lines() {
        match line {
            Ok(line_content) => { 
                let paper = handle_wrapping_paper(&line_content);
                res_paper += paper; 

                let ribbon = handle_ribbon(&line_content);
                res_ribbon += ribbon;
            }  
            Err(e) => {
                eprintln!("Error reading line: {}", e);
            }
        }
    }

    
    print!("Part 1: {} ", res_paper);
    print!("Part 2: {} ", res_ribbon);

    Ok(())
}

fn parse_line(i:&str) -> Vec<i32> {
    let parts: Vec<i32> = i.split("x")
        .map(|s| s.parse::<i32>())
        .filter_map(Result::ok)    
        .collect();

    return parts
}

fn handle_ribbon(i:&str) -> i32 {
    let mut parts = parse_line(i);

    parts.sort();
    
    let cube = parts[0] * parts[1] * parts[2];
    let shortest = 2 * parts[0] + 2 * parts[1];

    return cube + shortest   
}

fn handle_wrapping_paper(i:&str) -> i32  {
    let parts = parse_line(i);

    let l = parts[0];
    let w = parts[1];
    let h = parts[2];

    let side1 = 2 * l * w;
    let side2 = 2 * w * h;
    let side3 = 2 * h * l;

    return side1 + side2 + side3 + std::cmp::min(l*w,std::cmp::min(h * l,w * h))

}