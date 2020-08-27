# Tələbə class-ının yaradılması və listə yığılması:

student = []


class createStudent:
    def __init__(self, name, surname, email, telNumber, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.telNumber = telNumber
        self.password = password

    def show(self):
        print(
            f"Tələbə{a} adı : {self.name} / soyadı: {self.surname} / email: {self.email} / telefon nömrəsi: +994{self.telNumber}.")


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

# Tələbənin datalarının daxil edilmə prosesi:


def registering_system():
    n = input("Ümumi tələbə sayını daxil edin: ")
    if n.isdigit():
        n = int(n)
        for _ in range(0, n):
            name = input("Adınızı daxil edin: ")
            checking_name(name)
            surname = input("Soyadınızı daxil edin: ")
            checking_surname(surname)
            email = input("Email adresinizi daxil edin: ")
            checking_email(email)
            telNumber = input("Əlaqə nömrənizi daxil edin: +994")
            checking_telNumber(telNumber)
            password = input("Şifrənizi yazın: ")
            checking_password(password)
            s = createStudent(_name, _surname, _email, _telNumber, _password)
            student.append(s)
    else:
        print("Tələbə sayı rəqəm vəya ədəd olmalıdır!")

    print("Tələbələrin datalarının sistemə yerləşdirilmə prosesi sona çatdı!")


registering_system()


# Tələbə adına görə tələbə məlumatlarının göstərilmə funksiyası:


def showData(student_name):
    i = 1
    for user in student:
        if student_name == user.name:
            print(f"Student{i}")
            print(user.name)
            print(user.surname)
            print(user.email)
            print(user.telNumber)
            i += 1
            break
        else:
            pass
    else:
        print("Bu adda tələbə yoxdu!")


# Tələbələrin siyahısının göstərilmə funksiyası:

a = 1


def show_data():
    global a
    for user in student:
        user.show()
        a += 1

# Bütün tələbə məlumatlarının göstərilmə funksiyası:


def allData():
    i = 1
    for user in student:
        print(f"Student{i}")
        print(user.name)
        print(user.surname)
        print(user.email)
        print(user.telNumber)
        print(user.password)
        i += 1


# Tələbə koduna görə tələbə məlumatlarının dəyişdirilmə funksiyası:

def changeData(student_psw):
    for user in student:
        if student_psw == user.password:
            while True:
                new_name = input("Yeni adınızı daxil edin: ")
                if new_name.isalpha():
                    user.name = new_name
                    break
                else:
                    print(
                        "Adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

            while True:
                new_surname = input("Yeni soyadınızı daxil edin: ")
                if new_surname.isalpha():
                    user.surname = new_surname
                    break
                else:
                    print(
                        "Soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

            while True:
                new_email = input("Yeni email adresinizi daxil edin: ")
                if "@" in new_email:
                    user.email = new_email
                    break
                else:
                    print("Yeni emailiniz standartlara uyğun deyil!")

            while True:
                new_telNumber = input("Yeni əlaqə nömrənizi daxil edin: +994")
                if new_telNumber.isdigit() and len(new_telNumber) == 9:
                    user.telNumber = new_telNumber
                    break
                else:
                    print("Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")

            while True:
                new_password = input("Yeni şifrənizi yazın: ")
                if new_password.isdigit() and len(new_password) == 3:
                    user.password = new_password
                    print("Qeydiyyatınız uğurla başa çatdı!")
                    break
                else:
                    print("Şifrə 3 rəqəmli ədəd olmalıdır!")

            showData(new_name)
            break
        else:
            pass
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")

# Tələbə koduna görə tələbə məlumatlarının silinmə funksiyası:


def deleteData(student_psw):
    for user in student:
        if student_psw == user.password:
            student.remove(user)
            print("Daxil edilən koda uyğun tələbənin dataları sistemdən silindi!")
            break
        else:
            pass
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")


# Outputda görmək istədiyiniz əmrlərin verilməsi:
for i in range(100):
    command = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Tələbərin ümumi siyahısını görmək istəyirsinizsə-1
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə-2
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə-3
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə-4
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə-5 
                    ==>''')
    if command == "1":
        show_data()
    elif command == "2":
        name_input = input(
            "Datasını görmək istədiyiniz tələbənin adını daxil edin: ")
        showData(name_input)
    elif command == "3":
        while True:
            secret_psw = input("4-rəqəmli gizli şifrəni daxil edin: ")
            if secret_psw == "2005":
                allData()
                break
            else:
                print("Yanlış şifrə!")
    elif command == "4":
        psw_input = input(
            "Datasını dəyişmək istədiyiniz tələbənin kodunu daxil edin: ")
        changeData(psw_input)
    elif command == "5":
        psw_input = input(
            "Datasını silmək istədiyiniz tələbənin kodunu daxil edin: ")
        deleteData(psw_input)
    else:
        print("Belə funksionallıq yoxdur!Əldə etmək istədiyiniz məlumatlara uyğun düzgün ədədi daxil edin!")
