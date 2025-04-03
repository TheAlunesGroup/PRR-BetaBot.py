
from tkinter import *   
import customtkinter
import pexpect

#from datetime import datetime  

def GUI(): 
  customtkinter.set_appearance_mode("light") 
  customtkinter.set_default_color_theme("green")
  root = customtkinter.CTk() 
  root.title("PRR Bot") 
  root.geometry("600x900") 
  def Booking():    
    def Board_Selecter(values):
        if values == "BB":
            Rooms_Amount = customtkinter.CTkLabel(root, text="  How many rooms:        ",font=("Century Gothic", 20))
            Rooms_Amount.grid(row=3, column=0)  
            def Room_N(values): 
                if values == "one":
                    Type_Room = customtkinter.CTkLabel(root, text="Type of room                ", font=("Century Gothic", 20), justify=("left"))
                    Type_Room.grid(row=4, column=0)   
                    def Delux():  

                        NoAL = customtkinter.CTkLabel(root, text="How many adults aged(12 above)", font=("Century Gothic", 20)) 
                        NoAL.grid(row=5, column=0) 
                        NoAE = customtkinter.CTkEntry(root) 
                        NoAE.grid(row=5, column=1) 
                        NoC5L = customtkinter.CTkLabel(root, text="Children(0-5)", font=("Century Gothic", 20)) 
                        NoC5L.grid(row=6, column=0) 
                        NoC5E = customtkinter.CTkEntry(root)
                        NoC5E.grid(row=6, column=1)
                        NoC6L = customtkinter.CTkLabel(root, text="Children(6-11)", font=("Century Gothic", 20)) 
                        NoC6L.grid(row=7, column=0) 
                        NoC6E = customtkinter.CTkEntry(root)
                        NoC6E.grid(row=7, column=1) 
                        def Calculate(): 
                            NoA = NoAE.get()
                            NoC5 = NoC5E.get() 
                            NoC6 = NoC6E.get() 
                            try: 
                                NoA = int(NoA) 
                                NoC5 = int(NoC5) 
                                NoC6 = int(NoC6) 
                            except ValueError or NoA == () or NoC5 == () or NoC6 ==() or NoA < 2:
                                    NoAE.configure(text="ERROR") 
                                    NoC5E.configure(text="ERROR") 
                                    NoC6E.configure(text="ERROR")   
                            if (NoA+NoC5+NoC6) > 3:
                                    NoAE.configure(text="ERROR") 
                                    NoC5E.configure(text="ERROR") 
                                    NoC6E.configure(text="ERROR")  
                            NoA_Price = NoA * 12000  
                            if NoC6 == 0: 
                                NoC6_Price = 0
                            NoC6_Price = NoC6 * 4000 
                            match NoA: 
                                case 2: 
                                    NoA_price = 20000 
                                case 3: 
                                    NoA_price = 26000    
                            def refresh():  
                                Name = name.get() 
           
                                NoA = NoAE.get() 
                                NoC5 = NoC5E.get() 
                                NoC6 = NoC6E.get() 
                                Choose1 = Choose.get()  
                                add = int(NoA + NoC5 + NoC6) 
                                add_p = int(NoA_Price+NoA_price+NoC6_Price) 
                                ExtraMeal
                            def ExtraMeal(values):           
                                if values == "Normal":  
                                    add = int(NoA + NoC5 + NoC6)
                                    add_p = int(NoA_Price+NoA_price+NoC6_Price) 
                                    Result = customtkinter.CTkLabel(root, text = (f"Booking Summary \n Name: {name.get()} \n Date: \n Board: {Board1.get()} \n Amount of people: {add} \n Total Price: {(add_p) + (int(NoA)*2000) + int(NoC6)*1000}"), font=("Century Gothic", 20))
                                    Result.grid(row=10 , column=0) 
                                    Refresh = customtkinter.CTkButton(root, text="Refrsh", command=refresh) 
                                    Refresh.grid(row=14, column=0) 
                                elif values == "BBQ":
                                    add = int(NoA + NoC5 + NoC6)
                                    add_p = int(NoA_Price+NoA_price+NoC6_Price) 
                                    Result = customtkinter.CTkLabel(root, text = (f"Booking Summary \n Name: {name.get()} \n Date: \n Board: {Board1.get()} \n Amount of people: {add} \n Total Price: {(add_p) + int(NoA*4000+int(NoC6*2000))}"), font=("Century Gothic", 20))
                                    Result.grid(row=10 , column=0) 
                                    Refresh = customtkinter.CTkButton(root, text="Refrsh", command=refresh) 
                                    Refresh.grid(row=14, column=0) 
                            ChooseL = customtkinter.CTkLabel(root, text="Extra Meal Options", font=("Century Gothic", 20)) 
                            ChooseL.grid(row=9, column=0)
                            Choose = customtkinter.CTkComboBox(root, values=["Select", "Normal", "BBQ"], font=("Century Gothic", 20), command = ExtraMeal) 
                            Choose.grid(row=9, column=1) 
                        Next = customtkinter.CTkButton(root, text="Next", font=("Century Gothic", 20), command=Calculate) 
                        Next.grid(row=8, column=0)
                    def SelecterR(values): 
                        if values == "Delux":
                            Delux()
                    RoomSelect = customtkinter.CTkComboBox(root, values=["Selected", "Delux", "Standard"], font=("Century Gothic", 20), command=SelecterR) 
                    RoomSelect.grid(row=4, column=1) 

            RoomComboBox = customtkinter.CTkComboBox(root, values=["Select", "one", "two", "three", "four"], command=Room_N, font=("Century Gothic", 20))
            RoomComboBox.grid(row=3, column=1)
    Name = customtkinter.CTkLabel(root, text="  Name:                 ", font=("Custom Gothic", 20), justify="left")  
    name = customtkinter.CTkEntry(root, font=("Century Gothic", 26), justify="left") 
    Name.grid(row=0, column=0) 
    name.grid(column=1, row=0)
    Date = customtkinter.CTkLabel(root, text="  Date:                ", font=("Century Gothic", 20)) 
    date_Month = customtkinter.CTkComboBox(root, values=["Month", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]) 
    Date.grid(row=1, column=0) 
    date_Month.grid(row=1, column=1) 
    date_Day = customtkinter.CTkComboBox(root, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "20", "21", "22", "23", "24", "25", "26", "27","28","30", "31"])
    date_year = customtkinter.CTkComboBox(root, values=["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035"]) 
    date_Day.grid(row=1, column=2) 
    date_year.grid(row=1, column=3)
    Board = customtkinter.CTkLabel(root, text="  Board:                ", font=("Century Gothic", 20)) 
    Board.grid(row=2, column=0)  
    Board1 = customtkinter.CTkComboBox(root, values=["Select","BB", "HB", "FB"], command=Board_Selecter, font=("Century Gothic", 20))
    Board1.grid(row=2, column=1)
  Booking() 
  root.mainloop()



