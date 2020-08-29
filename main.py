import checking_funcs
import additional_funcs
import json

# Tələbə class-ının yaradılması və listə yığılması:


class dictGenerator(dict):
    def __init__(self):
        self = dict()

    def addKeyValue(self, key, value):
        self[key] = value


data = dictGenerator()
data.addKeyValue('students', [])


def createDict(_name, _surname, _email, _telNumber, _password):
    innerDict = dictGenerator()
    innerDict.addKeyValue('name', _name)
    innerDict.addKeyValue('surname', _surname)
    innerDict.addKeyValue('email', _email)
    innerDict.addKeyValue('telNumber', _telNumber)
    innerDict.addKeyValue('password', _password)
    return innerDict


class Student:
    def __init__(self, name, surname, email, telNumber, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.telNumber = telNumber
        self.password = password

    def show(self, a):
        print(
            f"Tələbə{a} adı : {self.name} / soyadı: {self.surname} / email: {self.email} / telefon nömrəsi: +994{self.telNumber}.")


# Tələbənin datalarının daxil edilmə prosesi:


def registering_system():
    n = input("Ümumi tələbə sayını daxil edin: ")
    if n.isdigit():
        n = int(n)
        for x in range(1, n+1):
            print(f"Tələbə{x} məlumatlarını daxil edin =>")
            name = input("Adınızı daxil edin: ")
            checking_funcs.checking_name(name)
            surname = input("Soyadınızı daxil edin: ")
            checking_funcs.checking_surname(surname)
            email = input("Email adresinizi daxil edin: ")
            checking_funcs.checking_email(email)
            telNumber = input("Əlaqə nömrənizi daxil edin: +994")
            checking_funcs.checking_telNumber(telNumber)
            password = input("Şifrənizi yazın: ")
            checking_funcs.checking_password(password)
            s = Student(checking_funcs._name, checking_funcs._surname,
                        checking_funcs._email, checking_funcs._telNumber, checking_funcs._password)
            additional_funcs.student.append(s)
            data['students'].append(createDict(checking_funcs._name, checking_funcs._surname,
                                               checking_funcs._email, checking_funcs._telNumber, checking_funcs._password))
    else:
        print("Tələbə sayı rəqəm vəya ədəd olmalıdır!")


registering_system()
print("Tələbələrin datalarının sistemə yerləşdirilmə prosesi sona çatdı!")
with open("student_db.json", "w") as connect:
    json.dump(data, connect)

# Outputda görmək istədiyiniz əmrlərin verilməsi:
command = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Tələbələrin ümumi siyahısını görmək istəyirsinizsə => 1
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə => 2
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə => 3
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə => 4
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə => 5
                    Əgər sistemdən çixmaq istəyirsinizsə bunu yazın => exit  
                    ==>''')
while command != "exit":
    if command == "1":
        additional_funcs.show_data()
    elif command == "2":
        name_input = input(
            "Datasını görmək istədiyiniz tələbənin adını daxil edin: ")
        additional_funcs.showData(name_input)
    elif command == "3":
        while True:
            secret_psw = input("4-rəqəmli gizli şifrəni daxil edin: ")
            if secret_psw == "2005":
                additional_funcs.allData()
                break
            else:
                print("Yanlış şifrə!")
    elif command == "4":
        psw_input = input(
            "Datasını dəyişmək istədiyiniz tələbənin kodunu daxil edin: ")
        additional_funcs.changeData(psw_input)
    elif command == "5":
        psw_input = input(
            "Datasını silmək istədiyiniz tələbənin kodunu daxil edin: ")
        additional_funcs.deleteData(psw_input)
    else:
        print("Belə funksionallıq yoxdur!Əldə etmək istədiyiniz məlumatlara uyğun düzgün ədədi daxil edin!")

    command = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Tələbələrin ümumi siyahısını görmək istəyirsinizsə => 1
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə => 2
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə => 3
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə => 4
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə => 5
                    Əgər sistemdən çixmaq istəyirsinizsə bunu yazın => exit  
                    ==>''')
