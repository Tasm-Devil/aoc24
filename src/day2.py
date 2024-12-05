def read_file(filepath):
    list1 = []
    
    with open(filepath, 'r') as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            list1.append(values)
    
    return list1

def is_safe(differences):
    return all(1 <= abs(diff) <= 3 for diff in differences) and (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences))

def main_a(filepath):
    lines = read_file(filepath)
    differences = []
    for line in lines:
        line_differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        if is_safe(line_differences):
            differences.append(line_differences)
            
        #print(line, " - ", line_differences, " - Safe" if line_differences in differences else " - Not Safe")
    return len(differences)

def main_b(filepath):
    lines = read_file(filepath)
    differences = []
    for line in lines:
        line_differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        
        # Überprüfen, ob die ursprüngliche Zeile "Safe" ist
        if is_safe(line_differences):
            differences.append(line_differences)
            #print(line, " - ", line_differences, " - Safe")
            continue
        
        # Überprüfen, ob die Zeile "Safe" wird, wenn genau ein Wert entfernt wird
        safe = False
        for i in range(len(line)):
            modified_line = line[:i] + line[i+1:]
            modified_differences = [modified_line[j + 1] - modified_line[j] for j in range(len(modified_line) - 1)]
            if is_safe(modified_differences):
                safe = True
                break
        #safe = any(is_safe([line[j + 1] - line[j] for j in range(len(line) - 1) if j != i]) for i in range(len(line)))
        
        
        if safe:
            differences.append(line_differences)
            #print(line, " - ", line_differences, " - Safe")
        else:
            #print(line, " - ", line_differences, " - Not Safe")
            pass
    
    return len(differences)

if __name__ == "__main__":
    print("Teil1s: ", main_a("inputs_2024/day_2_small.txt"))
    print("Teil1l: ", main_a("inputs_2024/day_2_large.txt"))
    print("Teil2s: ", main_b("inputs_2024/day_2_small.txt"))
    print("Teil2l: ", main_b("inputs_2024/day_2_large.txt"))