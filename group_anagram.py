from collections import defaultdict

def grp_anagram(anag): # define function 'grp_anagram'
    anagram_dict = defaultdict(list)# create a dict, doesn't return KeyError if a key doesn't exist
    for word in anag:
        sorted_word = "".join(sorted(word))#sort the list
        anagram_dict[sorted_word].append(word)
    
    print(anagram_dict.items())

# given a list
words = ["ate", "eat", "tea", "bat", "tab", "arc", "car"] 
grp_anagram(words)    
