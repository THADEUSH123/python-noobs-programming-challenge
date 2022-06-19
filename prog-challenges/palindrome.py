def is_palindrome(word):
    return word == word[::-1]


words = ['hello', 'draw', 'ana', 'anna', 'jim', '23', '22']


def test_words(words):
    for word in words:
        if is_palindrome(word):
            print('{} is a palindrome.'.format(word))
        else:
            print('{} is not a palindrome.'.format(word))


def longest(word1, word2):
    """Return the word that is longer or the first word if the same."""
    if len(word1) >= len(word2):
        return word1
    else:
        return word2


def longest_palindrone(sentance):
    """Find the longest palindrome in a given string."""
    words = sentance.replace('.', '').split()
    words.sort(key=len, reverse=True)
    print(words)
    for word in words:
        if is_palindrome(word):
            return word
    return None


sentance = 'th ehdks dad rar waw ada racecars. go osgo bob'

print(longest_palindrone(sentance))
