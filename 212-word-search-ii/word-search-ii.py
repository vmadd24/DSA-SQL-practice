class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndofWord = False

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        r = len(board)
        c = len(board[0])

        words_trie = TrieNode()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        res = []


        def insertWords(word: str) -> None:

            curr = words_trie

            for x in word:
                idx = ord(x) - ord("a")
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]

            curr.isEndofWord = True
        


        def backtrack(i: int, j: int, trie_node: TrieNode, path: str):

            if trie_node.isEndofWord:
                trie_node.isEndofWord = False
                res.append(path)

            for di, dj in directions:

                new_i, new_j = i + di, j + dj

                if (not (0 <= new_i < r and 0 <= new_j < c)) or board[new_i][new_j] == "*":
                    continue
                    
                curr_node = trie_node.children[ord(board[new_i][new_j])-ord("a")]

                if curr_node:
                    temp = board[new_i][new_j]
                    board[new_i][new_j] = "*"
                    backtrack(new_i, new_j, curr_node, path + temp)
                    board[new_i][new_j] = temp
        

        for word in words:
            insertWords(word)

        
        for i in range(r):
            for j in range(c):
                trie_node = words_trie.children[ord(board[i][j]) - ord("a")]
                if trie_node:
                    temp = board[i][j]
                    board[i][j] = "*"
                    backtrack(i, j, trie_node, temp)
                    board[i][j] = temp
        
        return res