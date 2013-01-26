#!/usr/bin/python

import sys
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

max_letters = int(sys.argv[1])
num_questions = int(sys.argv[2])

for i in xrange(num_questions):
  s = ''.join(random.choice(chars) for j in xrange(max_letters))
  n = random.randint(1, max_letters)
  print "%s %d" % (s, n)
