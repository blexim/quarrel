#!/usr/bin/python

import copy
import cmd
import cPickle

values = {
      'A' : 1,
      'B' : 5,
      'C' : 2,
      'D' : 3,
      'E' : 1,
      'F' : 5,
      'G' : 4,
      'H' : 4,
      'I' : 1,
      'J' : 15,
      'K' : 6,
      'L' : 2,
      'M' : 4,
      'N' : 1,
      'O' : 1,
      'P' : 3,
      'Q' : 15,
      'R' : 2,
      'S' : 1,
      'T' : 1,
      'U' : 3,
      'V' : 6,
      'W' : 5,
      'X' : 10,
      'Y' : 5,
      'Z' : 12
    }

def score(s):
  return sum(values[c] for c in s)


class Trie(object):
  def __init__(self):
    self.children = {}
    self.words = []
    self.score = 0

  def get(self, c):
    if c in self.children:
      return self.children[c]

    self.children[c] = Trie()
    return self.children[c]

  def insert(self, word, s=None, wordscore=0):
    if s is None:
      if ' ' in word:
        w = word[:word.index(' ')]
      else:
        w = word

      s = ''.join(sorted(w))
      wordscore = score(w)

    if s == '':
      self.words.append(word)
      self.score = wordscore
    else:
      c = s[0]
      s = s[1:]

      self.get(c).insert(word, s, wordscore)

  def search(self, word, numletters):
    word = ''.join(sorted(word))
    bestscore = self.score
    bestwords = copy.copy(self.words)
    depth = 0

    if numletters == 0:
      return (bestscore, bestwords)

    while word:
      c = word[0]
      word = word[1:]

      t = self.get(c)
      (child_score, child_words) = t.search(word, numletters-1)

      if child_score > bestscore:
        bestscore = child_score
        bestwords = child_words
      elif child_score == bestscore:
        bestwords += child_words

    return (bestscore, bestwords)

def load(words):
  f = open(words)
  t = Trie()
  n = 0

  for w in f:
    t.insert(w.strip())
    n += 1

  f.close()

  return (t, n)

class QuarrelCmd(cmd.Cmd):
  def default(self, l):
    toks = l.split()

    if l == '.':
      return True

    if len(toks) == 0:
      print "Expected: solve <word> [numletters]"
      return
    elif len(toks) == 1:
      w = toks[0]
      numletters = 9
    else:
      w = toks[0]
      numletters = int(toks[1])

    w = w.upper()

    (s, ws) = t.search(w, numletters)

    print "Score = %d:" % s

    for w in set(ws):
      print w


if __name__ == '__main__':
  import sys
  import time

  if len(sys.argv) > 1:
    dictname = sys.argv[1]
  else:
    dictname = 'bigdict.txt'

  print "Loading..."

  start = time.time()
  (t, n) = load(dictname)
  end = time.time()
  elapsed = end-start

  print "Loaded %d words in %.02fs" % (n, elapsed)

  if len(sys.argv) > 2:
    total = 0
    nwords = 0

    start = time.time()
    f = open(sys.argv[2])

    for l in f.xreadlines():
      toks = l.split()
      w = toks[0]
      n = int(toks[1])

      (score, words) = t.search(w, n)
      total += score
      nwords += 1

    f.close()
    end = time.time()
    elapsed = end-start

    print "Solved %d words in %.02fs" % (nwords, elapsed)

    print total
  else:
    qcmd = QuarrelCmd()
    qcmd.prompt = "> "
    qcmd.cmdloop()
