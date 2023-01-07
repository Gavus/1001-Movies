#!/usr/bin/env python3

from pandas import DataFrame, read_csv
from numpy import nan


def load_csv(file: str) -> DataFrame:
    df = read_csv(file, sep=">")
    df.columns = df.columns.str.strip()
    df["Watched"] = df["Watched"].replace(nan, "")
    return df


def save_csv(df: DataFrame, file: str):
    df.to_csv(file, sep=">", index=False)


def save_markdown(df: DataFrame, file: str):
    md = df.to_markdown(index=False)
    if md is None:
        print("Error: Could not convert dataframe to markdown table")
        return
    with open(file, "w") as f:
        f.write(md)


def main():
    csvfile = "movies.txt"
    tablefile = "movies.md"
    df = load_csv(csvfile)
    save_markdown(df, tablefile)


if __name__ == "__main__":
    main()
