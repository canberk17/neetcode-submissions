impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {

        let mut rows: HashMap<usize, HashSet<char>> =  HashMap::new();

        let mut cols: HashMap<usize,HashSet<char>> = HashMap::new();

        let mut boxes: HashMap<(usize, usize), HashSet<char>> = HashMap::new();


        for row in 0..9 {
            for col in 0..9 {
                let cell_value = board[row][col];

                if cell_value == '.'{
                    continue
                }

                let box_id = (row/3,col/3);

                let is_row_duplicate = !rows.entry(row).or_default().insert(cell_value);
                let is_col_duplicate = !cols.entry(col).or_default().insert(cell_value);
                let is_box_duplicate = !boxes.entry(box_id).or_default().insert(cell_value);

                if is_row_duplicate || is_col_duplicate || is_box_duplicate {
                     return false
                }
            }
            }
            return true
            }
            
        }
        
