import sys

from collections import Counter

def counterSubset(list_1, list_2):
    c1, c2 = Counter(list_1), Counter(list_2)
    for k, n in c1.items():
        if n > c2[k]:
            return False
    return True


def score_word(word):
    letter_val_map = {'a': 1,
                      'b': 2,
                      'c': 3,
                      'l': 5,
                      'p': 15,
                      'h': 4,
                      '*': 0,
                      '?': 0}
                      # Add all letter values here
    score = 0
    for l in list(word):
        if l in letter_val_map:
            score += letter_val_map[l]
    return score

def is_match(tile, word):
    tile_letter_list = list(tile)
    word_letter_list = list(word)
    # Basic case check
    if counterSubset(tile_letter_list, word_letter_list):
        return True

    # Advanced case check for wild cards

    # for pos in range(len(word_letter_list)):
    #     temp_word_letter_list = word_letter_list
    #     print(str(pos) + ' of ' + str(len(word_letter_list)))
    #     print(word_letter_list)
    #
    #     del temp_word_letter_list[pos]
    #     if counterSubset(tile_letter_list, temp_word_letter_list):
    #         print("Wildcard used")
    #         word_letter_list[pos] = '?'
    #         print(''.join(word_letter_list))
    #         return True


    return False



def total(tile, word_list):
    matches = []
    for word in word_list:
        # if counterSubset(list(word), list(tile)):
        if is_match(word, tile):
            matches.append((word, score_word(word)))

    return sorted(matches, key=lambda tup: tup[1], reverse=True)

def main():
    file_name = "input.txt" # Update name of file with words here
    with open(file_name, "r") as f:
        valid_words = f.read().splitlines()
    print("Script imported these words: " + ", ".join(valid_words) + ".")

    tile = sys.argv[1]
    if len(tile) > 7 or len(tile) < 2:
        print("ERROR: Tile input must be greater than two and less than 7")
        quit()

    # Input validate all upercase here


    print("Comparing to the tile input: '" + tile + "'.")


    matches = total(tile, valid_words)
    if matches:
        print("The following matches exist: ")
        for match in matches:
            print(match[0] + " for " + str(match[1]) + " points.")
    else:
        print("No matches have been identified based on the tile and known valid words.")



    return total(tile, valid_words)



main()
