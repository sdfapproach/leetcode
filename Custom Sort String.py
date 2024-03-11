# https://leetcode.com/problems/custom-sort-string/?envType=daily-question&envId=2024-03-11
# Custom Sort String

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # count = collections.Counter(s)
        # new_str = ""

        # for char in order:
        #     new_str += char * count[char]
        #     del count[char]

        # for key, value in count.items():
        #     new_str += key * value

        # return new_str

        count = collections.Counter(s)
        result = []

        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]

        for char, freq in count.items():
            result.append(char * freq)

        return ''.join(result)