def booking(): 
    print("Enter the following infomation:") 
    Name = str(input("Name:")) 
    print("Enter the following for the date") 
    day = input("Day:")
    month = input("Month:") 
    rooms = int(input("How many rooms. Limit is 4:"))  
    nights = int(input("How many nights staying:"))
    if rooms == 1: 
        check1 = 0
        print("Which room would you like Delux or standered rooms")
        print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
        print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
        print("Note that we do not have single(1 person) rates")
        print("What do you choses. Delux(D) or Standard(S)") 
        response = input("")  

        
        if response == "D" or response == "Delux" or response == "delux" or response == "d" or response == "1" or response == "Standard" or response == "standard" or response == "S" or response == "s" or response == "2":
            check1 = 1 
        else:
            while check1 == 0: 
                print("Invalid value. Try again") 
                print("Which room would you like Delux or standered rooms")
                print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
                print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
                print("Note that we do not have single(1 person) rates")
                print("What do you choses. Delux(D) or Standard(S)") 
                response = input("") 
                if response == "D" or response == "Delux" or response == "delux" or response == "d" or response == "1" or response == "Standard" or response == "standard" or response == "S" or response == "s" or response == "2": 
                    check1 = check1 + 1 
                else: 
                    check1 = 0 
        check1 = check1 + 1
        if response == "D" or response == "Delux" or response == "delux" or response == "d" or response == "1":
            print("Enter the following people. The limit is 3:") 
            NoA = int(input("How many adults aged 13 and above:")) 
            check = 0
            if NoA <= 1: 
                while check < 1: 
                    print("There should be at least two adult. Try again")
                    NoA = int(input("How many adults aged 13 and above:")) 
                    if NoA < 0 and NoA < 1:
                        check = check + 1 
                    else: 
                        check = 0 
            NoC5 = int(input("How many children aged 0 - 5:")) 
            NoC6  = int(input("How many children aged 6 - 12:"))  
            add_P = NoA + NoC5 + NoC6 
            check = 0
            if add_P > 3 or add_P < 2:
                while check < 1: 
                    print("The limit has passed(3) or there is no more that two people. Try again") 
                    NoA = int(input("How many adults aged 13 and above:"))   
                    while check < 1: 
                         print("There should be at least two adult. Try again")
                         NoA = int(input("How many adults aged 13 and above:")) 
                         if NoA < 0 and NoA < 1:
                            check = check + 1 
                         else: 
                            check = 0
                    NoC5 = int(input("How many children aged 0 - 5:")) 
                    NoC6  = int(input("How many children aged 6 - 12:"))  
                    add_P = NoA + NoC5 + NoC6  
                    if add_P <= 3 and add_P > 0 and add_P > 1:
                        check = check + 1 
                    else: 
                        check = 0 
            check = check + 1 
            Price_NoA = (NoA * 12000) 
            if NoC6 == 0: 
                Price_NoC6 = 0
            Price_NoC6 = (NoC6 * 6000) 
            match NoA: 
                case 2: 
                    price_RMA = 22000 
                case 3: 
                    price_RMA = 27000 
            match NoC6: 
                case 1: 
                    price_RMC6 = 11000  
                case 0: 
                    price_RMC6 = 0
            add_price = price_RMA + price_RMC6 + Price_NoA + Price_NoC6 
            print("This will be sent to the owner:") 
            print(f"name:{Name}") 
            print(f"date:{day}/{month}/2025")
            print(f"Total amount of people:{add_P}") 
            print(f"Total price:{add_price}")
       
        elif response == "Standard" or response == "standard" or response == "S" or response == "s" or response == "2": 
            print("Enter the following infomation. The limit is 4:") 
            check = 0
            NoA = int(input("How many adults aged 13 and above:"))
            if NoA == 0 or NoA <= 1: 
                while check < 1: 
                    print("There should be at least two adult. Try again") 
                    NoA = int(input("How many adults aged 13 and above:")) 
                    if NoA < 0 and NoA < 1: 
                        check = check + 1 
                    else: 
                        check = 0 
            NoC5 = int(input("How many children aged 0 - 5:")) 
            NoC6 = int(input("How many children 6 - 12:")) 
            add_P = (NoA + NoC5 + NoC6) 
            check = 0 
            if add_P > 4: 
                while check < 1: 
                    print("The limit has passed(3) or there is no more that two people. Try again") 
                    NoA = int(input("How many adults aged 13 and above:"))   
                    while check < 1: 
                         print("There should be at least two adult. Try again")
                         NoA = int(input("How many adults aged 13 and above:")) 
                         if NoA < 0 and NoA < 1:
                            check = check + 1 
                         else: 
                            check = 0
                    NoC5 = int(input("How many children aged 0 - 5:")) 
                    NoC6  = int(input("How many children aged 6 - 12:"))  
                    add_P = NoA + NoC5 + NoC6  
                    if add_P <= 3 and add_P > 0 and add_P > 1:
                        check = check + 1 
                    else: 
                        check = 0  
            check = check + 1 
            Price_NoA = (NoA * 12000) 
            if NoC6 == 0: 
                Price_NoC6 = 0
            Price_NoC6 = (NoC6 * 6000) 
            match NoA: 
                case 2: 
                    price_RMA = 18000
                case 3: 
                    price_RMA = 21000 
                case 4: 
                    price_RMA = 23000
            match NoC6: 
                case 1: 
                    price_RMC6 = 9000
                case 2: 
                    price_RMC6 = 10500  
                
            add_price = price_RMA + price_RMC6 + Price_NoA + Price_NoC6 
            print("This will be sent to the owner:") 
            print(f"name:{Name}") 
            print(f"date:{day}/{month}/2025")
            print(f"Total amount of people:{add_P}") 
            print(f"Total price:{add_price}")
    if rooms == 2: 
        check1 = 0
        print("Which room would you like Delux or standered rooms")
        print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
        print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
        print("Note that we do not have single(1 person) rates")
        print("What do you choses. Two delux rooms(D), Two Standard rooms(S) or One standard and delux rooms(SD/DS)") 
        response = input(":") 
        if response == "DS" or response == "ds" or "SD" or response == "sd" or response == "3" or response == "D" or response == "d" or response == "1" or response == "S" or response == "s" or response == "2": 
            check1 = 1
        else: 
            while check1 == 0: 
              check1 = 0
              print("Error. Try again") 
              print("Which room would you like Delux or standered rooms")
              print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
              print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
              print("Note that we do not have single(1 person) rates")
              print("What do you choses. Two delux rooms(D), Two Standard rooms(S) or One standard and delux rooms(SD/DS)") 
              response = input(":")
              if response == "DS" or response == "ds" or "SD" or response == "sd" or response == "3" or response == "D" or response == "d" or response == "1" or response == "S" or response == "s" or response == "2": 
                check1= check1 + 1
              else: 
                 check = 0
            
        check1 = check1 + 1 
        if response == "D" or response == "d" or response == "1" or response == "Delux" or response == "delux":  
            check = 0
            print("Enter the following for the first delux room") 
            NoA = int(input("How many adults aged 13 and above:")) 
            NoC5 = int(input("How many children aged 0 - 5:")) 
            NoC6 = int(input("How many children aged 6 - 12:"))  
            print("Enter the following for room 2")  
            NoA1 = int(input("How many adults aged 13 and above:")) 
            NoC51 = int(input("How many children aged 0 - 5:")) 
            NoC61 = int(input("How many children aged 6 - 12:"))   
            add_P = NoA + NoC5 + NoC6 + NoA1 + NoC51 + NoC61 
            if add_P > 6 and add_P < 2:
                while check < 1: 
                    print("The total amount of people has passed or the there is less than two people, please try again") 
                    check = 0
                    print("Enter the following for the first delux room") 
                    NoA = int(input("How many adults aged 13 and above:")) 
                    NoC5 = int(input("How many children aged 0 - 5:")) 
                    NoC6 = int(input("How many children aged 6 - 12:"))  
                    print("Enter the following for room 2")  
                    NoA1 = int(input("How many adults aged 13 and above:")) 
                    NoC51 = int(input("How many children aged 0 - 5:")) 
                    NoC61 = int(input("How many children aged 6 - 12:"))   
                    add_P = NoA + NoC5 + NoC6 + NoA1 + NoC51 + NoC61 
                    if add_P > 2 and add_P <= 6: 
                        check = check + 1 
                    else: 
                        check =  0  
            check = check + 1  
            ADD_NOC6 = NoC6 + NoC61
            Price_NoA = (NoA1 + NoA) * 12000 
            Price_NoC6 = 0
            if ADD_NOC6 == 0 :
                Price_NoC6 == 0
            Price_NoC6 = (NoC6 + NoC61) * 6000
            match NoA: 
                case 2: 
                    price_RMA = 22000 
                case 3: 
                    price_RMA = 27000 
            match NoC6: 
                case 1: 
                    price_RMC6 = 11000 
                case 0: 
                    price_RMC6 = 0
            match NoA1: 
                case 2: 
                    price_RMA1 = 22000 
                case 3: 
                    price_RMA1 = 27000 
            match NoC6: 
                case 1: 
                    price_RMC61 = 11000 
                case 0: 
                    price_RMC61 = 0
            add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6
            print("This will be sent to the owner:") 
            print(f"name:{Name}") 
            print(f"date:{day}/{month}/2025")
            print(f"Total amount of people:{add_P}") 
            print(f"Total price:{add_price}")
       
        if response == "Standard" or response == "standard" or response == "S" or response == "s" or response == "2": 
            check = 0 
            check1 = 0
            print("Enter the following infomation for the first room") 
            NoA = int(input("How many adults aged 13 and above:")) 
            if NoA == 0 or NoA < 2: 
                while check1 < 1: 
                    print("You got an error. You need to have at least two adults or it may have passed the limit(4). Try again") 
                    NoA = int(input("How many adults aged 13 and above:"))  
                    if NoA > 1: 
                        check1 = check1 + 1 
                    else: 
                        check1 = 0
            NoC5 = int(input("How many children aged 0 - 5:")) 
            NoC6 = int(input("How many children aged 6 - 12:")) 
            print("Enter the the following for the second room")  
            check2 = 0
            NoA1 = int(input("How many adults aged 13 and above:")) 
            if NoA1 == 0 or NoA1 < 2: 
                while check2 < 1: 
                    print("You got an error. You need to have at least two adults or it may have passed the limit. Try again") 
                    NoA1 = int(input("How many adults aged 13 and above:"))  
                    if NoA1 > 1: 
                        check2 = check2 + 1 
                    else: 
                        check2 = 0
            NoC51 = int(input("How many children aged 0 - 5:")) 
            NoC61 = int(input("How many children aged 6 - 12:"))
            add_P = NoA + NoC5 + NoC6 + NoA1 + NoC51 + NoC61       
            if add_P > 8 or add_P < 2: 
                while check < 1: 
                    print("Error. The limit has passed(8)")
                    print("Enter the following infomation for the first room") 
                    NoA = int(input("How many adults aged 13 and above:")) 
                    if NoA == 0 or NoA < 2: 
                         while check1 < 1: 
                           print("You got an error. You need to have at least two adults or it may have passed the limit(4) Try again") 
                           NoA = int(input("How many adults aged 13 and above:"))  
                           if NoA > 1: 
                              check1 = check1 + 1 
                           else: 
                              check1 = 0
                    NoC5 = int(input("How many children aged 0 - 5:")) 
                    NoC6 = int(input("How many children aged 6 - 12:")) 
                    print("Enter the the following for the second room")  
                    check2 = 0
                    NoA1 = int(input("How many adults aged 13 and above:")) 
                    if NoA1 == 0 or NoA1 < 2: 
                       while check2 < 1: 
                           print("You got an error. You need to have at least two adults or has passed the limit(3), try again") 
                           NoA1 = int(input("How many adults aged 13 and above:"))  
                           if NoA1 > 1: 
                             check2 = check2 + 1 
                           else: 
                             check2 = 0
                    NoC51 = int(input("How many children aged 0 - 5:")) 
                    NoC61 = int(input("How many children aged 6 - 12:"))
                    add_P = NoA + NoC5 + NoC6 + NoA1 + NoC51 + NoC61       
                           
                    if add_P <= 8 and add_P > 1: 
                        while check < 1:  
                            check1 = 0
                            print("Enter the following infomation for the first room") 
                            NoA = int(input("How many adults aged 13 and above:")) 
                            if NoA == 0 or NoA < 2: 
                             while check1 < 1: 
                                 print("You got an error. You need to have at least two adults or it has passed the limit(4)") 
                                 NoA = int(input("How many adults aged 13 and above:"))  
                                 if NoA > 1: 
                                   check1 = check1 + 1 
                                 else: 
                                   check1 = 0
                            NoC5 = int(input("How many children aged 0 - 5:")) 
                            NoC6 = int(input("How many children aged 6 - 12:")) 
                            print("Enter the the following for the second room")  
                            NoA1 = int(input("How many adults aged 13 and above:")) 
                            if NoA1 == 0 or NoA1 < 2: 
                               while check1 < 1: 
                                   print("Error. There should be at least two adults or it may have passed the limit. Try again") 
                                   NoA1 = int(input("How many adults aged 13 and above:")) 
                                   if NoA1 > 1: 
                                       check1 = check1 + 1 
                                   else: 
                                       check1 = 0 
                            NoC51 = int(input("How many children aged 0 - 5:")) 
                            NoC61 = int(input("How many children aged 6 - 12:"))
                            add_P = NoA + NoC5 + NoC6 + NoA1 + NoC51 + NoC61   
                            if add_P <= 8:
                                check = 1 
                            else: 
                                check = 0   
            check = check + 1 
            addNoA = (NoA + NoA1) 
            AddNoA = (addNoA - 6) 
            Price_NoA = (8000 * AddNoA) + 72000  
            ADD_NOC6 = NoC6 + NoC61
            if ADD_NOC6 == 0 :
                Price_NoC6 == 0
            Price_NoC6 = (NoC61 + NoC6) * 6000
            match NoA: 
                case 2: 
                    price_RMA = 18000
                case 3: 
                    price_RMA = 21000 
                case 4: 
                    price_RMA = 23000
            match NoC6: 
                case 0: 
                    price_RMC6 = 0
                case 1: 
                    price_RMC6 = 9000
                case 2: 
                    price_RMC6 = 10500 
            match NoA1: 
                case 2: 
                    price_RMA1 = 18000
                case 3: 
                    price_RMA1 = 21000 
                case 4: 
                    price_RMA1 = 23000
            match NoC61: 
                case 0:
                    price_RMC61 = 0
                case 1: 
                    price_RMC61 = 9000
                case 2: 
                    price_RMC61 = 10500 
            add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6      
            print("This will be sent to the owner:") 
            print(f"name:{Name}") 
            print(f"date:{day}/{month}/2025")
            print(f"Total amount of people:{add_P}") 
            print(f"Total price:{add_price}")
         
        if response == "DS" or response == "ds" or response == "SD" or response == "sd" or response == "3": 
            check0 = 0 
            check1 = 0
            print("Enter the following for the first delux room:") 
            NoA = int(input("How many adults aged 13 and above:"))
            if NoA < 2 or NoA > 3: 
                while check < 1: 
                    print("Error, Try again") 
                    NoA = int(input("How many adults aged 13 and above:"))
                    if not NoA < 2 or not NoA > 3: 
                        check1 = 1 
                    else: 
                        check1 = 0 
            NoC5 = int(input("How many children aged 0 - 5:")) 
            NoC6 = int(input("How many children aged 6 - 12:")) 
            check2 = 0 
            print("Enter the following for the standard room:")
            NoA1 = int(input("How many adults aged 13 and above:")) 
            if NoA1 < 2 or NoA1 > 4:
                while check2 < 1: 
                    print("Error, try again") 
                    NoA1 = int(input("How many adults aged 13 and above"))
                    if not NoA < 2 or not NoA1 > 4: 
                        check2 = 1 
                    else: 
                        check2 = 0 
            NoC52 = int(input("How many children aged 0 - 5:"))
            NoC62 = int(input("How many children aged 6 - 12:")) 
            add_P = NoA + NoA1 + NoC5 + NoC51 + NoC6 + NoC61 
            if add_P > 7: 
                while check0 < 1: 
                    print("Error, Try again") 
                    check0 = 0 
                    check1 = 0
                    print("Enter the following for the first delux room:") 
                    NoA = int(input("How many adults aged 13 and above:"))
                    if NoA < 2 or NoA > 3: 
                        while check < 1: 
                            print("Error, Try again") 
                            NoA = int(input("How many adults aged 13 and above:"))
                            if not NoA < 2 or not NoA > 3: 
                                check1 = 1 
                            else: 
                                check1 = 0 
                    NoC5 = int(input("How many children aged 0 - 5:")) 
                    NoC6 = int(input("How many children aged 6 - 12:")) 
                    check2 = 0 
                    print("Enter the following for the standard room:")
                    NoA1 = int(input("How many adults aged 13 and above:")) 
                    if NoA1 < 2 or NoA1 > 4:
                        while check2 < 1: 
                           print("Error, try again") 
                           NoA1 = int(input("How many adults aged 13 and above"))
                           if not NoA < 2 or not NoA1 > 4: 
                              check2 = 1 
                           else: 
                              check2 = 0 
                    NoC52 = int(input("How many children aged 0 - 5:"))
                    NoC62 = int(input("How many children aged 6 - 12:")) 
                    add_P = NoA + NoA1 + NoC5 + NoC51 + NoC6 + NoC61 
                    if add_P <= 7: 
                        check0 = 1 
                    else: 
                        check0 = 0  
            check0 = 1 
            add_NoA = NoA + NoA1 
            if add_NoA > 6: 
                Price_NoA = (72000) + 8000 
            Price_NoA = add_NoA * 12000  
            if NoC6 == 0 or NoC61 == 0: 
                Price_NoC6 = 0 
            ADD_NOC6 = NoC6 + NoC61
            if ADD_NOC6 == 0 :
                Price_NoC6 == 0
            Price_NoC6 = (NoC6 + NoC61) * 8000 
            
            match NoA: 
                case 2: 
                    price_RMA = 22000 
                case 3: 
                    price_RMA = 27000 
            match NoA1: 
                case 2: 
                    price_RMA1 = 18000 
                case 3: 
                    price_RMA1 = 21000 
                case 4: 
                    price_RMA1 = 23000 
            match NoC6: 
                case 1: 
                    price_RMC6 = 11000  
            match NoC61: 
                case 2: 
                    price_RMC61 = 9000 
                case 3:
                    price_RMC61 = 10500 
            add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6 
            print("This will be sent to the owner:") 
            print(f"name:{Name}") 
            print(f"date:{day}/{month}/2025")
            print(f"Total amount of people:{add_P}") 
            print(f"Total price:{add_price}")
       
    if rooms == 3:  
           check01 = 0
           print("Which room would you like Delux or standered rooms")
           print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
           print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
           print("Note that we do not have single(1 person) rates")
           print("What do you choses. Two delux rooms and one standard room(DDS) or two standard rooms and one delux room(SSD)") 
           response = input("")  
           if response == "DDS" or response == "dds" or response == "1":  
               check01 = 1 
               check = 0
               print("Enter the following for the first delux room")
               NoA = int(input("How many adults aged 13 and above:")) 
               if NoA < 2: 
                   while check < 1: 
                       print("There should be at least two adults or it may have passed the limit(3)")
                       NoA = int(input("How many adults aged 13 and above:"))
                       if NoA > 1: 
                           check = check + 1 
                       else: 
                           check = 0 
               check = check + 1 
               NoC5 = int(input("How many children aged 0 - 5:")) 
               NoC6 = int(input("How many children aged 6 - 12:")) 
               print("Enter the following for the second delux room")  
               check1 = 0 
               NoA1 = int(input("How many adults aged 13 and above:")) 
               if NoA1 > 3 or NoA1 < 2: 
                   while check < 1: 
                       print("Error. It nedd at least two people or it has passed the limit(3). Try again") 
                       NoA1 = int(input("How many adults aged 13 and above:")) 
                       if NoA1 > 1 and NoA1 <= 4: 
                           check1 = check1 + 1 
                       else: 
                           check = 0 
               NoC51 = int(input("How many adults aged 0 - 5:")) 
               NoC62 = int(input("How many children aged 6 - 12:"))
               print("Enter the following for the standard room") 
               check2 = 0
               NoA2 = int(input("How many adults aged 13 and above:")) 
               if NoA2 > 4 or NoA2 < 2: 
                   while check < 1: 
                       print("Error. The amount of people has passed the limit(4) or there isnt 2 or more people") 
                       NoA2 = int(input("How many adults aged 13 and above:")) 
                       if NoA2 > 1 and NoA2 <= 4: 
                           check = check + 1 
                       else: 
                           check = 0 
               NoC52 = int(input("How many children aged  0 - 5:")) 
               NoC62 = int(input("How many children aged 6 - 12:")) 
               add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62  
               check3 = 0
               if add_P > 10: 
                   while check < 1: 
                       print("The limit has passed(10). Try again")
                       check = 0
                       print("Enter the following for the first delux room")
                       NoA = int(input("How many adults aged 13 and above:")) 
                       if NoA < 2: 
                         while check < 1: 
                             print("There should be at least two adults or it may have passed the limit(3)")
                             NoA = int(input("How many adults aged 13 and above:"))
                             if NoA > 1: 
                               check = check + 1 
                             else: 
                               check = 0 
                       check = check + 1 
                       NoC5 = int(input("How many children aged 0 - 5:")) 
                       NoC6 = int(input("How many children aged 6 - 12:")) 
                       print("Enter the following for the second delux room")  
                       check1 = 0 
                       NoA1 = int(input("How many adults aged 13 and above:")) 
                       if NoA1 > 3 or NoA1 < 2: 
                          while check < 1: 
                             print("Error. It nedd at least two people or it has passed the limit(3). Try again") 
                             NoA1 = int(input("How many adults aged 13 and above:")) 
                             if NoA1 > 1 and NoA1 <= 4: 
                                 check1 = check1 + 1 
                             else: 
                                check = 0 
                       NoC51 = int(input("How many adults aged 0 - 5:")) 
                       NoC62 = int(input("How many children aged 6 - 12:"))
                       print("Enter the following for the standard room") 
                       check2 = 0
                       NoA2 = int(input("How many adults aged 13 and above:")) 
                       if NoA2 > 4 or NoA2 < 2: 
                          while check < 1: 
                             print("Error. The amount of people has passed the limit(4) or there isnt 2 or more people") 
                             NoA2 = int(input("How many adults aged 13 and above:")) 
                             if NoA2 > 1 and NoA2 <= 4: 
                                check = check + 1 
                             else: 
                                check = 0 
                       NoC52 = int(input("How many children aged  0 - 5:")) 
                       NoC62 = int(input("How many children aged 6 - 12:")) 
                       add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62  
                       if add_P <= 10 and not add_P == 0: 
                           check3 = 0  
                       else: 
                           check3 = 0  

               check3 = check3 + 1 
               addNoA = NoA + NoA1 + NoA2 
               AddNoA = addNoA - 6
               Price_NoA = (AddNoA * 8000) + 72000  
               ADD_NOC6 = NoC6 + NoC61 + NoC62
               if ADD_NOC6 == 0 :
                  Price_NoC6 == 0
               Price_NoC6 = (NoC61 + NoC6 + NoC62) * 6000
               match NoA: 
                   case 2: 
                       price_RMA = 22000 
                   case 3: 
                       price_RMA = 27000 
               match NoA1: 
                   case 2: 
                       price_RMA1 = 22000 
                   case 3: 
                       price_RMA1 = 27000 
               match NoA2: 
                   case 2: 
                       price_RMA2 = 18000
                   case 3: 
                       price_RMA2 = 21000 
                   case 4: 
                       price_RMA2 = 23000

                   case 4: 
                       price_RMA2 = 23000 
               match NoC6: 
                   case 0: 
                       price_RMC6 = 0
                   case 1: 
                       price_RMC6 = 11000 
               match NoC61: 
                   case 1: 
                       price_RMC61 = 11000 
                   case 0: 
                       price_RMC6 = 0
               match NoC62: 
                   case 1: 
                       price_RMC62 = 9000 
                   case 2: 
                       price_RMC62 = 10500 
                   case 0: 
                       price_RMC6 = 0
               add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6 + price_RMA2 + price_RMC62 
               print("This will be sent to the owner:") 
               print(f"name:{Name}") 
               print(f"date:{day}/{month}/2025")
               print(f"Total amount of people:{add_P}") 
               print(f"Total price:{add_price}")
       
           if response == "SSD" or response == "ssd" or response == "2": 
               check01 = 1
               check0 = 0
               print("Enter the following for the first standard room")  
               check = 0
               NoA = int(input("How many adults aged 13 and above:"))  
               if NoA < 0 or NoA < 2: 
                   while check < 1: 
                       print("There is less than 2 people. Try again") 
                       NoA = int(input("How many adults aged 13 and above:")) 
                       if NoA > 1: 
                           check = check + 1 
                       else: 
                           check = 0  
               check = 1
               NoC5 = int(input("How many children aged 0 - 5:")) 
               NoC6 = int(input("How many children aged 6 - 12:")) 
               check1 = 0
               print("Enter the following for the first delux room") 
               NoA1 = int(input("How may adults aged 13 and above:")) 
               if NoA1 < 2 or NoA1 > 3: 
                   while check1 < 1: 
                       print("Error. The limit has passed the room limit(3) or the adults is less than 2. Try again") 
                       NoA1 = int(input("How may adults aged 13 and above:")) 
                       if NoA1 < 5 and NoA1 > 1: 
                           check1 = check1 + 1 
                       else: 
                           check1 = 0 
               check1 = 1
               NoC51 = int(input("How many children aged 0 -  5:")) 
               NoC61 = int(input("How many children aged 6 - 12:")) 
               check2 = 0 
               print("Enter the following standard room") 
               NoA2 = int(input("How may adults aged 13 and above:")) 
               if NoA2 < 2 or NoA2 > 4: 
                   while check < 1: 
                       print("Error. ") 
                       NoA2 = int(input("How many adults aged 3 and above")) 
                       if NoA2 > 1 and NoA2 < 5: 
                           check2 = check2 + 1 
                       else: 
                           check2 = 0  
               check2 = check2 + 1
               NoC52 = int(input("How many children aged 0 - 5:")) 
               NoC62 = int(input("How many children aged 6 - 12:")) 
               add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62 
               if add_P > 11: 
                   while check0 < 1: 
                       print("Error") 
                       check0 = 0
                       print("Enter the following for the first standard room")  
                       check = 0
                       NoA = int(input("How many adults aged 13 and above:"))  
                       if NoA < 0 or NoA < 2: 
                           while check < 1: 
                                print("There is less than 2 people. Try again") 
                                NoA = int(input("How many adults aged 13 and above:")) 
                                if NoA > 1: 
                                   check = check + 1 
                                else: 
                                   check = 0  
                       check = 1
                       NoC5 = int(input("How many children aged 0 - 5:")) 
                       NoC6 = int(input("How many children aged 6 - 12:")) 
                       check1 = 0
                       print("Enter the following for the first delux room") 
                       NoA1 = int(input("How may adults aged 13 and above:")) 
                       if NoA1 < 2 or NoA1 > 3: 
                           while check1 < 1: 
                                print("Error. The limit has passed the room limit(3) or the adults is less than 2. Try again") 
                                NoA1 = int(input("How may adults aged 13 and above:")) 
                                if NoA1 < 5 and NoA1 > 1: 
                                   check1 = check1 + 1 
                                else: 
                                   check1 = 0 
                       NoC51 = int(input("How many children aged 0 -  5:")) 
                       NoC61 = int(input("How many children aged 6 - 12:")) 
                       check2 = 0 
                       print("Enter the following standard room") 
                       NoA2 = int(input("How may adults aged 13 and above:")) 
                       if NoA2 < 2 or NoA2 > 4: 
                           while check < 1: 
                              print("Error. ") 
                              NoA2 = int(input("How many adults aged 3 and above")) 
                              if NoA2 > 1 and NoA2 < 5: 
                                    check2 = check2 + 1 
                              else: 
                                    check2 = 0   
                       check2 = 1
                       NoC52 = int(input("How many children aged 0 - 5:")) 
                       NoC62 = int(input("How many children aged 6 - 12:")) 
                       add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62  
                       if add_P <= 11: 
                           check0 = check0 + 1
                       else: 
                           check0 = 0 
               check0 = 1
               addNoA =  NoA + NoA1 + NoA2
               AddNoA = addNoA - 6
               ADD_NOC6 = NoC6 + NoC62 + NoC61 
               if ADD_NOC6 == 0: 
                   Price_NoC6 = 0
               Price_NoC6 = (ADD_NOC6) * 6000
               Price_NoA = (AddNoA * 8000) + 72000
               
               match NoA: 
                   case 2: 
                       price_RMA = 18000 
                   case 3: 
                       price_RMA = 21000 
                   case 4: 
                       price_RMA = 23000  
               match NoA1: 
                   case 2: 
                       price_RMA1 = 22000 
                   case 3: 
                       price_RMA1 = 27000 
               match NoA2: 
                   case 2: 
                       price_RMA2 = 18000 
                   case 3: 
                       price_RMA2 = 21000 
                   case 4: 
                       price_RMA2 = 23000
               match NoC6: 
                   case 1: 
                       Price_NoC6 = 9000 
                   case 2: 
                       Price_NoC6 = 10500 
               match NoC61: 
                   case 1: 
                       price_RMC61 = 11000 
               match NoC62: 
                   case 2: 
                       price_RMC62 = 9000 
                   case 3: 
                       price_RMC62 = 10500 
               add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6 + price_RMA2 + price_RMC62 
               print("This will be sent to the owner:") 
               print(f"name:{Name}") 
               print(f"date:{day}/{month}/2025")
               print(f"Total amount of people:{add_P}") 
               print(f"Total price:{add_price}") 
           else: 
               while check01 == 0:
                   print("Error, try again") 
                   print("Which room would you like Delux or standered rooms")
                   print("Delux rooms have connected toliets and one queen sized bed and a small bed. One person is 20000 and two people is 24000. aditonal is 2000. The limit for Delux is three people")
                   print("Standard rooms have two queen sized beds but dosent have connected bathrooms. One person is 17000, two people is 20000. aditional people is 8000. limit for stadered is 4 people")  
                   print("Note that we do not have single(1 person) rates")
                   print("What do you choses. Two delux rooms and one standard room(DDS) or two standard rooms and one delux room(SSD)") 
                   response = input("")  
                   if response == "SSD" or response == "ssd" or response == "2" or response == "DSS" or response == "dss" or response == "1":  
                       check01 = 1 
                   else: 
                       check01 = 0
                       
    if rooms == 4: 
               check0 = 0
               print("Enter the following for the first standard room")  
               check = 0
               NoA = int(input("How many adults aged 13 and above:"))  
               if NoA < 0 or NoA < 2: 
                   while check < 1: 
                       print("There is less than 2 people. Try again") 
                       NoA = int(input("How many adults aged 13 and above:")) 
                       if NoA > 1: 
                           check = check + 1 
                       else: 
                           check = 0  
               check = 1
               NoC5 = int(input("How many children aged 0 - 5:")) 
               NoC6 = int(input("How many children aged 6 - 12:")) 
               check1 = 0
               print("Enter the following for the first delux room") 
               NoA1 = int(input("How may adults aged 13 and above:")) 
               if NoA1 < 2 or NoA1 > 3: 
                   while check1 < 1: 
                       print("Error. The limit has passed the room limit(3) or the adults is less than 2. Try again") 
                       NoA1 = int(input("How may adults aged 13 and above:")) 
                       if NoA1 < 5 and NoA1 > 1: 
                           check1 = check1 + 1 
                       else: 
                           check1 = 0 
               check1 = 1
               NoC51 = int(input("How many children aged 0 -  5:")) 
               NoC61 = int(input("How many children aged 6 - 12:")) 
               check2 = 0 
               print("Enter the following standard room") 
               NoA2 = int(input("How may adults aged 13 and above:")) 
               if NoA2 < 2 or NoA2 > 4: 
                   while check < 1: 
                       print("Error. ") 
                       NoA2 = int(input("How many adults aged 3 and above")) 
                       if NoA2 > 1 and NoA2 < 5: 
                           check2 = check2 + 1 
                       else: 
                           check2 = 0  
               check2 = check2 + 1
               NoC52 = int(input("How many children aged 0 - 5:")) 
               NoC62 = int(input("How many children aged 6 - 12:")) 
               print("Enter the following for the second delux room") 
               check4 = 0 
               NoA4 = int(input("How many adults aged 13 and above")) 
               if NoA4 < 2 or NoA4 > 3:
                   while check4 < 1: 
                       print("Error, Try again")
                       NoA4 = int(input("How many adults aged 13 and above:")) 
                       if not NoA4 < 2 or not NoA4 > 3: 
                           check4 = 1
                       else:
                           check4 = 0
               NoC54 = int(input("How many children aged 0 - 5:")) 
               NoC64 = int(input("How many children aged 6 - 12:"))

               add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62 + NoA4 + NoC54 + NoC64
               if add_P > 14: 
                   while check0 < 1: 
                       print("Error") 
                       check0 = 0
                       print("Enter the following for the first standard room")  
                       check = 0
                       NoA = int(input("How many adults aged 13 and above:"))  
                       if NoA < 0 or NoA < 2: 
                           while check < 1: 
                                print("There is less than 2 people. Try again") 
                                NoA = int(input("How many adults aged 13 and above:")) 
                                if NoA > 1: 
                                   check = check + 1 
                                else: 
                                   check = 0  
                       check = 1
                       NoC5 = int(input("How many children aged 0 - 5:")) 
                       NoC6 = int(input("How many children aged 6 - 12:")) 
                       check1 = 0
                       print("Enter the following for the first delux room") 
                       NoA1 = int(input("How may adults aged 13 and above:")) 
                       if NoA1 < 2 or NoA1 > 3: 
                           while check1 < 1: 
                                print("Error. The limit has passed the room limit(3) or the adults is less than 2. Try again") 
                                NoA1 = int(input("How may adults aged 13 and above:")) 
                                if NoA1 < 5 and NoA1 > 1: 
                                   check1 = check1 + 1 
                                else: 
                                   check1 = 0 
                       NoC51 = int(input("How many children aged 0 -  5:")) 
                       NoC61 = int(input("How many children aged 6 - 12:")) 
                       check2 = 0 
                       print("Enter the following standard room") 
                       NoA2 = int(input("How may adults aged 13 and above:")) 
                       if NoA2 < 2 or NoA2 > 4: 
                           while check < 1: 
                              print("Error. ") 
                              NoA2 = int(input("How many adults aged 3 and above")) 
                              if NoA2 > 1 and NoA2 < 5: 
                                    check2 = check2 + 1 
                              else: 
                                    check2 = 0   
                       check2 = 1
                       NoC52 = int(input("How many children aged 0 - 5:")) 
                       NoC62 = int(input("How many children aged 6 - 12:")) 
                       check4 = 0 
                       NoA4 = int(input("How many adults aged 13 and above")) 
                       if NoA4 < 2 or NoA4 > 3:
                          while check4 < 1: 
                             print("Error, Try again")
                             NoA4 = int(input("How many adults aged 13 and above:")) 
                             if not NoA4 < 2 or not NoA4 > 3: 
                                check4 = 1
                             else:
                                check4 = 0
                       NoC54 = int(input("How many children aged 0 - 5:")) 
                       NoC64 = int(input("How many children aged 6 - 12:"))
                       add_P = NoA + NoA1 + NoA2 + NoC5 + NoC51 + NoC52 + NoC6 + NoC61 + NoC62 + NoA4 + NoC54 + NoC64
                       if add_P <= 14: 
                           check0 = check0 + 1
                       else: 
                           check0 = 0  
               check0 = 1
               addNoA =  NoA + NoA1 + NoA2 + NoA4
               AddNoA = addNoA - 6 
               ADD_NOC6 = NoC6 + NoC61 + NoC62 + NoC64
               if ADD_NOC6 == 0:
                  Price_NoC6 == 0
               Price_NoC6 = (NoC6 + NoC61 + NoC62 + NoC64) * 6000
               Price_NoA = (AddNoA * 8000) + 72000

               match NoA: 
                   case 2: 
                       price_RMA = 18000 
                   case 3: 
                       price_RMA = 21000 
                   case 4: 
                       price_RMA = 23000  
               match NoA1: 
                   case 2: 
                       price_RMA1 = 22000 
                   case 3: 
                       price_RMA1 = 27000 
               match NoA2: 
                   case 2: 
                       price_RMA2 = 18000 
                   case 3: 
                       price_RMA2 = 21000 
                   case 4: 
                       price_RMA2 = 23000 
               match NoA4: 
                   case 2: 
                       price_RMA4 = 22000 
                   case 3: 
                       price_RMA4 = 27000 
               match NoC6: 
                   case 0: 
                       Price_NoC6 = 0
                   case 1: 
                       Price_NoC6 = 9000 
                   case 2: 
                       Price_NoC6 = 10500 
               match NoC61: 
                   case 0:
                       price_RMC61 = 0
                   case 1: 
                       price_RMC61 = 11000  
               match NoC64:  
                   case 0: 
                       price_RMC64 = 0
                   case 1: 
                       price_RMC64 = 11000 
               match NoC62: 
                   case 0:
                       price_RMC62 = 0
                   case 2: 
                       price_RMC62 = 9000 
                   case 3: 
                       price_RMC62 = 10500  
               add_price = price_RMA + price_RMA1 + price_RMC6 + price_RMC61 + Price_NoA + Price_NoC6 + price_RMA2 + price_RMC62 + price_RMC64 + price_RMA4 
               print("This will be sent to the owner:") 
               print(f"name:{Name}") 
               print(f"date:{day}/{month}/2025")
               print(f"Total amount of people:{add_P}") 
               print(f"Total price:{add_price}") 
print("Thank you for contacting PowerHouse River Resort. Here are the folloing commands to interact.\n (Booking_) to make a booking.") 
response = str(input(""))   
    
if response == "booking_" or response == "Booking_": 
    booking() 
elif response == "Learnmore_" or response == "learnmore_": 
    print("coming soon")  
elif response == "GUI" or response == "gui":
    GUI()

# The last line 1037