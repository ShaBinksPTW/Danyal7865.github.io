print("What is the secret number?")
answer = int(input())
if answer == 5:
    print("Correct Answer")
elif answer < 5:
    print("Secret number is higher than", answer)
    
elif answer > 5:
    print("Secret number is lower than", answer)
