impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {

        let mut result = vec![1; nums.len()] ;

        for (ind ,num ) in nums.iter().enumerate(){
            for (ind2 ,num2 ) in nums.iter().enumerate(){
                if ind2!= ind {
                    result[ind] *= num2;

                }
            }
        }
        result



    }
}
