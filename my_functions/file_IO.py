# Write file txt function
def write_file_txt(filename, list_data):
    with open(filename, "w") as f:
        for item in list_data:
            f.write(item)


# Read file txt function
def read_file_txt(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.rstrip("\n") for line in lines]
