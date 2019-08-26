# Write a function that takes a list of words as input, and returns
# a list of those words bucketized by anagrams.
#
# "Anagram" definition: a word, phrase, or name formed by rearranging
# the letters of another, such as cinema, formed from iceman.
#
# Example:
#
# anagram_buckets(word_list)
#
# Input:  ["star", "rats", "car", "arc", "arts", "stars"]
# Output:  [ ["star", "rats", "arts"], ["car", "arc"], ["stars"] ]


test_input = ["star", "rats", "car", "arc", "arts", "stars"]



def anagram_buckets(word_list):
    buckets = {}  # keys are the alphabetical reordered word, val is a
    for word in word_list:
        word_hash = "".join(sorted(word))
        if word_hash in buckets:
            bucket = buckets[word_hash]
            bucket.append(word)
            buckets[word_hash] = bucket
        else:
            buckets[word_hash] = [word]

    return buckets.values()

print(anagram_buckets(test_input))

anagram_buckets()




#
#
# import collections
#
# test_input = ["star", "rats", "car", "arc", "arts", "stars"]
#
#
# def get_alfa_key(word):
#     """return a reordered string in alfabetical order."""
#     return ''.join(sorted(list(word)))
#
#
# def anagrams(words):
#     """Find anagrams."""
#     word_map = collections.defaultdict(list)
#
#     for word in words:
#         word_hash = get_alfa_key(word)
#         word_map[word_hash].append(word)
#     return word_map.values()
#
#
# print(anagrams(test_input))
