import argparse
import pandas as pd


def return_lorem():
    return "lorem"


def main():
    args = parse_args()
    df = import_csv_as_dataframe(args["csv_filename"])
    age_group = {
        "keine Angabe": -1,
        "<16": 1,
        "16-19": 2,
        "20-29": 3,
        "30-39": 4,
        "40-49": 5,
        "50-59": 6,
        ">60": 7,
    }

    for key in age_group.keys():
        df_new = filter_dataframe(df, "Alter", [age_group[key]])
        print(
            f"age group {key} : {df_new['Lokal vs Online: [Keine Beschreibung] 01'].mean()} 'mean'"
        )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_filename", default="data.csv")
    return vars(parser.parse_args())


def import_csv_as_dataframe(filename):
    return pd.read_csv(filename, encoding="utf-16", sep="\t", skiprows=1)


def filter_dataframe(dataframe, column_identifier, filter_params_arr):
    df_tmp = dataframe.copy()
    for x in dataframe.index:
        if dataframe.loc[x, column_identifier] not in filter_params_arr:
            df_tmp = df_tmp.drop(x, inplace=False)
    return df_tmp


if __name__ == "__main__":
    main()
