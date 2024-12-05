import re

def read_string_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main_a(filepath):
    #text = read_string_from_file("inputs_2024/day_3_small.txt")
    text = read_string_from_file(filepath)

    # Regular expression to find multiple occurrences of mul(x,x) where x is an integer
    pattern = r'mul\(\d+,\d+\)'

    # Example usage
    matches = re.findall(pattern, text)
    # Extract the two numbers from each match and store them in a list of tuples
    extracted_numbers = [tuple(map(int, re.findall(r'\d+', match))) for match in matches]
    #print(extracted_numbers)
    # Output: [(2, 4), (3, 7), (32, 64), (11, 8), (8, 5)]

    # Multiply both numbers of each tuple and add all the products
    total_sum = sum(a * b for a, b in extracted_numbers)
    return total_sum

def main_b(filepath):
    #text = read_string_from_file("inputs_2024/day_3_small.txt")
    text = read_string_from_file(filepath)

    # Regular expression to find multiple occurrences of mul(x,x) where x is an integer
    pattern = r'mul\(\d+,\d+\)'
    # find "do()" and "don't" in text
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t'   

    # Example usage
    matches = re.findall(pattern, text)
    do_matches = re.findall(do_pattern, text)
    dont_matches = re.findall(dont_pattern, text)

    # Extract the two numbers from each match and store them in a list of tuples
    extracted_numbers = [tuple(map(int, re.findall(r'\d+', match))) for match in matches]
    print(extracted_numbers)
    # Output: [(2, 4), (3, 7), (32, 64), (11, 8), (8, 5)]

    # Multiply both numbers of each tuple and add all the products
    total_sum = sum(a * b for a, b in extracted_numbers)
    
    # Print the matches for "do()" and "don't"
    print(f'do() matches: {do_matches}')
    print(f'don\'t matches: {dont_matches}')
    
    return total_sum


#print(main_a("inputs_2024/day_3_large.txt"))
print(main_b("inputs_2024/day_3_small2.txt"))
