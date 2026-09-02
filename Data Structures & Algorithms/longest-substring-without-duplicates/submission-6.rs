use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut seen = HashSet::new();
        
        let mut curr = 0;
        let mut longest = 0;
        let mut left = 0;

        // We borrow the vector (&chars) and copy the char (&c)
        for &c in &chars {
            while seen.contains(&c) {
                let left_char = chars[left];
                seen.remove(&left_char);
                curr -= 1;
                left += 1;
            }

            seen.insert(c);
            curr += 1;
            longest = longest.max(curr);
        }

        longest
    }
}