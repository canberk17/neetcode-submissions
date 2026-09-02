impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {

        let mut maxheap = BinaryHeap::new();

        let mut hashmap = HashMap::new();


        for i in 0..nums.len(){
            *hashmap.entry(nums[i]).or_insert(0) += 1;
        }
        
        for (key,val) in hashmap {
            maxheap.push((val,key));
        }

        let mut result = vec![];
        for _ in 0..k{
            if let Some((val,key)) = maxheap.pop(){
            result.push(key)
        }
        }

        result

            
        






    }
}
