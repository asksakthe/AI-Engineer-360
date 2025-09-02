n =3
while (n>=1):
    password = input("Enter your password: ")
    passkey = "openAI123"
    if (password == passkey):
        print("Login Successful")
        break
    else:
        n -= 1
        print("Entered password is not matching, Try Again!!!")
        print(f"Attempt Left :{n}")