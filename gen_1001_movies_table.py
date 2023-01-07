#!/usr/bin/env python3

"""
Generate a markdown table based of movies.txt
"""

from argparse import ArgumentParser
from numpy import nan
from pandas import DataFrame, read_csv

CSVFILE = "movies.txt"
TABLEFILE = "movies.md"


def load_csv(csv: str) -> DataFrame:
    "Load csv file into dataframe."

    dataframe = read_csv(csv, sep=">")
    dataframe.columns = dataframe.columns.str.strip()
    dataframe["Watched"] = dataframe["Watched"].replace(nan, "")
    return dataframe


def save_csv(dataframe: DataFrame, csv: str):
    "Save dataframe as csv file."

    dataframe.to_csv(csv, sep=">", index=False)


def save_markdown(dataframe: DataFrame, markdown: str):
    "Save dataframe as markdown table."

    table = dataframe.to_markdown(index=False)
    if table is None:
        print("Error: Could not convert dataframe to markdown table")
        return
    with open(markdown, "w", encoding="utf-8") as file:
        file.write(table)


def main():
    "Main wrapper function."

    parser = ArgumentParser(
        prog="Generate1001MoviesTable",
        description="Generate a markdown table based of movies.txt",
        epilog="text at the bottom of help")
    parser.add_argument("command",
                        help="What to do",
                        choices=["save-table"])
    args = parser.parse_args()

    dataframe = load_csv(CSVFILE)

    if args.command == "save-table":
        save_markdown(dataframe, TABLEFILE)


if __name__ == "__main__":
    main()
