print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark! Take charge and mark your territory!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne! You look amazing!")
elif username == "victor" and password == "Vi13tor":
 print("Hey there Victor! Continue winning today!")  
else:
 print("You do not have access. Go away!")

def endGame():
  while True:
    print()
    x= input(""""You do not have access. Go away!".
To try again please click Stop on top right page and click Run """)
    print()
    continue


if __name__ == "__main__":
  endGame()