
def read_string_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main_a(filepath):
    input = read_string_from_file(filepath)
    return input

def main_b(filepath):
    input = read_string_from_file(filepath)
    return input

if __name__ == "__main__":
    print(main_a("inputs_2024/day_Xa_small.txt"))
    print(main_b("inputs_2024/day_Xb_small.txt"))
