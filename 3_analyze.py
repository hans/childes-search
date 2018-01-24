from argparse import ArgumentParser

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main(args):
  sns.set_style('darkgrid')

  df = pd.read_table(args.file, header=None)

  fig, axs = plt.subplots(2)
  fig.suptitle(args.file)

  adj_type_order = df[2].value_counts().index

  # Plot adjective type histogram.
  sns.countplot(x=2, order=adj_type_order, data=df, ax=axs[0])

  # Calculate type/token frequencies.
  token_frequencies = df[2].value_counts()
  type_frequencies = df.groupby(2).agg({0: 'nunique'}).reindex(token_frequencies.index)
  type_token_ratios = type_frequencies.div(token_frequencies, axis=0).reset_index()
  sns.barplot(x="index", y=0, data=type_token_ratios, ax=axs[1])

  axs[0].set_title("token frequency")
  axs[0].set_xlabel("adj type")
  axs[1].set_ylabel("token frequency")

  axs[1].set_title("type/token ratio")
  axs[1].set_xlabel("adj type")
  axs[1].set_ylabel("type/token ratio")

  plt.tight_layout()

  if args.out:
    plt.savefig(args.out)
  else:
    plt.show()


if __name__ == '__main__':
  p = ArgumentParser()

  p.add_argument("file")
  p.add_argument("--out")

  main(p.parse_args())
