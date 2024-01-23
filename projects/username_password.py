def openapp():
    print("Welcome:::: ")

def start():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "user" or password != "password":
        raise ValueError("Invalid password")
    else:
        openapp()

try:
    start()
except ValueError:
    print("Username or password not correct")

except Exception as exp:
    print(f"Something else went wrong:::")
    print(exp)