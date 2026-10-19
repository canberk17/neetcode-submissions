class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for word in words:
            for char in word:
                graph[char]
        

        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1),len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for  j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        
        visited = set()
        path = set()

        result = []

        def dfs(char):

            if char in path:
                return False
            

            if char in visited:
                return True
            

            path.add(char)



            for neighbour in graph[char]:
                if not dfs(neighbour):
                    return False

            path.remove(char)
            visited.add(char)
            result.append(char)

            return True

        for char in graph:
            if not dfs(char):
                return ""
            
        return "".join(result[::-1])