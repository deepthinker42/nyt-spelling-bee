#!/usr/bin/env python3

import os
import sys
import argparse

WORDS = "/usr/share/dict/linux.words"


class Words(object):

    def __init__(self, required_letter, other_letters):
        self.required_letter = required_letter
        self.other_letters = other_letters
        self.all_letters = f'{self.required_letter}{self.other_letters}'
        return

    def get_words(self):
        words = {}
        with open(WORDS) as f:
            for line in f.readlines():
                line = line.strip()
                if (not line) or (not len(line) > 3) or (not self.required_letter in line) or (not all([x in self.all_letters for x in line])):
                    continue
                words.setdefault(len(line), []).append(line)
        return words

    def main(self):
        words = self.get_words()
        for word_length in sorted(words, reverse=True):
            print(f'{word_length}-letter words')
            for word in words[word_length]:
                print(f'    {word}')
        return 


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Find words that satify the NY Times Spelling Bee puzzle')
    parser.add_argument('-r', '--required-letter', help='Required letter that words must have', required=True)
    parser.add_argument('-o', '--other-letters', help='The rest of the letters that the words can have', required=True)
    args = parser.parse_args()
    w = Words(args.required_letter, args.other_letters)
    w.main()

