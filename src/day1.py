from collections import Counter

def read_file(filepath):
    list1 = []
    list2 = []
    
    with open(filepath, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.strip().split())
            list1.append(num1)
            list2.append(num2)
    
    return list1, list2

def main_a(filepath):
    list1, list2 = read_file(filepath)
    # Add your code here to process the lists or call other functions
    list1.sort()
    list2.sort()
    total = 0
    for i, j in zip(list1, list2):
        total += abs(j-i)
    return total

def main_b(filepath):
    list1, list2 = read_file(filepath)
    list2 = [x for x in list2 if x in list1]
    # Aggregate list2 and count each distinct value
    count_dict = dict(Counter(list2))
    values_list = [count_dict.get(x,0)*x for x in list1]
    return sum(values_list)

if __name__ == "__main__":
    print(main_a("inputs_2024/day_1_large.txt"))
    print(main_b("inputs_2024/day_1_large.txt"))
