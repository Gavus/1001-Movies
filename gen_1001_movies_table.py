#!/usr/bin/env python3
"""
Generate a markdown table based of movies.txt
"""

from argparse import ArgumentParser
from random import randint
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


def print_info(dataframe: DataFrame):
    "Print number of movies watched."

    nbr_titles = len(dataframe['Title'])
    nbr_watched = sum(x != "" for x in dataframe['Watched'])
    percentage = f"{100*nbr_watched/nbr_titles:.2f}%"
    print(f"Total movies watched: {nbr_watched}/{nbr_titles} {percentage}")


def get_not_watched(dataframe: DataFrame):
    "Print all movies not watched."

    res = dataframe.loc[(dataframe['Watched'] == '')]
    for i in res.index:
        year = dataframe['Year'][i]
        title = dataframe['Title'][i]
        print(f"{year} {title}")


def rand_not_watched(dataframe: DataFrame):
    "Randomly choose a movie not watched."

    res = dataframe.loc[(dataframe['Watched'] == '')]
    rand_i = randint(0, len(res.index))
    year = dataframe['Year'][rand_i]
    title = dataframe['Title'][rand_i]
    print(f"{year} {title}")


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

    cmds = [
        "save-csv", "save-table", "info", "list-not-watched",
        "rand-not-watched"
    ]

    parser = ArgumentParser(
        prog="Generate1001MoviesTable",
        description="Generate a markdown table based of movies.txt",
        epilog="text at the bottom of help")
    parser.add_argument("command", help="What to do", choices=cmds)
    args = parser.parse_args()

    dataframe = load_csv(CSVFILE)

    if args.command == "save-csv":
        save_csv(dataframe, CSVFILE)
    elif args.command == "save-table":
        save_markdown(dataframe, TABLEFILE)
    elif args.command == "info":
        print_info(dataframe)
    elif args.command == "list-not-watched":
        get_not_watched(dataframe)
    elif args.command == "rand-not-watched":
        rand_not_watched(dataframe)
    else:
        print("Error: Invalid option?")


if __name__ == "__main__":
    main()
