#!/usr/bin/env python3


def read(input: str) -> list[str]:
    ret = []
    with open(input, "r") as file:
        for line in file.readlines():
            if "+ [ ]" in line:
                line = line.removeprefix('+ [ ]').split()
                title = line[:-1]
                year = int(line[-1][1:-1])
                ret.append((" ".join(title), year))
    print(f"Found {len(ret)} movies")
    return ret

def gen_table(movies, output):
    with open(output, "w") as file:
        file.write("| Year | Title |\n")
        file.write("|------|-------|\n")
        for title, year in movies:
            file.write(f"| {year} | {title} |\n")


def main():
    movies = read("README.md")
    gen_table(movies, "table.md")


if __name__ == "__main__":
    main()

