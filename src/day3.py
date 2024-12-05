import re

# Regular expression to find multiple occurrences of mul(x,x) where x is an integer
mul_pattern = r'mul\(\d+,\d+\)'
# find "do()" and "don't" in text
do_pattern = r'do\(\)'
dont_pattern = r'don\'t'   

def read_string_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main_a(filepath):
    #text = read_string_from_file("inputs_2024/day_3_small.txt")
    text = read_string_from_file(filepath)

    # Example usage
    matches = re.findall(mul_pattern, text)
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
    #xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

    # Combine all patterns into one
    combined_pattern = f'({mul_pattern})|({do_pattern})|({dont_pattern})'

    # Find all matches for the combined pattern
    all_matches = re.findall(combined_pattern, text)

    # Flatten the list of tuples and filter out empty strings
    all_matches = [match for group in all_matches for match in group if match]

    # Print all matches for debugging purposes
    #print("All matches:", all_matches)

    # Filter out mul-patterns that are between "don't" and "do()"
    filtered_matches = []
    skip = False
    for match in all_matches:
        if re.match(dont_pattern, match):
            skip = True
        elif re.match(do_pattern, match):
            skip = False
        elif re.match(mul_pattern, match) and not skip:
            filtered_matches.append(match)

    # Print filtered matches for debugging purposes
    #print("Filtered matches:", filtered_matches)

    # Extract the two numbers from each mul(x,x) match and store them in a list of tuples
    extracted_numbers = [tuple(map(int, re.findall(r'\d+', match))) for match in filtered_matches]
    
    # Print extracted numbers for debugging purposes
    #print("Extracted numbers:", extracted_numbers)

    # Multiply both numbers of each tuple and add all the products and return the sum
    total_sum = sum(a * b for a, b in extracted_numbers)
    
    return total_sum

if __name__ == "__main__":
    print(main_a("inputs_2024/day_3a_large.txt")) # 182619815
    print(main_b("inputs_2024/day_3b_large.txt")) # 80747545
