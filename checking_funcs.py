def checking_name(name):
    global _name
    while True:
        if name.isalpha():
            _name = name
            break
        else:
            print("Adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
            name = input("Adınızı daxil edin: ")


def checking_surname(surname):
    global _surname
    while True:
        if surname.isalpha():
            _surname = surname
            break
        else:
            print("Soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
            surname = input("Soyadınızı daxil edin: ")


def checking_email(email):
    global _email
    while True:
        if "@" in email:
            _email = email
            break
        else:
            print("Düzgün email adresi daxil edin!")
            email = input("Email adresinizi daxil edin: ")


def checking_telNumber(telNumber):
    global _telNumber
    while True:
        if telNumber.isdigit() and len(telNumber) == 9:
            _telNumber = telNumber
            break
        else:
            print("Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")
            telNumber = input("Əlaqə nömrənizi daxil edin: +994")


def checking_password(password):
    global _password
    while True:
        if password.isdigit() and len(password) == 3:
            print("Qeydiyyatınız uğurla başa çatdı!")
            _password = password
            break
        else:
            print("Şifrə 3 rəqəmli ədəd olmalıdır!")
            password = input("Şifrənizi yazın: ")
