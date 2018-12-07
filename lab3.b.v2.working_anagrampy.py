# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:22:24 2018
@author: Javier Soon 
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Give a word file list, input the list in either a 
AVL Tree or a Red Black Tree after which search for a word and if the word 
exists in the list return the number of anagrams for that word.
exists in the list return the number of anagrams for that word.
Next find the largest number of anagrams in the file/tree.

"""
#import Node
import AVLTree
#import RBTNode
import RedBlackTree
# use a file reader
import time
count = 0
count1 = 0


# =============================================================================
# creates the tree from the file
# =============================================================================
        
def file_reader(user_input, words_file):
    
    if user_input == 'AVL':
        english_words = AVLTree.AVLTree()
        with open(words_file) as file:
            for line in file:
                english_words.insert(AVLTree.Node(str.lower(line.strip('\n'))))
            return english_words

    elif user_input == 'RBT':
        english_words = RedBlackTree.RedBlackTree()
        with open(words_file) as file:
            for line in file:
                english_words.insert((str.lower(line.strip('\n'))))
#        print_ascend(english_words.root)        # used to debug
        return english_words
    
    else:
        print ('Invalid entry')
        print('Must be either AVL or RBT')
    
        
# =============================================================================
# asks for user to input the word they want to make an anagram for        
# =============================================================================
def user(user_input, words_file):
    if user_input == 'AVL':
         user_search = input('What word do you want to find: ')
         return user_search
    
    elif user_input == 'RBT':
         user_search = input('What word do you want to find: ')
         return user_search
     
    else:
        return None
    
# =============================================================================
#     prints the anagrams for the word along with the number of anagrams
# =============================================================================
def print_anagrams(user_search_word, english_words, prefix=""):
    global count
    
    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word
#        print((str1))    # prints the word that it just did an anagram for (repeats are included)
       
        if english_words.search(str1):  # looks for str in the tree
            count += 1
            print(prefix + user_search_word)
            print_anagrams(str1, english_words, prefix) 
            
    else:
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
            
            if cur not in before:  # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)   
    return count



# =============================================================================
# another print but will be used to find the maxes
# =============================================================================
def print_anagrams2(user_search_word, english_words, count,prefix=""):
    
    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word
#        print((str1))    # prints the word that it just did an anagram for (repeats are included)
       
        if english_words.search(str1):  # looks for str in the tree
            count += 1
            print_anagrams(str1, english_words, count,prefix) 
            
    else:
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
            
            if cur not in before:  # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, count, prefix + cur)   
    return count


# =============================================================================
#   finds the max number of anagrams and the word 
# =============================================================================
def max_ana(english_words, words_file):
    max = -1    # will hold the max number of anagrams
    max_word = " "  # will hold the word of the max 
    
    with open (words_file, "r") as list:
        for i in list:
            line = i.split()
            count_a = print_anagrams2(line[0], english_words)
                        
            if max < count_a:
                max = count_a
                max_word = line[0]
            
                
    print('This is the largest anagram word is: ' + max_word)
    print(' with ' + max +' anagrams')

# =============================================================================
#   prints the tree in ascending order to make sure the tree was built correctly
# =============================================================================
def print_ascend(tree):
    global count1
    if tree is None:
        return
    print_ascend(tree.left)
    count1 = count1 + 1
    print(tree.key)
    print_ascend(tree.right)
    return count1


# =============================================================================
#    main method will do all the calls here
# =============================================================================
def main():
    
    words_file = 'words.txt'#= input ('What file do you want to use: ')
    user_input = input('What type of tree do you want to use: AVL or RBT: ')        # asks tree type
    
    starttime = time.time()
   
    english_words = file_reader(user_input, words_file) # makes the tree type be called english_words
    
    endtime = time.time()
    runtime = endtime - starttime
    print(runtime)
    
    
    user_search_word= user(user_input, words_file) # asks for the word that they want to check for

#    searchword = english_words.search(user_search_word)
#    print_ascend(english_words.root)
#    print(searchword.key)

    starttime1 = time.time()
    print_anagrams(user_search_word, english_words)
    print(count)
    endtime1 = time.time()
    runtime1 = endtime1 - starttime1
    print(runtime1)
    
    
    print('working on max length')
    
    max_ana(english_words, words_file)
        
main()