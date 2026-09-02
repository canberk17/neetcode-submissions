impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {

        let mut result = vec![1; nums.len()] ;

        let mut prefix = 1 ;

        for  i in 0..nums.len(){
            result[i] *= prefix;
            prefix *= nums[i]

        


        }
        let mut suffix = 1;

        for j in (0..nums.len()).rev(){
            result[j] *= suffix;
            suffix *= nums[j];

        }




        result
        // for (ind ,num ) in nums.iter().enumerate(){
        //     for (ind2 ,num2 ) in nums.iter().enumerate(){
        //         if ind2!= ind {
        //             result[ind] *= num2;
        //         }
        //     }
        // }
        // result


        





    }
}
