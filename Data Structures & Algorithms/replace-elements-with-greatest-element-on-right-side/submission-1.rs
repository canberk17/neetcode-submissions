impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {

        let mut arr = arr;
        let mut max_from_right = -1;


        for  i in (0..arr.len()).rev(){
            let current = arr[i];

            arr[i]= max_from_right;

            if current > max_from_right{
                max_from_right = current;
            };
        };

        arr

    }
}
