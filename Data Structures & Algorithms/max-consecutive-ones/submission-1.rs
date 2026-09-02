impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {

        let mut curr = 0;
        let mut max_ones = 0 ;

        for i in 0..nums.len(){
            if nums[i] == 1 {
                curr += 1;
                max_ones = max_ones.max(curr)
            } else{
                curr = 0;
            }
        }

        max_ones

    }
}
