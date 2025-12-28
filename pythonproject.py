contacts={}

file=open("contacts.csv","w")
file.close()

while True:
    print("\n------Contact Book------")
    print("1.Add contact\n2.Update contact\n3.Delete contact\n4.Search contact\n5.View contact\n6.Show contacts\n7.Exit")

    choice=int(input("Enter your choice: "))
    
    match choice:
    
        case 1:
            name=input("Enter your name= ")
            if name in contacts:
                print(f"Contact name {name} is already exist!")
            else:
                age=int(input("Enter age: "))
                email=input("Enter email: ")
                mobile=input("Enter mobil number: ")
                contacts [name]={"age":age,"email":email,"mobile no":mobile}
                print("Contact successfully saved")

                file=open("contacts.csv","a")
                file.writelines(contacts[name])
                file.close()
               
        case 2:
            name=input("Enter name to update contact: ")
            if name in contacts:
                age=int(input("Enter updated age: "))
                email=input("Enter updated email: ")
                mobile=input("Enter updated mobile number: ")
                contacts[name]={"Age":age,"Email":email,"Mobile no":mobile}
                print("Contact updated Successfully")

                file=open("contacts.csv","w")
                file.write(contacts[name])
                file.close()

            else:
                print("Contact not found!")

        case 3:
            name=input("Enter name you wanted to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact name {name} deleted successfully!")
            else:
                print("Contact not found!")
            
        case 4:
            search_name = input("Enter name you wanted to search: ")
            found=False
            for name, cantact in contacts.items():
                if search_name.lower() in name.lower():
                    print(f"found- Name:{name}, Age:{age}, Email:{email}, Mobile no:{mobile}")
                    found = True
                if not found:
                    print("No contact found with that name")

        case 5:
            name=input("Enter contact name to view: ")
            if name in contacts:
                contact=contacts[name]
                print(f"Name:{name}, Age:{age}, Email:{email}, Mobile no:{mobile}")
            else:
                print("Contact not found")

        case 6:
            print(contacts.items())
            file=open("contacts.csv","r")
            var=file.read()
            print()
        case 7:
            print("------Exit Contact Book------")
            break

        case _:
            print("Enter valid input between 1-6: ")
                

           
           
        
