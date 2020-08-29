import checking_funcs
import additional_funcs
import json

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
            additional_funcs.data['students'].append(additional_funcs.createDict(checking_funcs._name, checking_funcs._surname,
                                                                                 checking_funcs._email, checking_funcs._telNumber, checking_funcs._password))
    else:
        print("Tələbə sayı rəqəm vəya ədəd olmalıdır!")


registering_system()
print("Tələbələrin datalarının sistemə yerləşdirilmə prosesi sona çatdı!")
with open("student_db.json", "w") as connect:
    json.dump(additional_funcs.data, connect)

# Outputda görmək istədiyiniz əmrlərin verilməsi:
command = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə => 1
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə => 2
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə => 3
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə => 4
                    Əgər sistemdən çixmaq istəyirsinizsə bunu yazın => exit  
                    ==>''')
while command != "exit":
    if command == "1":
        name_input = input(
            "datasını görmək istədiyiniz tələbənin adını daxil edin: ")
        additional_funcs.showData(name_input)
    elif command == "2":
        while True:
            secret_psw = input("4-rəqəmli gizli şifrəni daxil edin: ")
            if secret_psw == "2005":
                additional_funcs.allData()
                break
            else:
                print("Yanlış şifrə!")
    elif command == "3":
        psw_input = input(
            "datasını dəyişmək istədiyiniz tələbənin kodunu daxil edin: ")
        additional_funcs.changeData(psw_input)
    elif command == "4":
        psw_input = input(
            "datasını silmək istədiyiniz tələbənin kodunu daxil edin: ")
        additional_funcs.deleteData(psw_input)
    else:
        print("Belə funksionallıq yoxdur!Əldə etmək istədiyiniz məlumatlara uyğun düzgün ədədi daxil edin!")

    command = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə => 1
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə => 2
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə => 3
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə => 4
                    Əgər sistemdən çixmaq istəyirsinizsə bunu yazın => exit  
                    ==>''')
