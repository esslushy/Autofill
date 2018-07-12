#import
import codecs

#classes
class TrieNode:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.children = []
#functions
def add(root, word):
    inChild = False#not found to be in child node yet
    node = root#so it can change every time when new children are added and it goes down one node
    for char in word:#a node contains one letter therefore it needs to iterate through each letter
        for child in node.children:#check each child to see if it contains the value
            if child.value == char:#if they match
                child.count+=1#increase count by one
                node = child#advance down the node root as the character advance through the word
                inChild = True#was in child so skips if statement
                break#once found no need to continue
        if(not inChild):#if it is not in child outside the child in children loop because it runs 0 times with no children
            new_node = TrieNode(char)#make new node with the value
            node.children.append(new_node)#add it to children
            node = new_node#go down the node root as characters advance

def checkInTrie(UInput, trie):
    node = trie
    existsInChild = False
    for char in UInput:
        for child in node.children:
            if char == child.value:
                node = child#move down the line to continue moving down the word
                existsInChild=True
                break#no longer need to continue this loop
            else:
                existsInChild = False
        if(not existsInChild):
            return False
    return True#if every word exists in child then return true

def advanceToEndOfWord(UInput, trie):
    node = trie
    for char in UInput:
        for child in node.children:
            if char == child.value:
                node = child
                break
    return node

def returnCompletions(UInput, trie):
    node = advanceToEndOfWord(UInput,trie)#move down trie until end of word fragment
    possibleNumberOfAutofills=len(node.children)#how many possible autofills
    #sort children from highest inputs into them highest to lowest
    #return up to top 5 possible autofill endings to it
    #end function by returning the array of autofills

#variables
historyArray = codecs.open("my_history.txt").read().lower().split("\n")#split the words into an array
trie = TrieNode("*")#root node

#start programming
for word in historyArray:#setting up nodes
    add(trie, word)#add new nodes taking root and word. Because of how arrays work no need to return it as it indexes to the same array)
notFullInput = input("What would you like to autofill? Put in a word fraction and see if it autofills.\n")
if(checkInTrie(notFullInput, trie)):
    autofillResults = returnCompletions(notFullInput,trie)
    for result in autofillResults:
        print(result)
else:
    print("No results were found.")
