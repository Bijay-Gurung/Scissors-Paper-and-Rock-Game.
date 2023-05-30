import random
random.seed()

score = 0

def messages():
    message = "Welcome"
    x = message.center(50)
    print(x)

def humanVShuman():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    human1 = input("Player 1 choice: ")
    human2 = input("Player 2 choice: ")

    if human1 == "1" and human2 == "2":
        print("player2 wins")
    elif human1 == "1" and human2 == "3":
        print("player1 wins")
    elif human1 == "1" and human2 == "1":
        print("It's a draw")
    elif human1 == "2" and human2 == "1":
        print("player1 wins")
    elif human1 == "2" and human2 == "3":
        print("player2 wins")
    elif human1 == "2" and human2 == "2":
        print("It's a draw")
    elif human1 == "3" and human2 == "1":
        print("player2 wins")
    elif human1 == "3" and human2 == "2":
        print("player1 wins")
    elif human1== "3" and human2 == "3":
        print("It's a draw")

def Human_VS_AI(score):
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    human = input("Player Choice: ")
    computer = random.randint(1,3)
    print("Computer Choice:",computer)

    if human == "1" and computer == 1:
        print("It's draw")
    elif human == "1" and computer == 2:
        print("Computer Win")
        score -= 1
        print("your Score is:",score)
    elif human == "1" and computer == 3:
        print("You Win")
        score += 1
        print("your score is:", score)
    elif human == "2" and computer == 2:
        print("It's a draw")
    elif human == "2" and computer == 1:
        print("You Win")
        score += 1
        print("your score is:", score)
    elif human == "2" and computer == 3:
        print("Computer Win")
        score -= 1
        print("your score is:", score)
    elif human == "3" and computer == 3:
        print("It's a draw")
    elif human == "3" and computer == 1:
        print("Computer Win")
        score -= 1
        print("your score is:", score)
    elif human == "3" and computer == 2:
        print("You Win")
        score += 1
        print("your score is:", score)
    return score

def play_game(score):
    print("1. Human vs AI")
    print("2. Human vs Human")
    choice = input(">")

    if choice == "1":
        score = Human_VS_AI(score)
    elif choice == "2":
        humanVShuman()
    return score
def save_score(score):
    name = input("Enter Name: ")
    with open('Leaderboard.txt','a') as file:
        file.write(name+' '+str(score)+'\n')

def display_leaderboard():
    title = "leaderboard"
    x = title.center(50)
    print(x)
    with open('Leaderboard.txt','r') as file:
        data = file.read()
        print(data)
def main():
    global score
    messages()
    while True:
        print("1. Play Game")
        print("2. Save Score")
        print("3. Display Leaderboard")
        print("4. Quit")
        choice = input(">")

        if choice == "1":
            score = play_game(score)
        elif choice == "2":
            save_score(score)
        elif choice == "3":
            display_leaderboard()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again!")
main()
