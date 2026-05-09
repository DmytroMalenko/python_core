import os

def read_quiz(file):
    questions = []

    try:
        f = open(file, "r")
        for line in f:
            line = line.strip()
            if "|" in line:
                parts = line.split("|")
                if len(parts) == 6:

                    a = {
                        "text": parts[0],
                        "a": parts[1],
                        "b": parts[2],
                        "c": parts[3],
                        "d": parts[4],
                        "right": parts[5]
                    }
                    questions.append(a)

        f.close()

        return questions

    except FileNotFoundError: 
        print("File not found!")
        return 


def show_quizzes():

    files = ["music.txt", "geografy.txt", "sport.txt"]

    print("\nList of quiz :")

    i = 1

    for file in files:
        print(i, "-", file)
        i = i + 1

    return files



def play_quiz(questions, quiz_name):

    score = 0

    number = 1

    for a in questions:

        print("Quesrtions", number)
        print(a["text"])

        print("a)", a["a"])
        print("b)", a["b"])
        print("c)", a["c"])
        print("d)", a["d"])

        answer = input("Answer: ").strip().lower()

        if answer == a["right"].strip().lower():
            print("Right!")
            score = score + 1

        else:
            print("Uncorrect!")

        number = number + 1

    print("\nResults:", score, "/", len(questions))

    return score


def save_result(name, score, total):

    try:

        f = open("results.txt", "a")

        f.write(name + " : " + str(score) + "/" + str(total) + "\n")

        f.close()

    except Exception:

        print("Error!")


def create_quiz():
    print("===== Create New Quiz =====")
    
    quiz_name = input("Enter quiz name (e.g., animals.txt): ").strip()
    
    if quiz_name == "":
        print("Name can't be empty!")
        return
    
    if not quiz_name.endswith(".txt"):
        quiz_name = quiz_name + ".txt"
    
    file = "animals.txt" + quiz_name
    

    number1 = input("How many questions (5-10)? ").strip()
    
    num_question = int(number1)
    
    if num_question < 5 or num_question > 10:
        print("Number must be between 5 and 10!")
        return
    
    questions = [] 

    for i in range(num_question):
        print("Question:" + str(i+1) )

        text = input("Question text: ").strip()
        

        a = input("a: ").strip()
        b = input("b: ").strip()
        c = input("c: ").strip()
        d = input("d: ").strip()

        right = input("Right answer (a/b/c/d): ").strip().lower()
        
 
        while right == "a" and right == "b" and right == "c" and right == "d":
            print("Correct.")
            right = input("Right answer (a/b/c/d): ").strip().lower()
        

        question_line = text + "|" + a + "|" + b + "|" + c + "|" + d + "|" + right
        questions.append(question_line)

    
    print("Quiz " + quiz_name + " created successfully")


while True:

    print("\n===== Quiz =====")
    print("1 - List of Quiz")
    print("2 - Play")
    print("3 - Quit")
    print("4 - Create new Quiz")

    choice = input(">>> ")

    if choice == "1":

        show_quizzes()

    elif choice == "2":

        files = show_quizzes()

        num = int(input("Number of quiz: ")) - 1

        if 0 <= num < len(files):
            file = files[num]
            questions = read_quiz(file)

            if len(questions) > 0:

                score = play_quiz(questions, file)

                save_result(file, score, len(questions))

        else:

            print("There aren't this number!")

    elif choice == "3":

        print("Bye!")
        break

    elif choice == "4":
        create_quiz()

    else:

        print("Enter 1-3!")