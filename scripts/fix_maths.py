import sys


def usage():
    print("Usage: python3 fix_maths.py <filename>")


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        usage()
        return

    with open(filename, "r+") as in_file:
        file_txt = in_file.read()
    raw_txt = str(file_txt)
    file_txt = file_txt.replace("\\\\\\\\[", "$$")
    file_txt = file_txt.replace("\\\\\\\\]", "$$")
    file_txt = file_txt.replace("\\\\\\\\(", "$")
    file_txt = file_txt.replace("\\\\\\\\)", "$")
    if raw_txt == file_txt:
        print("No changes were made")
        return

    with open(filename, "w+") as out_file:
        out_file.write(file_txt)
    print("Successfully wrote to: {}".format(filename))


if __name__ == '__main__':
    main()
