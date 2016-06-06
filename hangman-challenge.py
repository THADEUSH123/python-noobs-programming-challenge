"""Programing challenge submission.

This script plays a game of hangman. One class represents the game and one
class represents a player of the game. A human can also interact with the
game class.

"""

from random import choice
from re import match
from collections import Counter


class HangManGame(object):
    """Game of hangman.

    A representation of a game with which a Player class or human can interact.

    """

    def __init__(self, dictionary_file):
        """Initialize the vocabulary and start the game.

        Pick a random word from the vocabulary and keep it as the secret word.
        All words are capitalized.
        """
        with open(dictionary_file, 'r') as word_file:
            normalized_vocabulary = word_file.read().upper()
            self.__available_letters = set([x for x in normalized_vocabulary])
            self.vocabulary = normalized_vocabulary.split()

        self.__secret_word = choice(self.vocabulary)
        self.__revealed_word = '_' * len(self.__secret_word)
        self.__misguessed_count = 0

    @property
    def player_won(self):
        """Return if the player is a winner.

        Value is True if the player won, otherwise return False. If a game is
        is not complete(i.e. the player has not lost), return False.
        """
        if self.game_complete:
            return (self.__secret_word == self.__revealed_word)
        else:
            return None

    @property
    def game_complete(self):
        """Return if the game is finished."""
        matched = self.__secret_word == self.__revealed_word
        too_many_wrong_guesses = self.__misguessed_count >= 6
        return (matched or too_many_wrong_guesses)

    @property
    def turn_status(self):
        """Return representation of guessed letters and wrong guesses."""
        HANGMAN_DISPLAY = (
            """
            -----
            |   |
            |
            |          {letter_misguesses}
            |
            |          {status}
            |
            |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            |  -+-     {letter_misguesses}
            |
            |          {status}
            |
            |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            | /-+-     {letter_misguesses}
            |
            |          {status}
            |
            |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            | /-+-\\   {letter_misguesses}
            |
            |          {status}
            |
            |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            | /-+-\\   {letter_misguesses}
            |   |
            |   |      {status}
            |
            |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            | /-+-\\   {letter_misguesses}
            |   |
            |   |      {status}
            |  |
            |  |
            |
            -- {letters_known} ---
            {letters_available}
            """,
            """
            -----
            |   |
            |   O
            | /-+-\\   {letter_misguesses}
            |   |
            |   |      YOU LOST
            |  | |
            |  | |
            |
            -- {letters_known} ---
            {letters_available}
            """)

        print HANGMAN_DISPLAY[self.__misguessed_count].format(
            letter_misguesses='X' * self.__misguessed_count,
            status='YOU WON!!!' * (self.__secret_word == self.__revealed_word),
            letters_known=self.__revealed_word,
            letters_available=' '.join(self.__available_letters))

        return (self.__revealed_word, self.__misguessed_count,
                self.__available_letters)

    def word_contains(self, guessed_letter):
        """A letter guess against the secret word."""
        guessed_letter = guessed_letter.upper()
        if guessed_letter not in self.__available_letters:
            print('Invalid guess!')
        else:
            self.__available_letters.remove(guessed_letter)
            if guessed_letter in self.__secret_word:
                working_revealed = list(self.__revealed_word)
                for index, secret_letter in enumerate(self.__secret_word):
                    if secret_letter == guessed_letter:
                        working_revealed[index] = guessed_letter

                self.__revealed_word = ''.join(working_revealed)
                return True
            else:
                self.__misguessed_count += 1
                return False


class Player(object):
    """Class to manage AI guessing of words against a HangManGame Class.

    The basic algorythm the AI uses is: Keep a list of all possible words. Each
    turn, remove words that are not a match based on the revealed clues and
    previous guesses. Guess the letter that appears in the most words. Repeat.
    """

    def __init__(self, vocab_list):
        """Initialize knowledge of the player."""
        self.possible_words = vocab_list

    def remove_words_containing(self, letter):
        """Remove all the words that contain the specific letter."""
        self.possible_words = [w for w in self.possible_words
                               if letter not in w]

    @staticmethod
    def possibly_matching_words(words, revealed):
        """The possible secret words given what is already revealed.

        Find the subset of words that could be correct given the known
        letters from previous guesses.
        """
        regex = revealed.replace('_', '.')
        return [word for word in words if match(regex, word)]

    @staticmethod
    def most_common_letter(words, letters_available):
        """Return the letter present in the most words."""
        letters = [letter for word in words for letter in set(word)
                   if letter in letters_available]

        letter_count = Counter(letters)
        return max(letter_count, key=letter_count.get)

    def generate_guess(self, revealed_letters, letters_available):
        """Return best letter guess."""
        down_selected_words = self.possibly_matching_words(self.possible_words,
                                                           revealed_letters)

        return self.most_common_letter(down_selected_words, letters_available)


def automated_mode(vocab_path, iterations):
    """AI Player can play against the HangManGame Class."""
    games = [HangManGame(vocab_path) for _ in range(iterations)]
    wins = 0
    for game in games:
        print('\nNEW GAME\n\n\n')
        player = Player(game.vocabulary)
        while not game.game_complete:
            revealed, missed, available = game.turn_status
            letter = player.generate_guess(revealed, available)
            print('PLAYER guesses the letter: {}'.format(letter))
            if not game.word_contains(letter):
                player.remove_words_containing(letter)

        game.turn_status
        if game.player_won:
            wins += 1

    print('\n\n\n{} wins and {} losses'.format(wins, iterations - wins))


def interactive_mode(vocab_path):
    """Human can play against the HangManGame Class."""
    game = HangManGame(vocab_path)
    while not game.game_complete:
        revealed, missed, available = game.turn_status
        try:
            guess = raw_input('Guess a letter: ')
            game.word_contains(guess)
        except:
            print('Invalid Guess.')

    game.turn_status


def main():
    """Main sript body.

    Discussion: From questions.
    Evaluating word dificulty: If a bot(like the one implemented) is playing
    the game, longer secret words are easier because of the higher probability
    of guessing a correct letter early and using that information to down
    select possible secret words. Human player "word difficulty" differs
    because most humans lacks a vocabulary that is comprehensive of all
    possible secret words(i.e. a human can't guess a word that is unknown to
    them). One solution may be to build an index of word frequency. More
    frequent words have a higher liklyhood of being known by the player, and
    thus infered during the game.
    How would I mitigate word difficulty: I would segment the word frequencies
    and assign some ratio of difficult, easy, and hard questions based on the
    win loss ratio of the player. There is likely some optimal ratio that will
    keep people interested. Not too easy, but not too hard.

    To make this game more interesting, I would add word categories or running
    word phrases. For word categories, the randomly selected word would be in a
    general category visible to the player. Categories could be things like
    word origin, an industry, a specific language, a hobby, a sport, etc. I
    would implement by extending the custom vocabulary extension.

    I would also implement the win/loose history ratio to make the player feel
    challenged but not annoyed by words that are outside their vocabulary.
    """
    file_path = 'wordsEN.txt'
    while True:
        print(
            """
            1=>Automated Play
            2=>Interactive Play
            3=>Load custom vocabulary list
            4=>Exit
            """)
        choice = int(raw_input('Enter a choice[1]: ') or 1)
        if choice is 1:
            iterations = int(raw_input('How many iterations[2]? ') or 2)
            automated_mode(file_path, iterations)

        elif choice is 2:
            interactive_mode(file_path)

        elif choice is 3:
            file_path = raw_input(
                'Enter a file[{}]: '.format(file_path)) or file_path

        elif choice is 4:
            exit()

main()
