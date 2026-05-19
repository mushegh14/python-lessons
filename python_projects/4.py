import json

contacts = [
    {
        "id": 1,
        "name": "Aram",
        "phone": "091111111",
        "email": "aram@gmail.com",
        "address": "Gyumri",
    },
    {
        "id": 2,
        "name": "Ani",
        "phone": "077222222",
        "email": "ani@gmail.com",
        "address": "Yerevan",
    }
]


def show_menu():
    while True:

        print("___MENYU___")
        print("1. avelacnel kontakt:")
        print("2. voronel kontakt: ")
        print("3. ditel bolor kontaktnern: ")
        print("4. xmbagrel kontakt: ")
        print("5. jnjel kontakt: ")
        print("6. pahpanel kontakt: ")
        print("7. bernel kontakt: ")
        print("8. elq: ")

        number = input("Enter number: ")

        if number == "1":
            add_contact(contacts)
        elif number == "2":
            x = search_contact(contacts)
            if x is None:
                print("Nman kontakt goyutyun chuni")
            else:
                print("kontaktn goyutun uni")
                print(x)
            
        elif number == "3":
            show_all_contacts(contacts)
            
        elif number == "4":
            edit_contact(contacts)

        elif number == "5":
            save_contacts(contacts)
        elif number == "6":
            print("aystex klini phpanman bajin")
        elif number == "7":
            print("aystex klini berman bajin")
        elif number == "8":
            print("cragrayin avart")
            break
        else:
            print("sxal @ntrutyun , pordzeq noric")



def add_contact(contacts):
    contact_id = int(input("mutqarrir id" ))
    name = input("mutqagrir anunn")
    phone = input("mutqagrir heraxosi hamarn")
    email = input("mutagrir emaail ")
    address = input("mutqagrir hascen")

    now_list = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(now_list)

def search_contact(contacts):

    name = input("mutqagrel anunn").lower()

    for i in contacts:
        if i["name"].lower() == name:
            return i
    return None



def show_all_contacts(contacts):


    if len(contacts) == 0:
        print("kontaktner chkan")
        return

    for contact in contacts:
        print("ID:", contact["id"])
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])
        print("-" * 30)



def edit_contact(contacts):
    id_number = int(input("mutqagrir ID: "))

    for i in contacts:
        if i["id"] == id_number:
            while True:
                print("\n1. poxel id")
                print("2. poxel name")
                print("3. poxel phone")
                print("4. poxel email")
                print("5. poxel address")
                print("6. durs gal")

                num = input("vorn es uzum popoxel nshir tiv: ")

                if num == "1":
                    poxel_id = int(input("mutqagrir nor ID: "))
                    i["id"] = poxel_id
                    print("ID popoxvac e")

                elif num == "2":
                    poxel_name = input("mutqagrir nor anunn: ")
                    i["name"] = poxel_name
                    print("anunn poxvac e")

                elif num == "3":
                    poxel_phone = input("mutqagrel nor hmarn: ")
                    i["phone"] = poxel_phone
                    print("hmarn popoxvel e")

                elif num == "4":
                    poxel_email = input("mutqagrir nor emailn: ")
                    i["email"] = poxel_email
                    print("email popoxvel e")

                elif num == "5":
                    poxel_address = input("mutqarrir nor address: ")
                    i["address"] = poxel_address
                    print("address popoxvel e")

                elif num == "6":
                    print("xmbagrumic durs ekar")
                    return

                else:
                    print("sxal yntrutyun")

    print("nman id chka")


def delete_contact(contacts):
    id_number = int(input("mutqagrir jnjvox kontakti ID-n: "))

    for i in contacts:
        if i["id"] == id_number:
            contacts.remove(i)
            print("kontakt@ jnjvec")
            return

    print("nman ID-ov kontakt chka")

def save_contacts(contacts):

    with open("contact.json","w", encoding="utf-8") as f:
        json.dump(contacts,f,indent=4,ensure_ascii=False)
    
    print("kontaktner@ pahpanvecin contacts.json faylum")



show_menu()
