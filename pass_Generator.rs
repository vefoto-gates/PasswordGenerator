// This program is contributed by Gaurav Mandal

use rand::Rng;
use std::iter;

fn generate_password(length: usize, use_lowercase: bool, use_uppercase: bool, use_digits: bool, use_special_chars: bool) -> String {
    let mut characters = String::new();

    if use_lowercase {
        characters += "abcdefghijklmnopqrstuvwxyz";
    }
    if use_uppercase {
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }
    if use_digits {
        characters += "0123456789";
    }
    if use_special_chars {
        characters += "!@#$%^&*()_-+=<>?";
    }

    if !(use_lowercase || use_uppercase || use_digits || use_special_chars) {
        panic!("At least one character set (lowercase, uppercase, digits, special chars) must be selected.");
    }

    let password: String = iter::repeat_with(|| {
        let random_index = rand::thread_rng().gen_range(0..characters.len());
        characters.chars().nth(random_index).unwrap()
    })
    .take(length)
    .collect();

    password
}

fn main() {
    let password = generate_password(16, true, true, true, true);
    println!("{}", password);
}

// This code is contributed by Gaurav Mandall (https://www.linkedin.com/in/gauravmandall/)