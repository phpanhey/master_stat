import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    args = parse_args()
    df = import_csv_as_dataframe(args["csv_filename"])
    df = filter_dataframe(df, "Ausschluss", [1])
    analyse_item_six_by_age(df)


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


def analyse_item_six_by_age(df):
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

    relevant_fields = [
        "Vorteile Online Shopping: Bequemlichkeit",
        "Vorteile Online Shopping: Flexibilität",
        "Vorteile Online Shopping: 24h-Verfügbarkeit",
        "Vorteile Online Shopping: Zeitersparnis",
        "Vorteile Online Shopping: Lieferung nach Hause",
        "Vorteile Online Shopping: Beratung",
        "Vorteile Online Shopping: Umfangreiche Produktbeschreibungen",
        "Vorteile Online Shopping: verschiedene Zahlungsmöglichkeiten",
    ]

    for relevant_field in relevant_fields:
        print(f"\n## Item: {relevant_field}##")
        res = []
        for key in age_group.keys():
            df_new = filter_dataframe(df, "Alter", [age_group[key]])
            mean = float(df_new[relevant_field].mean())
            res.append(mean)
            print(f"Altergruppe: {key} mittelwert: {str(mean)}")
        filename = relevant_field.replace("Vorteile Online Shopping: ", "") + ".png"
        plot(age_group.keys(), res, "Alter", relevant_field, filename)


def plot(x_arr, y_arr, x_label, y_label, filename):
    plt.bar(x_arr, y_arr)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(filename)
    plt.clf()


if __name__ == "__main__":
    main()
