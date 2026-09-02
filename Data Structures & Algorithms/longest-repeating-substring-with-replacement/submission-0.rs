impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut seen = HashMap::new();
        
        let mut max_freq = 0;
        let mut longest = 0;
        let mut left = 0;

        

        // We borrow the vector (&chars) and copy the char (&c)
        for right in 0..chars.len() {
            let c = chars[right];

            *seen.entry(c).or_insert(0) += 1;

            max_freq = max_freq.max(*seen.get(&c).unwrap_or(&0));


            let current_window = (right - left + 1) as i32;

            if current_window - max_freq > k{
                let left_char = chars[left];
                if let Some(count) = seen.get_mut(&left_char) {
                    *count -= 1;
                    if *count == 0 {
                        seen.remove(&left_char);
                    }

                };
                left += 1;

            };
            longest = longest.max((right-left + 1) as i32);
            
        }
        longest

    }
}

