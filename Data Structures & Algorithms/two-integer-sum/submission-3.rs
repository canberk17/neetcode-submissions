use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut has = HashMap::new();

        for i in 0..nums.len() {
            let diff = target - nums[i];
            
            if has.contains_key(&diff){
                // FIX: Put the stored past index FIRST, and the current index SECOND
                return vec![*has.get(&diff).unwrap(), i as i32];
            }

            has.insert(nums[i], i as i32); 
        }
         
        vec![]
    }
}
