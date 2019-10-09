# Given two words (beginWord and endWord), and a dictionary's word list, 
# return the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Sample:
# beginWord = "hit"
# endWord = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# beginWord = "sail"
# endWord = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None

# keywords from the problem

# words = vertex (in graph vocabulary)
# letters different = edges (one letter part of the edge)
# shortest transformation sequence = path/bfs
# begin word - starting_vertex
# end word - destination vertex
# Dictionary = list of vertexes
# no duplicates = set
# same length = edges(part)
import sys
sys.path.append('../graph')
from util import Queue

f = open('words.txt','r')
words = f.read().split('\n')
word_set = set()

for word in words:
    word_set.add(word.lower())

#find/create all nodes/edges for words with one letter different
#this function replaces entry in the adjacency list for that node
def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

def find_word_ladder(beginWord,endWord):
        qq = Queue()
        visited = set()
        qq.enqueue([beginWord])

        while qq.size() > 0:
            path = qq.dequeue()
            word = path[-1] #Vertex is word

            if word not in visited:
                if word == endWord:
                    return path
                visited.add(word)
                for new_word in get_neighbors(word):
                    new_path = list(path)
                    new_path.append(new_word)
                    qq.enqueue(new_path)


print(find_word_ladder('sail','boat'))