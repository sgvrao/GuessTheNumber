# # Guess The N
# 1) Start a Infinate loop
# 2) Accept int 
# 3) Verify if number == 7
# 4) in case of True print Won else try again/

while True:
    guess = int(input("Guess the Number : "))
    if guess == 7:
        print("Won")
        break
    else:
        print("try Again")