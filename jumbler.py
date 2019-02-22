"""
Solve a jumble (anagram) by checking against each word in a dictionary
Authors: Nolan Cassidy

Usage: python3 jumbler.py jumbleword wordlist.txt
"""

import argparse


def jumbler(jumble, dict_file_name):
    """
     jumbler will take a string of alpha characters and a text file containing words then
     print all words that have the same letters and how many matches

     Args: jumble: a string to check to the dictionary
           dict_file_name: a text document that is made up of strings

     Returns: nothing

     Prints: each word the characters can spell out
             how many words were matched out of how many words in the file
    """

    # first you must open the file
    my_data = open(dict_file_name, "r")

    # second you must read each word from the file and perform an
    # appropriate comparison of each with 'jumble'; you need to count the
    # number of lines read from the file
    count = 0
    matches = 0
    for line in my_data:
        count += 1
        if(sorted(line.strip()) == sorted(jumble.strip())):
            matches += 1
            print(line, end="")
    # if a word matches 'jumble', you are to print the word on a line by itself

    # after you have read each word from the file and compared, you need to
    # close the file
    my_data.close()
    # assume that there were MATCHES words that matched, and NLINES in the file
    # if there was a single match, you need to print
    # "1 match in NLINES words", where NLINES is replaced by the value of NLINES
    # if there were two or more matches, you need to print
    # "MATCHES matches in NLINES words"
    # if there were no matches, you need to print
    # "No matches"
    if count == 0:
        print("No matches")
    elif count == 1:
        print("{} match in {} words.".format(matches, count))
    else:
        print("{} matches in {} words.".format(matches, count))

def main():
    """
    collect command arguments and invoke jumbler()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls jumbler()
    """
    parser = argparse.ArgumentParser(description="Solve a jumble (anagram)")
    parser.add_argument("jumble", type=str, help="Jumbled word (anagram)")
    parser.add_argument('wordlist', type=str,
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # gets arguments from command line
    jumble = args.jumble
    wordlist = args.wordlist
    jumbler(jumble, wordlist)


if __name__ == "__main__":
    main()




