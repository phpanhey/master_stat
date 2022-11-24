import argparse
import pandas as pd


def main():
    args = parse_args()
    df = import_csv_as_dataframe(args["csv_filename"])
    age_group = {
        -1: "keine Angabe",
        1: "<16",
        2: "16-19",
        3: "20-29",
        4: "30-39",
        5: "40-49",
        6: "50-59",
        7: ">60",
    }
    
    for i in range(1, 8):
        df_tmp = df.copy()
        for x in df.index:
            if df.loc[x, "Alter"] != i:
                df_tmp = df_tmp.drop(x, inplace=False)

        print(
            f"age group {age_group[i]} : {df_tmp['Lokal vs Online: [Keine Beschreibung] 01'].mean()} 'mean'"
        )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_filename", default="data.csv")
    return vars(parser.parse_args())


def import_csv_as_dataframe(filename):
    df = pd.read_csv(filename, encoding="utf-16", sep="\t", skiprows=1)

    return df


if __name__ == "__main__":
    main()
