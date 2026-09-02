impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {

        let mut has_num = HashSet::new();

        for i in 0..nums.len(){
            if has_num.contains(&nums[i]){
                return true
            }
            has_num.insert(nums[i]);
        }
        
        return false
    }
}