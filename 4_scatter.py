"""
Render a scatter-plot of type/token patterns across corpora.
"""

import argparse

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main(args):
  dfs = [pd.read_table(tsv) for tsv in args.tsvs]
  df = pd.concat(dfs)

  lmplot = sns.lmplot("token_frequency", "type_token_ratio", hue="corpus", data=df, fit_reg=False)
  lmplot.axes[0, 0].set_ylim(0, 1)
  lmplot.axes[0, 0].set_xscale("log")

  plt.tight_layout()
  plt.show()


if __name__ == '__main__':
  p = argparse.ArgumentParser()

  p.add_argument("tsvs", type=str, action="store", nargs="+")
  main(p.parse_args())
