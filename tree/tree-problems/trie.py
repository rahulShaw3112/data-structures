# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class Node:
    def __init__(self, ch):
        self.val = ch
        self.children = {}
        self.endsHere = False
        
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('@')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.root
        for i,ch in enumerate(word):
            if(ch not in temp.children):
                temp.children[ch] = Node(ch)
            
            temp = temp.children[ch]
            if(i == len(word)-1):
                temp.endsHere = True
                    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        for i,ch in enumerate(word):
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        if(temp.endsHere):
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for i,ch in enumerate(prefix):
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)