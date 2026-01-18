print("___BASIC QUIZ GAME___")

# CREATE A FUNCTION
def quiz_game():
    print('\nWELCOME TO THE KIDS QUIZ GAME\n')
    print('Answer the following questions. Good luck!\n')

Questions = [{"Question": "1.what is the colour of the sky on a clear day?",
             'Options': ["A.GREEN", "B.BLUE", "C.RED"],
             "ANSWER": "B"},
             {
              "Question": "2. Which animal says 'Meow'?",
              'Options': ["A.DOG", "B.CAT", "C.COW"],
              "ANSWER": "B"},
             {
              "Question": "3. Which bird is known to be wise?",
              'Options': ["A.OWL", "B.PARROT" ,"C.CROW"],
              "ANSWER": "A"
             },
             {
              "Question": "4. Which food is made from milk?",
              'Options': ["A.BREAD", "B.RICE" ,"C.CHEESE"],
              "ANSWER": "C"},
             {
              "Question": "2. How many legs does a spider have?",
              'Options': ["A.8", "B.6" ,"C.10"],
              "ANSWER": "A"},
             ]

score = 0

"""LOOP THROUGH THE QUESTIONS"""
for question in Questions:
    print(question['Question'])
    for option in question['Options']:
        print(option)
    choice = input('Enter your choice (A/B/C): ').upper()

    if choice == question['ANSWER']:
        print('Correct!\n')
        score += 1
    else:
        print(f"Wrong Answer! The Correct Answer was {question['ANSWER']}.\n")

"""FINAL QUIZ GAME RESULTS"""
print(f'Your final score is: {score}/5')
if score >= 3:
    print('Congratulations! You passed the quiz game!')
else:
    print('Keep trying!' "you'll do better next time!")












