# EXERCISE 1

def max_kernel(num_list, k):
    result = []
    i = 0
    j = k
    while i < len(num_list) and j < len(num_list) + 1:
        result.append(max(num_list[i:j]))
        i += 1
        j += 1

    return result


# EXERCISE 2


def character_count(word):
    character_statistic = {}

    # Your Code Here
    word = word.strip()
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    # End Code Here

    return character_statistic


# EXERCISE 3


def count_word(file_path):
    counter = {}

    # Your Code Here
    with open(file_path, 'r') as file:
        data = file.read().lower().split()
        for word in data:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    # End Code Here

    return counter


path = 'P1_data.txt'

word_count = count_word(path)
output = "{\n"
for (key, value) in word_count.items():
    output += f" '{key}' : {value},\n"
output += "}"
# print(output)

# EXERCISE 4


def levenshtein_distance(token1, token2):

    m = len(token1) + 1    # row
    n = len(token2) + 1    # column
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        matrix[i][0] = i
    for j in range(n):
        matrix[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            ins_cost = matrix[i][j - 1] + 1
            del_cost = matrix[i - 1][j] + 1
            sub_cost = matrix[i - 1][j - 1] + cost
            matrix[i][j] = min(ins_cost, del_cost, sub_cost)

    return matrix[m - 1][n - 1]


token1 = 'yu'
token2 = 'you'
# print(levenshtein_distance(token1, token2))


# Multiple choice

# Question 1

assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))

# Question 2


def character_count(word):
    character_statistic = {}

    # Your Code Here
    word = word.strip()
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    # End Code Here

    return character_statistic


assert character_count(" Baby ") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
# print(character_count('smiles'))

# Question 3

file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
# print(result['man'])

# Question 4

assert levenshtein_distance("hi", "hello") == 4
# print(levenshtein_distance("hola", "hello"))

# Question 5


def check_the_number(n):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Your code here
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)

    if n in list_of_numbers:
        result = "True"
    else:
        result = "False"

    return result


N = 7
assert check_the_number(N) == "False"

N = 2
result = check_the_number(N)
# print(result)

# Question 6


def append_list(data, max_val, min_val):
    result = []
    for i in data:
        # Your code here
        # Neu i < min thi them min vao result
        if i < min_val:
            result.append(min_val)
        elif i > max_val:
            result.append(max_val)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max_val = 1
min_val = 0
assert append_list(data=my_list, max_val=max_val,
                   min_val=min_val) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max_val = 2
min_val = 1
# print(append_list(data = my_list, max_val = max_val, min_val = min_val))

# Question 7


def extend_list(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert extend_list(list_num1, extend_list(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

# print(extend_list(list_num1, extend_list(list_num2, list_num3)))

# Question 8


def find_min_in_list(n):
    # Your code here
    return min(n)


my_list = [1, 22, 93, -100]
assert find_min_in_list(my_list) == -100

my_list = [1, 2, 3, -1]
# print(find_min_in_list(my_list))

# Question 9


def find_max_in_list(n):
    # Your code here
    return max(n)


my_list = [1001, 9, 100, 0]
assert find_max_in_list(my_list) == 1001

my_list = [1, 9, 9, 0]
# print(find_max_in_list(my_list))

# Question 10


def check_equal_num(integers, number=1):
    return any(x == number for x in integers)


my_list = [1, 3, 9, 4]
assert check_equal_num(my_list, -1) == False

my_list = [1, 2, 3, 4]
# print(check_equal_num(my_list, 2))

# Question 11


def find_mean(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


assert find_mean([4, 6, 8]) == 6
# print(find_mean())

# Question 12


def check_if_divisible_by_three(data):
    var = []
    for i in data:
        # Your code here
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    return var


assert check_if_divisible_by_three([3, 9, 4, 5]) == [3, 9]
# print(check_if_divisible_by_three([1, 2, 3, 5, 6]))

# Question 13


def factorial(y):
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var


assert factorial(8) == 40320
# print(factorial(4))

# Question 14


def reverse_string(x):

    # your code here
    x = list(x)
    x = x[::-1]
    reversed_string = ''.join(x)
    return reversed_string


x = 'I can do it'
assert reverse_string(x) == "ti od nac I"

x = 'apricot'
# print(reverse_string(x))

# Question 15


def check_positive_num(x):
    # Your code here
    # Neu x >0 tra ve 'T', nguoc lai tra ve 'N'
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function(data):
    res = [check_positive_num(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
# print(my_function(data))

# Question 16


def function_helper(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def find_unique_num(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert find_unique_num(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
# print(find_unique_num(lst))
