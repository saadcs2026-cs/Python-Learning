secret = 21
t = 1
guess = int(input("Enter your guess:  "))

while True:
    if guess==secret:
        print("Good Job, you did it in",t,"tries")
        break
    else:
        print("Try Again")
        t+=1
        guess = int(input("Enter your guess:  "))

