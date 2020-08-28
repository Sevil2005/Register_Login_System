def checking_name(name):
    global _name
    while name.isalpha() == False:
        print("Adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
        name = input("Adınızı daxil edin: ")
    _name = name


def checking_surname(surname):
    global _surname
    while surname.isalpha() == False:
        print("Soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
        surname = input("Soyadınızı daxil edin: ")
    _surname = surname


def checking_email(email):
    global _email
    while "@" not in email:
        print("Düzgün email adresi daxil edin!")
        email = input("Email adresinizi daxil edin: ")
    _email = email


def checking_telNumber(telNumber):
    global _telNumber
    while telNumber.isdigit() == False or len(telNumber) != 9:
        print("Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")
        telNumber = input("Əlaqə nömrənizi daxil edin: +994")
    _telNumber = telNumber


def checking_password(password):
    global _password
    while password.isdigit() == False or len(password) != 3:
        print("Şifrə 3 rəqəmli ədəd olmalıdır!")
        password = input("Şifrənizi yazın: ")
    _password = password
