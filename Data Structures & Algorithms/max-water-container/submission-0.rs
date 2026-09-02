impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {

        let mut left = 0;
        let mut right = heights.len() - 1;

        let mut most_water = 0;


        while left < right{
            let mut width = right - left;
            let mut curr_height = std::cmp::min(heights[left],heights[right]);

            let total = curr_height * width  as i32;

            most_water = std::cmp::max(total,most_water);


            if heights[left] < heights[right]{
                left += 1;
            }else{
                right -= 1;
            };

            


        };

        most_water

    }
}
