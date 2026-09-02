impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let mut left = 0;
        let mut right = chars.len() - 1;

        if chars.is_empty(){
            return true;
        }


        while left < right {
            if !chars[left].is_alphanumeric(){
                left += 1;
            } else if !chars[right].is_alphanumeric(){
                right -= 1;

           } else if chars[left].to_ascii_lowercase() != chars[right].to_ascii_lowercase() {
                return false
            } 
            else {
                left += 1;
                right -= 1;
            }

            
        };
        true
        

    }
}

