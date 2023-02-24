num = {
    'zero': 0,
    'one': 1,   
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

string = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine',]


def string_to_num(s):
    res = 0
    cur_num = ''
    c = 0
    while c < len(s):
        cur_num += s[c]
        c += 1
        if cur_num in num:
            res = res*10 + num[cur_num]
            cur_num = ""

    return res


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def num_to_string(nums):
    if (nums == 0):
        return ""   

    else:

        half_ans = string[nums % 10]
        ans = num_to_string(int(nums/10)) + half_ans

    return ans


input_1 = input("Enter the number 1")
num1 = string_to_num(input_1)

input_2 = input("Enter the number 2")
num2 = string_to_num(input_2)

gcd = int(gcd(num1, num2))

output = num_to_string(gcd)

print(output)
