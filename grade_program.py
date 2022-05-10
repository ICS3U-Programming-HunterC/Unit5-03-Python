#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 9, 2022
# This program gets your mark in number level and finds the middle
# percentage


def calc_mark(mark):
    # check what the middle mark is
    if mark == "1-":
        return "51%"
    elif mark == "1":
        return "55%"
    elif mark == "1+":
        return "58%"
    elif mark == "2-":
        return "61%"
    elif mark == "2":
        return "65%"
    elif mark == "2+":
        return "68%"
    elif mark == "3-":
        return "71%"
    elif mark == "3":
        return "75%"
    elif mark == "3+":
        return "78%"
    elif mark == "4-":
        return "83%"
    elif mark == "4":
        return "91%"
    elif mark == "4+":
        return "98%"
    else:
        return "1-"


def main():
    # get the mark
    mark_as_string = input("Enter your mark(ex. 4-): ")

    # call function
    calculated_mark = calc_mark(mark_as_string)

    # display the middle percentage
    print(
        "Level {0} has a middle percentage of {1}".format(
            mark_as_string, calculated_mark
        )
    )


if __name__ == "__main__":
    main()
