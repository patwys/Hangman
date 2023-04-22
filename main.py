word = "kiszony"

user_word = []

for _ in word:
    user_word.append("_")
print(user_word)

used_letters = []

no_of_tries = 5


def state_of_game():
    print()
    print()
    print(user_word)
    print(f"Your chances: {no_of_tries} ")
    print(f"Used letters: {used_letters}")
    print()
    print()


def is_letter(user_input):
    return not user_input.isalpha() or len(user_input) > 1


def already_exist(user_input, used_letters):
    return user_input in used_letters


def validate_input(user_input, used_letters):
    while is_letter(user_input) or already_exist(user_input, used_letters):
        if is_letter(user_input):
            user_input = input("Not a letter. Try again: ")
        if already_exist(user_input, used_letters):
            user_input = input("It's been used. Try again: ")
    return user_input


def find_indexes(user_input, word):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if user_input == letter_in_word:
            indexes.append(index)
    return indexes


while True:
    user_letter = input("Your letter: ")

    validated_input = validate_input(user_letter, used_letters)

    used_letters.append(validated_input)

    is_find_index = find_indexes(validated_input, word)

    if len(is_find_index) == 0:
        print("Missed. ")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("G.A.M.E.  O.V.E.R.")
            exit()

    else:
        for index in is_find_index:
            user_word[index] = validated_input
            if ''.join(user_word) == word:
                print("Y.O.U.  W.I.N.")
                exit()
    #    already_exist(user_letter, used_letters)
    state_of_game()

