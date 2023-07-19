class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.end = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                char = word[i]

                if char == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]

            return cur.end

        return dfs(0, self.root)