import json


# Tələbə məlumatlarının dict-ə yığılması və 'student_db.json' faylına köçürülməsi:


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

# Tələbə adına görə tələbə məlumatlarının göstərilmə funksiyası:


def showData(student_name):
    i = 1
    for user in data['students']:
        if student_name == user['name']:
            print(f"Student{i}")
            print(user['name'])
            print(user['surname'])
            print(user['email'])
            print(user['telNumber'])
            i += 1
            break
    else:
        print("Bu adda tələbə yoxdu!")


# Bütün tələbə məlumatlarının göstərilmə funksiyası:


def allData():
    i = 1
    for user in data['students']:
        print(f"Student{i}")
        print(user['name'])
        print(user['surname'])
        print(user['email'])
        print(user['telNumber'])
        print(user['password'])
        i += 1

# Tələbə koduna görə tələbə məlumatlarının silinmə funksiyası:


def deleteData(student_psw):
    for user in data['students']:
        if student_psw == user['password']:
            data['students'].remove(user)
            with open("student_db.json", "w") as connect:
                json.dump(data, connect)
            print("Daxil edilən koda uyğun tələbənin dataları sistemdən silindi!")
            break
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")


# Tələbə koduna görə tələbə məlumatlarının dəyişdirilmə funksiyası:

def changeData(student_psw):
    for user in data['students']:
        if student_psw == user['password']:
            new_name = input("Yeni adınızı daxil edin: ")
            while new_name.isalpha() == False:
                print(
                    "Adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
                new_name = input("Yeni adınızı daxil edin: ")
            user['name'] = new_name

            new_surname = input("Yeni soyadınızı daxil edin: ")
            while new_surname.isalpha() == False:
                print(
                    "Soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")
                new_surname = input("Yeni soyadınızı daxil edin: ")
            user['surname'] = new_surname

            new_email = input("Yeni email adresinizi daxil edin: ")
            while "@" not in new_email:
                print("Yeni emailiniz standartlara uyğun deyil!")
                new_email = input("Yeni email adresinizi daxil edin: ")
            user['email'] = new_email

            new_telNumber = input("Yeni əlaqə nömrənizi daxil edin: +994")
            while new_telNumber.isdigit() == False or len(new_telNumber) != 9:
                print("Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")
                new_telNumber = input("Yeni əlaqə nömrənizi daxil edin: +994")
            user['telNumber'] = new_telNumber

            new_password = input("Yeni şifrənizi yazın: ")
            while new_password.isdigit() == False or len(new_password) != 3:
                print("Şifrə 3 rəqəmli ədəd olmalıdır!")
                new_password = input("Yeni şifrənizi yazın: ")
            user['password'] = new_password
            print("Qeydiyyatınız uğurla başa çatdı!")
            with open("student_db.json", "w") as connect:
                json.dump(data, connect)
            showData(new_name)
            break
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")
