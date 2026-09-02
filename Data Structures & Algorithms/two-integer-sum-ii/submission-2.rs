impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0;
        let mut right = numbers.len() - 1;


        while left < right {
            let current_sum = numbers[right]+numbers[left];

            if current_sum == target{
                return vec![left as i32 + 1,right as i32 + 1]

            } else if current_sum > target {
                right -= 1;

            } else  {
                left += 1;
        };
    };
    vec![]
}
}
