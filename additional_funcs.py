student = []

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
        print("Bu adda tələbə yoxdu!")


# Tələbələrin siyahısının göstərilmə funksiyası:


def show_data():
    a = 1
    for user in student:
        user.show(a)
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

# Tələbə koduna görə tələbə məlumatlarının silinmə funksiyası:


def deleteData(student_psw):
    for user in student:
        if student_psw == user.password:
            student.remove(user)
            print("Daxil edilən koda uyğun tələbənin dataları sistemdən silindi!")
            break
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")


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
