import os
import argparse

def get_file_names(folderpath, out="test files/output.txt"):
    files = os.listdir(folderpath)
    with open(out, "w") as file_object:
        file_object.write(str(files))

def get_all_file_names(folderpath, out="test files/output1.txt"):
    with open(out, "w") as file_object:
        for root, dirs, files in os.walk(folderpath):
            file_object.write(str(files))

def print_line_one(file_names):
    for file in file_names:
        for root, dirs, files in os.walk("."):
            if file in files:
                with open(file, "r") as file_object:
                    print(file_object.readline())

def print_emails(file_names):
    for file in file_names:
        for root, dirs, files in os.walk("."):
            if file in files:
                with open(file, "r") as file_object:
                    data = file_object.readlines()
                for line in data:
                    if line.__contains__("@"):
                        print(line)

def write_headlines(md_files, out="test files/output2.txt"):
    for file in md_files:
        for root, dirs, files in os.walk("."):
            if file in files:
                with open(file, "r") as file_object:
                    data = file_object.readlines()
                for line in data:
                    if line.startswith("#"):
                        with open(out, "w") as file_object_two:
                            file_object_two.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Application that can write file and folder names to txt files")
    parser.add_argument("-p", "--getpath", help="Path to folder")
    parser.add_argument("-ap", "--getallpaths", help="Path to folder you want the names of all files")
    parser.add_argument("-pl", "--printline", help="name of file you want the first line printed from")
    parser.add_argument("-pe", "--printemail", help="name of file you want to print emails from")
    parser.add_argument("-wh", "--writeheadline", help="name of markdown file you want to write headlines")

    args = parser.parse_args()

    if args.getpath:
        get_file_names(args.getpath)
    elif args.getallpaths:
        get_all_file_names(args.getallpaths)
    elif args.printline:
        print_line_one(args.printline)
    elif args.printemail:
        print_emails(args.printemail)
    elif args.writeheadline:
        write_headlines(args.writeheadline)