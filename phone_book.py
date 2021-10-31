contacts=[]
def add_contacts():
    name=input("enter a name")
    mobile=input("enter phone number")
    contact = (name,mobile)
    contacts.append(contact)
def print_list():
    print (contacts)

def search_list():
    name=input("enter name for search")
    for contact in contacts:
        contact[0]
        contact[1]
        if name==contact[0]:
            print(contact)
            break
    else:
        print("not found")
        
def search_phone():
    phone=input("enter a phone number")
    for contact in contacts:
        contact[0]
        contact[1]
        if phone==contact[1]:
            print(contact)
            break
    else:
        print("not found")
            
def save_contacts():
    handler=open("numbers2.txt","w")
    for contact in contacts:
        name,mobile=contact
        handler.write(f"{name},{mobile}\n")
    handler.close()     
        
