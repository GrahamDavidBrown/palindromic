import re


def is_palindrome(user_input):
    user_input = re.sub(r'[^A-Za-z"]', "", user_input).lower()
    length = len(user_input)
    if length % 2 != 0:
        user_input = user_input[:int(length / 2)] + user_input[int((length / 2) + 1):]
    first_half = user_input[0: int(length / 2)]
    second_half = user_input[int(length / 2): int(length)]
    rev_str = reverser(int(len(second_half)), list(second_half), "")
    if first_half == rev_str:
        return True
    else:
        return False


def reverser(count, second_half_list, rev_str):
    if second_half_list != []:
        rev_str += second_half_list.pop()
    if count <= 0:
        return rev_str
    count -= 1
    return reverser(count, second_half_list, rev_str)


def main():
    user_input = input("enter some text to determine if it is a palindrome: ")
    print(user_input)
    print(is_palindrome(user_input))


if __name__ == '__main__':
    main()
