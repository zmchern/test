import curses
from random import randrange,choice
from collections import defaultdict

actions = ['Up','Left','Down','Right','Restart''Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = dict(zip(letter_codes,action*2))