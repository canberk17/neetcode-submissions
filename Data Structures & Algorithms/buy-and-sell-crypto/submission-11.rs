impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        
        let mut size = prices.len() ;
        let mut left = 0;
        let mut right = left + 1;
        let mut max_prof = 0;


        while right < size {

            if prices[left] < prices[right]{
                let profit = prices[right] - prices[left];
                max_prof = max_prof.max(profit);
                right += 1;
            } else{

                left = right;
                right += 1;

            }
            
        }
        max_prof

    }
}
