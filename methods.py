users = {}

with open("Authentication/usersdata.txt") as usersdata:
    datas = usersdata.read().split()
    key = ''
    for i in range(len(datas)):
        if i % 5 == 0:
            key = datas[i]
            users[key] = []
        else:
            users[key].append(datas[i])

emailtypes = ["gmail.com", "email.com", "outlook.com", "mail.ru"]

def white():
    print(f"\033[38;2;{255};{255};{255}m")

def red():
    print(f"\033[38;2;{255};{0};{0}m")

def yellow():
    print(f"\033[38;2;{255};{255};{0}m")

def green():
    print(f"\033[38;2;{0};{255};{0}m")

def cancel(x):
    x = x.lower()
    if x == "cancel":
        return exit(0)

def br():
    print("\n")

class LogIn:    
    def email(cancel, users, white, red, yellow, green):
        
        gm = input("Email: ").lower()
        cancel(gm)

        gmExist = True if gm in users.keys() else False

        while not gmExist:
            red()
            print("\nWrong email")
            white()
            gm = input("Please enter correct email \n>>> ").lower()
            cancel(gm)
            if gm in users.keys():
               gmExist = True
        
        return gm
    
    def password(cancel, users, gm, white, red, yellow, green):
        psw = input("\nPassword: ")
        cancel(psw)

        isPsw = True if users[gm][3] == psw else False

        while not isPsw:
            red()
            print("\nWrong password")
            white()
            psw = input("Please enter correct password \n>>> ")
            cancel(psw)
            if users[gm][3] == psw:
                isPsw = True
    
        green()
        print(f"\nHi, {users[gm][0].title()}!")
        print("\nThese are your infos")
        white()
        print(f"First Name: {users[gm][0].title()} \nLast Name: {users[gm][1].title()} \nPhone Number: {users[gm][2]} \nEmail: {gm.lower()} \nPassword: {users[gm][3]}")



class SignUp:
    def fname(cancel, white, red, yellow, green):
        fName = input("\nFirst Name: ")

        isFname = True if 65 <= ord(fName[0]) <= 90 else False

        while not isFname:
            yellow()
            print("\nFirst Letter of First Name should be upppercase letter")
            white()
            fName = input("First Name: ")

            isFname = True if 65 <= ord(fName[0]) <= 90 else False
        
        return fName
    def lname(cancel, white, red, yellow, green):
        lName = input("\nLast Name: ")

        isLname = True if 65 <= ord(lName[0]) <= 90 else False

        while not isLname:
            yellow()
            print("\nFirst Letter of Last Name should be upppercase letter")
            white()
            lName = input("Last Name: ")

            isLname = True if 65 <= ord(lName[0]) <= 90 else False
        
        return lName
    def number(cancel, white, red, yellow, green):
        telNumber = input("\nPhone Number (do not include + sign): ")
        cancel(telNumber)

        isTelNumber = True if telNumber.isdigit() else False

        while not isTelNumber:
            yellow()
            telNumber = input("\nPlease enter correct Phone Number \n >>> ")
            white()
            cancel(telNumber)

            isTelNumber = True if telNumber.isdigit() else False
        
        return telNumber

    def email(cancel, users, emailtypes, white, red, yellow, green):
        email = input("\nEmail: ")
        cancel(email)

        isEmail = False
        alreadyHas = True if email in users.keys() else False

        signs = ["`", "-", "=", "[", "]", ";", "'", ",", "/", "~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "+", "{", "}", "|", ":", '"', "<", ">", "?"]

        while not isEmail:
            for i in signs:
                if i in email:
                    red()
                    print(f"\nEmail should not include signs like {i}")
                    white()
                    email = input("Please enter correct email \n >>> ")
                    cancel(email)
                    alreadyHas = True if email in users.keys() else False
                    continue
            if alreadyHas:
                red()
                print("\nAccount with this email has already existed")
                white()
            elif not (email.isascii()):
                red()
                print("\nEmail should be in Latin letters")
                white()
                email = input("Please enter correct email \n >>> ")
                cancel(email)
                alreadyHas = True if email in users.keys() else False
            elif "@" in email:
                indSign = email.index("@")

                emailtype = email[indSign+1::]
                if emailtype in emailtypes:
                    isEmail = True
                else:
                    red()
                    print("\nThere is an error after @")
                    white()
                    email = input("Please enter correct email \n >>> ")
                cancel(email)
                alreadyHas = True if email in users.keys() else False
            else:
                red()
                print("\nEmail must have sign of @")
                white()
                email = input("Please enter correct email \n >>> ")
                cancel(email)
                alreadyHas = True if email in users.keys() else False
        
        return email
            

    def psw(cancel, white, red, yellow, green):
        password = input("\nPassword: ")
        cancel(password)

        signs = ["`", "-", "=", "[", "]", ";", "'", ",", ".", "/", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"]

        isLong = True if len(password) >= 8 else False
        hasUpper = False
        hasLower = False
        hasNumber = False
        hasSign = False
        hasEmpty = False if " " in password else True

        for i in password:
            if 48 <= ord(i) <= 57:
                hasNumber = True
            elif 65 <= ord(i) <= 90:
                hasUpper = True
            elif 97 <= ord(i) <= 122:
                hasLower = True
            elif i in signs:
                hasSign = True
    
        isPassword = True if isLong == True and hasUpper == True and hasLower == True and hasNumber == True and hasSign == True else False

        a = [isLong, hasUpper, hasLower, hasNumber, hasSign, hasEmpty]
        info = ["be 8 characters", "has one uppercase letter", "has one lowercase letter", "has number", "include one of these signs {~,!,`,@,#,$,%,^,&,*,(,),{,},_,-,=,+,\,|,[,],?,/,<,>,;,:,'}", "not be empty space"]

        while not isPassword:
            yellow()
            print("\nPassword must: ")
            for e in range(len(a)):
                if not a[e]:
                    print(f"* {info[e]} at least")
        
            red()
            password = input("\nPlease enter valid password \n >>> ")
            white()
            cancel(password)
            hasEmpty = False if " " in password else True
        
            isLong = True if len(password) >= 8 else False
            for i in password:
                if 48 <= ord(i) <= 57:
                    hasNumber = True
                elif 65 <= ord(i) <= 90:
                    hasUpper = True
                elif 97 <= ord(i) <= 122:
                    hasLower = True
                elif i in signs:
                    hasSign = True
        
            a = [isLong, hasUpper, hasLower, hasNumber, hasSign, hasEmpty]

            isPassword = True if isLong == True and hasUpper == True and hasLower == True and hasNumber == True and hasSign == True and hasEmpty == True else False

        return password

    def repws(cancel, users, password, telNumber, email, fName, lName, white, red, yellow, green):
        repassword = input("\nRetype Password: ")
        cancel(repassword)

        isRetypePassword = True if repassword == password else False

        while not isRetypePassword:
            red()
            print("\nRetype password must match password")
            white()
            repassword = input("Please enter correct Retype Password \n >>> ")
            cancel(repassword)

            isRetypePassword = True if repassword == password else False
    
        email = email.lower()
        fName = fName.lower()
        lName = lName.lower()

        with open('Authentication/usersdata.txt', 'a') as usersdata:
            usersdata.write(f" {email} {fName} {lName} {telNumber} {password}")

        green()
        print("Signed up Successfully!!!")
        white()