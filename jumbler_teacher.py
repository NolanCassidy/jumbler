"""
Solve a jumble (anagram) by checking against each word in a dictionary
Authors: jsventek

Usage: python3 jumbler.py jumbleword wordlist.txt
"""

import argparse

def jumbler(jumble, dict_file_name):
    """
    Print elements of dict_file_name that can be rearranged into the jumble.
    Args:
       jumble:  The anagram as a string
       dict_file_name:  the name of a file containing words, 1 per line
    Returns:  nothing
    Effects:  prints each matching word on an individual line,
              then a count of matching words (or "No matches" if zero)
    """

    # first you must open the file
    wordfile = open(dict_file_name, 'r')

    # second you must read each word from the file and perform an
    # appropriate comparison of each with 'jumble'; you need to count the
    # number of lines read from the file
    sorted_jumble = sorted(jumble)
    nlines = 0
    nmatches = 0
    for line in wordfile:
        word = line.strip()
        nlines += 1
        sorted_word = sorted(word)
        if sorted_word == sorted_jumble:
            print(word)
            nmatches += 1

    # if a word matches 'jumble', you are to print the word on a line by itself

    # after you have read each word from the file and compared, you need to
    # close the file
    wordfile.close()

    # assume that there were MATCHES words that matched, and NLINES in the file
    # if there was a single match, you need to print
    # "1 match in NLINES words", where NLINES is replaced by the value of NLINES
    # if there were two or more matches, you need to print
    # "MATCHES matches in NLINES words"
    # if there were no matches, you need to print
    # "No matches"
    if nmatches == 0:
        print("No matches")
    elif nmatches == 1:
        print('1 match in {} words'.format(nlines))
    else:
        print('{} matches in {} words'.format(nmatches, nlines))

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

    

    

