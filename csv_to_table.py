#!/usr/bin/env python3

import pandas as pd


def read_csv(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, sep=">")
    df.columns = df.columns.str.strip()
    return df


def write_csv(df: pd.DataFrame, file: str):
    df.to_csv(file, sep=">", index=False)


def write_markdown(df: pd.DataFrame, file: str):
    md = df.to_markdown(index=False)
    if md is None:
        print("Error: Could not convert dataframe to markdown table")
        return
    with open(file, "w") as f:
        f.write(md)


def main():
    df = read_csv("movies.txt")
    write_markdown(df, "movies.md")


if __name__ == "__main__":
    main()
