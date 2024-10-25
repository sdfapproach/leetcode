# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2024-10-25
# Remove Sub-Folders from the Filesystem

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder_set = set()

        folder.sort(key = lambda x : len(x))

        for di in folder:

            text = "/"

            for i in range(1, len(di)):

                if di[i] != "/":
                    text += di[i]
                else:
                    if text in folder_set:
                        break
                    else:
                        text += "/"
                    
            folder_set.add(text)
        
        return list(folder_set)