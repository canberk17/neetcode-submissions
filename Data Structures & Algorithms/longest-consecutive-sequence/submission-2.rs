impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
      let mut hashset = HashSet::new();
      let mut longest = 0;


      for num in nums{
        hashset.insert(num);

      }
      
      for num_ref in &hashset{
        let num = *num_ref;
        let mut i = 0;
        
        if hashset.contains(&(num - 1)){
            continue
        }
        while hashset.contains(&(num + i)){
                i += 1;
            
        }

        longest = std::cmp::max(longest,i);
      }


    longest



    }
}
