# Guess The Number
# 1) Attempt = 5
# 2) Start a loop 
# 3) if Attempt == 0: Print(Lost)
# 4) Accept int 
# 5) Verify if number == 7
# 6) in case of True print Won else try again 
# 7) after 5 tries declare Lost

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
