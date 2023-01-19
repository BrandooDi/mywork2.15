# !/usr/bin/env python3
# -*- coding: utf-8 -*


if __name__ == "__main__":
    # open the file.txt in append mode. Create a new file if no such file exists.
    with open("file.txt", "w") as fileptr:
        # appending the content to the file
        fileptr.write(
            "Python is the modern day language. It makes things so simple.\n"
            "It is the fastest-growing programing language"
        )

    # closing the opened file
    fileptr.close()