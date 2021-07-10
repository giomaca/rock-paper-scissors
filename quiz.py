# ---------------------------------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------------------")
        print(key)

        for ans in oprions[question_num - 1]:
            print(ans)

        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# ---------------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# ---------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print('------------------------------')
    print('RESULT')
    print('------------------------------')
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    for i in guesses:
        print(i, end=" ")
    print()

    score = (correct_guesses / len(guesses)) * 100
    print("%d" % score + "%")


# ---------------------------------------------------------------------
def play_again():
    ans = input("Play again (y or n): ")
    ans = ans.lower()
    if ans == "y":
        return True
    else:
        return False


# ---------------------------------------------------------------------

questions = {
    "Who create Python?: ": "A",
    "What years was Python created?: ": "B",
    "Python is tribute to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

oprions = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B False", "C. Sometimes", "D. Wha's Earth?"]
]

new_game()

while play_again():
    new_game()
print("Bye!")
