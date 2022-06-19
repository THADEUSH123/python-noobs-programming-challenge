import sys
from word_score import score_word
f=open("sowpods.txt")
contents = f.read()
scrabble_words = contents.split("\n")
print(len(scrabble_words))
f.close()

import time
s=time.time()
val = 0
for i in range(8031810176):
    val += 1
print(val)
e=time.time()
print(e-s)
print('yoooooolooooo')


letters = "crate"
# get letters from command line
#letters = sys.argv[1]

def make_words(letters,count):
    if count == 1:
        return list(letters)
    else:
        sub_words = make_words(letters,count - 1)
        new_words=[]
        for letter in letters:
            for word in sub_words:
                new_words.append(letter + word)
        #print("17 new words", new_words)
        return new_words


def check_words(letters):
    letters = letters.upper()
    good_words = []
    for word_length in range(1, len(letters)+1):
        print('LEN =', word_length)
        words = make_words(letters,word_length)
        #print("24: ", words)

        for word in words:
            if word in scrabble_words:
                good_words.append(word)
    return good_words
all_words = check_words(letters)
scored_words = []
for word in all_words:
    score = score_word(word)
    scored_words.append( (score, word))
sorted_words = sorted(scored_words, reverse=True)
for tup in sorted_words:
    print(tup)
