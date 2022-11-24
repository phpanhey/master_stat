import argparse
import pandas as pd


def main():
    args = parse_args()
    df = import_csv_as_dataframe(args["csv_filename"])
    print(df.loc[[0, 1, 2]])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_filename", default="data.csv")
    return vars(parser.parse_args())


def import_csv_as_dataframe(filename):
    df = pd.read_csv(filename, encoding="utf-16", sep="\t")
    return df


if __name__ == "__main__":
    main()
