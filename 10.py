def binary_search(dictionary, word): 
    left=0 
    right=len(dictionary)-1 
    while left <= right: 
        mid = (left + right) // 2 
        entry_word, definition = dictionary[mid] 
        if entry_word == word: 
            return f"Definition of '{word}': {definition}" 
        elif entry_word < word: 
            left = mid + 1 
        else: 
            right = mid - 1 
    return f"'{word}' not found in the dictionary." 
 
dictionary = [ 
    ("apple", "A fruit that is red or green."), 
    ("banana", "A long, yellow fruit."), 
    ("cat", "A small domesticated carnivorous mammal."), 
    ("dog", "A domesticated carnivorous mammal."), 
    ("elephant", "A large herbivorous mammal.") 
] 
 
word_to_find = "dog" 
print(binary_search(dictionary, word_to_find))