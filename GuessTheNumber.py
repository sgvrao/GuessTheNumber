attempt = 5
while True:    
    if attempt == 0:
        print("Lost")
        break
    guess = int(input("Guess the Number : "))
    if guess == 7:
        print("Won")
        break   
    attempt -= 1
    print(f"try Again,attempts remaining {attempt}")        
