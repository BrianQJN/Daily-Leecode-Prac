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