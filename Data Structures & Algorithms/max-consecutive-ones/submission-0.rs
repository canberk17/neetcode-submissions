impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {

        let mut res = usize::MIN;
        let mut cnt = 0;

        for i in 0..nums.len(){
            if nums[i] == 0 {
                
                cnt = 0;
            } else{
                cnt += 1;

            }
            res = res.max(cnt);
            

        }

        res as i32


    }
}
