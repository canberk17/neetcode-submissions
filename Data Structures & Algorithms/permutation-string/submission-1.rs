impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut s2: Vec<char> = s2.chars().collect();
        let mut s1: Vec<char> = s1.chars().collect();
        let size = s1.len();
        
        // 1. Sort s1 on its own line
        s1.sort();

        let mut left = 0;
        
        // 2. Stop loop early enough so left + size never goes out of bounds
        while left + size <= s2.len() {
            // 3. Extract a mutable slice of the window
            let window = &mut s2[left..left+size];
            
            // 4. Create a copy of this window to sort so you don't ruin the original s2
            let mut sorted_window = window.to_vec();
            sorted_window.sort();
            
            // 5. Compare the sorted vector to s1
            if sorted_window == s1 {
                return true;
            }

            left += 1;
        };
        
        false
    }
}
