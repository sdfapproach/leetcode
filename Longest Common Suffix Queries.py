# https://leetcode.com/problems/longest-common-suffix-queries/?envType=daily-question&envId=2026-05-28
# Longest Common Suffix Queries

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        trie = {}

        def is_better(i, best):
            if best == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[best]):
                return True
            if len(wordsContainer[i]) == len(wordsContainer[best]) and i < best:
                return True
            return False

        trie["best"] = -1

        for i, word in enumerate(wordsContainer):
            node = trie

            if is_better(i, node["best"]):
                node["best"] = i

            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {"best": -1}

                node = node[ch]

                if is_better(i, node["best"]):
                    node["best"] = i

        ans = []

        for query in wordsQuery:
            node = trie

            for ch in reversed(query):
                if ch not in node:
                    break
                node = node[ch]

            ans.append(node["best"])

        return ans