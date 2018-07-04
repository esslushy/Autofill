#import
import codecs

#classes
class TrieNode:
    def __init__(self, value: str):
        self.value = value
        self.count = 1
        self.children = []
#functions
def add(root, word):
    inChild = False
    node = root#so it can change every time when new children are added and it goes down one node
    for char in word:#a node contains one letter therefore it needs to iterate through each letter
        for child in node.children:#check each child to see if it contains the value
            if child.value == char:#if they match
                child.count+=1#increase count by one
                node = child#advance down the node root as the character advance through the word
                inChild = True
        if(not inChild):#if it is not in child outside the child in children loop because it runs 0 times with no children
            new_node = TrieNode(char)#make new node with the value
            node.children.append(new_node)#add it to children
            node = new_node#go down the node root as characters advance


#variables
historyArray = codecs.open("my_history.txt").read().lower().split("\n")#split the words into an array
trie = TrieNode("*")#root node

#start programming
for word in historyArray:#setting up nodes
    add(trie, word)#add new nodes taking root and word. Because of how arrays work no need to return it as it indexes to the same array
