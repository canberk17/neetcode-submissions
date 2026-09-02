impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {

        let mut left = 0;
        let mut right = height.len() - 1;

        let mut tallest_right = 0;
        let mut tallest_left = 0;

        let mut total_trapped = 0;


        while left < right {

            tallest_left = tallest_left.max(height[left]);
            tallest_right= tallest_right.max(height[right]);

            let mut water_level = min(tallest_right,tallest_left);

            if water_level  > height[left] {
                let trapped_water = water_level  - height[left] ;
                total_trapped  += trapped_water;

            } else  if water_level > height[right]{
                let trapped_water = water_level  - height[right] ;
                total_trapped  += trapped_water;


            }

            if height[left] > height[right]{
                right -= 1
            } else{
                left += 1
            }
    
        }
        total_trapped 

    }
}
