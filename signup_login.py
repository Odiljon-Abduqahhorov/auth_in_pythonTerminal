from methods import SignUp, LogIn, cancel, users, emailtypes, br, white, red, yellow, green

yellow()
print("Instruction: enter 'cancel' in any input to exit program")
white()

x = input("Sign up or Log in (S / L) >>> ")
cancel(x) 

while not(x == "S" or x == "L"):
    x = input("Please enter valid word (S / L) >>> ")
    cancel(x)

if x == "L":
    gm = LogIn.email(cancel, users, white, red, yellow, green)
    LogIn.password(cancel, users, gm, white, red, yellow, green)
else:
    fname = SignUp.fname(cancel, white, red, yellow, green)
    lname = SignUp.lname(cancel, white, red, yellow, green)
    telNumber = SignUp.number(cancel, white, red, yellow, green)
    email = SignUp.email(cancel, users, emailtypes, white, red, yellow, green)
    password = SignUp.psw(cancel, white, red, yellow, green)
    SignUp.repws(cancel, users, password, telNumber, email, fname, lname, white, red, yellow, green)
