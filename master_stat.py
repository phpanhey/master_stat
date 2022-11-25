import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    args = parse_args()
    df = import_csv_as_dataframe(args["csv_filename"])
    df = filter_dataframe(df, "Ausschluss", [1])
    print_descriptive_statistic(df)


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


def print_descriptive_statistic(df):

    woman_count = len(filter_dataframe(df, "Geschlecht", [1]).index)
    man_count = len(filter_dataframe(df, "Geschlecht", [2]).index)
    divers_count = len(filter_dataframe(df, "Geschlecht", [3]).index)

    print(
        f"Es haben {len(df.index)} Personen teilgenommen. Davon waren {woman_count} weiblich, {man_count} männlich und {divers_count} divers."
    )

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
    count_20_29 =len(filter_dataframe(df, "Alter", [age_group['20-29']]).index)
    count_30_39 =len(filter_dataframe(df, "Alter", [age_group['30-39']]).index)
    count_40_49 =len(filter_dataframe(df, "Alter", [age_group['40-49']]).index)
    count_50_59 =len(filter_dataframe(df, "Alter", [age_group['50-59']]).index)
    count_greater_60 =len(filter_dataframe(df, "Alter", [age_group['>60']]).index)
    print(f"Die meinsten Teilnehmer waren im Alter von 20-29 Jahren (n={count_20_29}) und 30-39 Jahren (n={count_30_39}). Weniger vertreten war die Altersgruppe 40-49 Jahre(n={count_40_49}). Menschen über 50 Jahre waren {count_50_59 + count_greater_60}.")

    plot(list(age_group.keys()),[1, 0, 0, 36, 27, 8, 14, 10],"alterskategorie","teilnehmer","gender_participant.png")

    


def plot(x_arr,y_arr,x_label,y_label, filename):
    plt.bar(x_arr, y_arr)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(filename)
    



if __name__ == "__main__":
    main()
