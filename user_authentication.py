

username = input("Enter you username: ")
password = input("Enter your password: ")

while True:
    aux = input("Confirm your password: ")
    if aux == password:
        break
    print("Password confirmation failed")
    continue

condition = input("To continue logging in, press 'y': ")

if not condition == "y":
    print("Registration completed successfully! ")
else:
    username_login = input("Enter the username: ")
    password_login = input("Enter your password: ")

    if (username_login != username) and (password_login != password):
        print("Login failed")
    else:
        print ("Login completed")
    


