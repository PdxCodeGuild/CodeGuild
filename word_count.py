# # Lab: Word Count
#
# ###### Delivery Method: Prompt Only
#

# Write a python module to analyze a given text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.
#
# ------------------------
#
# #### Instructions
#
# Find a book on [Project Gutenberg](http://www.gutenberg.org).
# Download it as a UTF-8 text file.
#
# 1. Open the file and deal with any decoding error that arise.

# with open("peter_pan.txt", "r", encoding="utf-8") as neverland:
#     lines = neverland.read().split()
#
# for word in lines:
#     print(word)

file = open("../text/peter_pan.txt", "r", encoding="utf-8")  #Opens the text file
word_list = file.read().lower().replace('.', '').replace(',', '').replace('?', '').split()  #Replaces characters and puts everything into lower case
wordcount={}
for word in word_list:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# for value in wordcount:
# 	if int(value) < 5:
# 		del wordcount[key] 

print(wordcount)
# print (word,wordcount)
# file.close();

# 1.  Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.
#
# 1.  Count how often each unique word is used, then print the most frequent top 10 out with their counts.
#
# 1. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
#
#
#
# --------------------------------------------------------
#
# #### Advanced
#
# 1. Make a command line tool with the `sys.argv`.  Allow the the user to pass in the filename to a `.txt` file when execiting your program.  Use the `sys.argv` to parse the filename to use for the analysis.
#
#
# ---------------------------------------------------------
#
# #### Super Advanced
#
# 1. Allow the user to enter a word and get the most likely words to follow the given word.  Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.
#     ```
#     Enter Query Word > Mr.
#     The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
#     ```
#
# 1. Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.
#
# 1. Chain together that ability to generate random sentences, one word at a time, from a given starting word.
# This is a language model.