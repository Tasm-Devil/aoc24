import numpy as np

def read_string_from_file(filepath):
    with open(filepath, 'r') as file:
        matrix = [list(line.strip()) for line in file]
        return np.array(matrix)

def search_word(matrix, word):
    rows, cols = matrix.shape
    word_len = len(word)
    
    # Check all directions
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1), # down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (-1, 1)  # up-right
    ]
    found = 0
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if all(0 <= row + dr * k < rows and 0 <= col + dc * k < cols and matrix[row + dr * k, col + dc * k] == word[k] for k in range(word_len)):
                    found += 1
    return found

def search_pattern(matrix, pattern):
    rows, cols = matrix.shape
    pattern_rows, pattern_cols = len(pattern), len(pattern[0])
    found = 0

    for row in range(rows - pattern_rows + 1):
        for col in range(cols - pattern_cols + 1):
            match = True
            for pr in range(pattern_rows):
                for pc in range(pattern_cols):
                    if pattern[pr][pc] and matrix[row + pr, col + pc] != pattern[pr][pc]:
                        match = False
                        break
                if not match:
                    break
            if match:
                found += 1
    return found

def main_a(filepath):
    matrix = read_string_from_file(filepath)
    word = "XMAS"
    found = search_word(matrix, word)
    return found

def main_b(filepath):
    matrix = read_string_from_file(filepath)
    patterns = [
        [['M', '', 'S'], ['', 'A', ''], ['M', '', 'S']],
        [['M', '', 'M'], ['', 'A', ''], ['S', '', 'S']],
        [['S', '', 'M'], ['', 'A', ''], ['S', '', 'M']],
        [['S', '', 'S'], ['', 'A', ''], ['M', '', 'M']],
        [['M', '', 'S'], ['', 'A', ''], ['S', '', 'M']],
        [['S', '', 'M'], ['', 'A', ''], ['M', '', 'S']]
    ]

    total_found = 0
    for pattern in patterns:
        total_found += search_pattern(matrix, pattern)

    return total_found

if __name__ == "__main__":
    #print(main_a("inputs_2024/day_4_large.txt")) # 18 2536
    print(main_b("inputs_2024/day_4_large.txt")) # 9
