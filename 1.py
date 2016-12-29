from __future__ import print_function

V = "AEIOUY"
C = "BCDFGHJKLMNPQRSTVWXZ"

def check_if_vowels(char):
    return char.upper() in V

def is_word(word):
    for t in word:
        if t.upper() in V or t.upper() in C: return True
    print(False)
    return False

def striped_words(text):
    text = text.replace(',',' ').split(" .,")
    print (text)
    total = 0
    for word in text:
        print(word)
        if not is_word(word): continue 
        i = 0
        while len(word)>i+1:
            if check_if_vowels(word[i]) != check_if_vowels(word[i+1]):
                i+=1
                continue
            else: break
        if i==len(word)-1 and len(word)!=1: total+=1
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
