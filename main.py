from service import *
from conation import create_tabele 



create_tabele()

while True:
    n = int(input("===Menu===\n1)Create Task\n2)Get task by id\n0)Exit\nChouse one: "))
    match n:
        case 1:
            print("Start create task")
            title = input("Enter title name: ")
            descrp = input("Enter Descritption: ")
            durat = input("Enter Duration date yyyy-mm-dd: ")   
            create_task(title, descrp, durat)
        case 2:
            id = int(input("Enter id: "))
            get_task(id)
        case 0:
            print("Exit")
            break
        case _:
            print("Error: enter again")
        
        
    
            