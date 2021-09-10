"""Generate Markov text from text files."""

from random import choice
import string



def open_and_read_file(file_path):

    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    words = contents.split()
    # print(words)
    return words




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string
    # your code goes here

    for i in range(len(words) - 2):
            try:
                key = words[i], words[i+1]
                if key in chains:
                        chains[key].append(words[i+2])
                else:
                    chains[key] = [words[i+2]]

            except IndexError:
                print("Index Error, reached the end of the iterator.")
                pass

    # print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.
    try:
        while word is not None:
            key = (key[1], word)
            words.append(word)
            word = choice(chains[key])
    except KeyError:
        print("Key error!!")




    # for key in chains:
    #     chains[key[1], choice(chains.get(key))]
    #     print(chains)



    # words = []

    # # your code goes here

    return ' '.join(words)


input_path = 'moby_dick.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)



new_name = []

i = 0

while i < 20:
    new_name.append(choice(string.ascii_lowercase))
    i += 1

new_name.append(".txt")

with open("".join(new_name), "x") as f:
    f.write(random_text)
print(random_text)
print("".join(new_name))
