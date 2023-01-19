# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == '__main__':
    with open("newfile.txt", "w") as data:
        data.write(os.environ.get("NUMBER_OF_PROCESSORS"))

    try:
        os.rename("newfile.txt", "myprocessor.txt")
        print("Файл успешно переименован")
    except FileExistsError:
        print("Файл уже существует")