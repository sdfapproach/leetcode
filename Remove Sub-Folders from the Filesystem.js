// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2025-07-19
// Remove Sub-Folders from the Filesystem

/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    
    const folderSet = new Set();
    folder.sort((a, b) => a.length - b.length);

    for (let di of folder) {
        let text = "/";
        let skip = false;

        for (let i = 1; i < di.length; i++) {
            if (di[i] !== "/") {
                text += di[i];
            } else {
                if (folderSet.has(text)) {
                    skip = true;
                    break;
                } else {
                    text += "/";
                }
            }
        }

        if (!skip) {
            folderSet.add(di);
        }
    }

    return Array.from(folderSet);

};