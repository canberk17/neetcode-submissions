class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]
            
            curr.word = word
        
        rows, cols = len(board), len(board[0])
        result = []


        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()

        def dfs(r, c , node):

            if (min(r,c) < 0 or r>= rows or c>= cols or (r,c) in visited):
                return 
            
            char = board[r][c]

            if char not in node.children:
                return
            
            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None
            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                dfs(nr, nc, node)
            
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result