db = []


class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password

    def show(self):
        print(f"Tələbə{a} ad: {self.name}, soyad: isə {self.surname}.")


i = 1


def receive_data_register():
    global i
    x = int(input("İstifadəçilərin sayını qeyd edin : "))
    while i <= x:
        print(f"Tələbə{i} qeydiyyatı ==>")
        input_name = input("Adınızı daxil edin : ")
        input_surname = input("Soyadınızı daxil edin : ")
        input_username = input("İstifadəçi adınızı daxil edin : ")
        input_password = input("Şifrənizi daxil edin : ")
        obyekt = User(input_name, input_surname,
                      input_username, input_password)
        db.append(obyekt)
        i += 1
    return db


receive_data_register()
print(db)

a = 1


def show_data():
    global a
    for user in db:
        user.show()
        a += 1


show_data()


list1 = []
list2 = []


def longest_name():
    for user in db:  # db == database
        t = len(user.name)
        list1.append(t)
        list2.append(user.name)
    list1.sort()
    list1.reverse()
    for i in list2:
        if len(i) == list1[0]:
            print(i)
        else:
            pass


longest_name()
