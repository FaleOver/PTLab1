# -*- coding: utf-8 -*-
import argparse
import sys
import os.path as osp
from CalcRating import CalcRating
from CalcDebtCount import CalcDebtCount
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader
from DataReader import DataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    ext = osp.splitext(path)[-1]
    reader = ''
    print(ext)
    if ext == ".txt":
        reader = TextDataReader()
    elif ext == ".xml":
        reader = XMLDataReader()
    else:
        print("File format error")
        return

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debt = CalcDebtCount(students).calc()
    print("Debt: ", debt)


if __name__ == "__main__":
    main()
