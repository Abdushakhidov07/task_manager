from service import *
from conation import create_tabele 



create_tabele()

while True:
    n = int(input("===Menu===\n1)Create Task\n2)Get task by id\n3)Update\n0)Exit\nChouse one: "))
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
        case 3:
            id = int(input("id "))
            title = input("Enter title name: ")
            descrp = input("Enter Descritption: ")
            duration = input("Enter Duration date yyyy-mm-dd: ") 
            status = input("Enter status:")  
            update_task(id,title,descrp,duration,status)
                  
        case 0:
            print("Exit")
            break
        case _:
            print("Error: enter again")
            
        
        
    
            