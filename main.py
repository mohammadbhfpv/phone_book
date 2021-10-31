from phone_book import add_contacts
from phone_book import print_list
from phone_book import search_list
from phone_book import search_phone
from phone_book import save_contacts
def menu():
    while True:
        print("1.add")
        print("2.list")
        print("3.search,name")
        print("4.search,number")
        choice=input("enter a choice:")
        if choice=="1":
            add_contacts()
            save_contacts()
        if choice=="2":
            print("list of contacts...")
            print_list()
        if choice=="3":
            print("enter a name")
            search_list()
        if choice=="4":
            print("enter a phone number: ")
            search_phone()   


menu()    
    

