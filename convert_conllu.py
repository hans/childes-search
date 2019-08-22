"""
Output CoNLL-U parse file from CHILDES corpus.
"""

from argparse import ArgumentParser
from pathlib import Path
import sys

import nltk
from nltk.corpus.reader import CHILDESCorpusReader


def print_conllu(sentence, out):
  if not sentence or sentence[0][0] == "xxx":
    # ???
    return

  # The dependency relation format uses its own indices. First resolve these
  # indices to be the same as basic sentence indices.
  real_indices = {0: 0}
  for i, (word, _, relation) in enumerate(sentence):
    given_index = int(relation.split('|')[0])
    real_indices[given_index] = i + 1

  out = []
  root_node = None
  for i, (word, tag, relation) in enumerate(sentence):
    _, given_head, head_reln = relation.split('|')

    out.append(("%s\t" * 10).strip() %
        (i + 1, word, "_", tag, "_", "_", real_indices[int(given_head)],
         head_reln, "_", "_"))

  print("\n".join(out))
  print()


def main(args):
  corpus = CHILDESCorpusReader(str(args.path.parent), str(args.path.name))
  # fit their strange api :)
  speaker = "ALL" if args.speakers == ["ALL"] else args.speakers

  for fileid in corpus.fileids():
    for sentence in corpus.words(fileid, relation=True, speaker=speaker):
      try:
        print_conllu(sentence, sys.stdout)
      except:
        # Some of the sentences bork because the parses aren't complete. Oh well.
        pass


if __name__ == '__main__':
  p = ArgumentParser()

  p.add_argument("path", type=Path)
  p.add_argument("--speakers", default="ALL", type=lambda speakers: speakers.split(","))

  main(p.parse_args())
