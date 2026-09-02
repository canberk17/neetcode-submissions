impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let chars_s: Vec<char> = s.chars().collect();
        let chars_t: Vec<char> = t.chars().collect();

        let mut counter_s = HashMap::new();
        let mut counter_t = HashMap::new();

        for i in 0..chars_s.len(){

            *counter_s.entry(chars_s[i]).or_insert(0) += 1;

        }


        for j in 0..chars_t.len(){

            *counter_t.entry(chars_t[j]).or_insert(0) += 1;

        }

    
        return counter_t==counter_s
    }
}
