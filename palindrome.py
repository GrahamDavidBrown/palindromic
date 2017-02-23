import re


def is_palindrome(user_input):
    user_input = re.sub(r'[^A-Za-z"]', "", user_input).lower()
    length = len(user_input)
    if length % 2 != 0:
        user_input = user_input[:int(length / 2)] + user_input[int(length / 2) + 1:]
    second_half = reverser(len(user_input[int(length / 2):]), list(user_input[int(length / 2):]), "")
    if user_input[: int(length / 2)] == second_half:
        return True
    else:
        return False


def reverser(count, second_half_list, second_half):
    if second_half_list != []:
        second_half += second_half_list.pop()
    if count <= 0:
        return second_half
    count -= 1
    return reverser(count, second_half_list, second_half)


def main():
    playing = True
    while playing == True:
        user_input = input("enter some text to determine if it is a palindrome(QQ to quit): ")
        if user_input == "QQ": #Working as intended
            playing = False
        if is_palindrome(user_input):
            print(user_input + " is a palindrome.")
        else:
            print(user_input + " is not a palindrome.")

if __name__ == '__main__':
    main()
