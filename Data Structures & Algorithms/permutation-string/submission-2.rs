use itertools::sorted;
impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {

        let  size = s1.len()  ;


        let mut left = 0;
        let s1_sorted : Vec<char> =sorted(s1.chars()).collect();
        

        while left + size <= s2.len() {
            let right = left + size;

            let permut_str: Vec<char> =sorted(s2[left..right].chars()).collect();
            

            if permut_str == s1_sorted{ 
                return true
            } 
            
            left +=1 ;
        
        };
        false


    }
}
