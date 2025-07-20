# https://leetcode.com/problems/delete-duplicate-folders-in-system/?envType=daily-question&envId=2025-07-20
# Delete Duplicate Folders in System

class TrieNode:
  def __init__(self):
    self.children: dict[str, TrieNode] = {}
    self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        ans = []
        root = TrieNode()
        subtreeToNodes: dict[str, list[TrieNode]] = collections.defaultdict(list)

        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children.setdefault(s, TrieNode())

        def buildSubtreeToRoots(node: TrieNode) -> str:
            subtree = '(' + ''.join(s + buildSubtreeToRoots(node.children[s])
                                    for s in node.children) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        def constructPath(node: TrieNode, path: list[str]) -> None:
            for s, child in node.children.items():
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])
        return ans