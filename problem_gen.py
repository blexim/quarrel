#!/usr/bin/python

import sys
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

wordlist = open(sys.argv[1])
max_letters = int(sys.argv[2])
num_questions = int(sys.argv[3])

ws = []

for w in wordlist.xreadlines():
  w = w.strip()

  if len(w) == max_letters:
    ws.append(w)

wordlist.close()

for i in xrange(num_questions):
  s = list(random.choice(ws))
  random.shuffle(s)
  s = ''.join(s)
  n = random.randint(2, max_letters)
  print "%s %d" % (s, n)
