class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for word in words:
            for char in word:
                graph[char]
        

        for i in range(len(words) -1):
            first = words[i]
            second = words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return ""
            
            for  j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    graph[first[j]].append(second[j])
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