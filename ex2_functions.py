import argparse

def print_file_content(file):
    with open(file) as file_obj:
        content = file_obj.readlines()
        print(content)

def write_list_to_file(output_file, lst):
    with open(output_file, "w") as file_obj:
        for element in lst:
            file_obj.write(str(element))
            file_obj.write("\n")

def write_list_to_file2(output_file, *strings):
    with open(output_file, "w") as file_obj:
        for string in strings:
            file_obj.write(string + "\n")

def read_csv(input_file):
    list = []
    with open(input_file) as file_obj:
        content = file_obj.readlines()

        for line in content:
            list.append(line)

    return list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Function to read csv files")
    parser.add_argument("csv_path", help="Path to csv file")
    parser.add_argument("-f", "--file", help="name of file you want to write to")

    args = parser.parse_args()
    print("csv path: ", args.csv_path)
    print("file: ", args.file)

    if not args.file:
        print_file_content(args.csv_path)
    else:
        list = read_csv(args.csv_path)
        write_list_to_file(args.file, list)