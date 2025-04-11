import customtkinter

#Importing a library called customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root.geometry("600x6000")
root.title("PowerHouse River Resort Bot")

#Setting the frame and appearance

Name_Label = customtkinter.CTkLabel(root, text="Full Name")
Name_Label.grid(row=0, column=0)
Name_Entry = customtkinter.CTkEntry(root)
Name_Entry.grid(row=0, column=1)

#Collecting user's names

Starting_Date_Label = customtkinter.CTkLabel(root, text="Starting Date")
Starting_Date_Label.grid(row=1, column=0)
Starting_Date_Month = customtkinter.CTkComboBox(root, values=["Month","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
Starting_Date_Month.grid(row=1, column=1)
Starting_Date_Day = customtkinter.CTkComboBox(root, values=["Day","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
Starting_Date_Day.grid(row=1, column=2)
Starting_Date_Year = customtkinter.CTkComboBox(root, values=["Year","2025", "2026", "2027", "2028", "2029", "2030", "20231"])
Starting_Date_Year.grid(row=1, column=3)

#Collecting user's starting date

Ending_Date_Label = customtkinter.CTkLabel(root, text="Ending Date")
Ending_Date_Label.grid(row=2, column=0)
Ending_Date_Month = customtkinter.CTkComboBox(root, values=["Month","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
Ending_Date_Month.grid(row=2, column=1)
Ending_Date_Day = customtkinter.CTkComboBox(root, values=["Day","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
Ending_Date_Day.grid(row=2, column=2)
Ending_Date_Year = customtkinter.CTkComboBox(root, values=["Year","2025", "2026", "2027", "2028", "2029", "2030", "20231"])
Ending_Date_Year.grid(row=2, column=3)

#Collecting user's ending date

def next_steps(value1):
    if value1 == "BB":
        Room_Number_Label = customtkinter.CTkLabel(root, text="How many rooms:")
        Room_Number_Label.grid(row=4, column=0)

        def type_rooms(value):
            if value == "One":
                Type_room_Label = customtkinter.CTkLabel(root, text="Type of room:")
                Type_room_Label.grid(row=5, column=0)

                def People(val):
                    if val == "Deluxe":
                        Number_of_Adults_Label = customtkinter.CTkLabel(root, text="Amount of Adults(12 & above)")
                        Number_of_Adults_Label.grid(row=6, column=0)
                        Number_of_Adults_Entry = customtkinter.CTkEntry(root)
                        Number_of_Adults_Entry.grid(row=6, column=1)

                        Number_of_Children_Aged_0_5_Label = customtkinter.CTkLabel(root, text="Amount of Children(0-5)")
                        Number_of_Children_Aged_0_5_Label.grid(row=7, column=0)
                        Number_of_Children_Aged_0_5_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_0_5_Entry.grid(row=7, column=1)

                        Number_of_Children_Aged_6_11_Label = customtkinter.CTkLabel(root, text="Amount of Children(6-11")
                        Number_of_Children_Aged_6_11_Label.grid(row=8, column=0)
                        Number_of_Children_Aged_6_11_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_6_11_Entry.grid(row=8, column=1)

                        def calculate_and_result():
                            Name = str(Name_Entry.get())
                            Starting_date = f"{Starting_Date_Month.get()}/{Starting_Date_Day.get()}/{Starting_Date_Year.get()}"
                            Ending_date = f"{Ending_Date_Month.get()}/{Ending_Date_Day.get()}/{Ending_Date_Year.get()}"
                            Board = Board_ComboBox.get()
                            Number_of_Adults = (Number_of_Adults_Entry.get())
                            Number_of_Children_Aged_0_5 = (Number_of_Children_Aged_0_5_Entry.get())
                            Number_of_Children_Aged_6_11 = (Number_of_Children_Aged_6_11_Entry.get())

                            try:
                                Number_of_Adults = int(Number_of_Adults)
                                Number_of_Children_Aged_0_5 = int(Number_of_Children_Aged_0_5)
                                Number_of_Children_Aged_6_11 = int(Number_of_Children_Aged_6_11)

                            except ValueError:
                                Number_of_Adults_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_Entry.configure(placeholder_text="Error")

                            if int(Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11) > 3 or int(Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11) < 2:
                                Number_of_Adults_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_Entry.configure(placeholder_text="Error")

                            if Number_of_Children_Aged_0_5 == ():
                                Number_of_Children_Aged_0_5 = 0

                            elif Number_of_Children_Aged_6_11 == ():
                               Number_of_Children_Aged_6_11 = 0


                            NoA_Price = Number_of_Adults*12000
                            NoC6_Price = Number_of_Children_Aged_0_5*4000

                            match Number_of_Adults:
                                case 2:
                                    NoA_price = 20000
                                case 3:
                                    NoA_price = 26000

                            Extra_Meals_Label = customtkinter.CTkLabel(root, text="Extra Meal Options")
                            Extra_Meals_Label.grid(row=10, column=0)

                            def final_step(vale):
                                if vale == "Normal":
                                    if Starting_Date_Month == "Month" or Starting_Date_Day == "Day" or Starting_Date_Year == "Year" or Ending_Date_Month == "Month" or Ending_Date_Day == "Day" or Ending_Date_Year == "Year":
                                        Starting_Date_Day.configure(placeholder_text="Error")
                                        Starting_Date_Month.configure(placeholder_text="Error")
                                        Starting_Date_Year.configure(placeholder_text="Error")
                                        Ending_Date_Day.configure(placeholder_text="Error")
                                        Ending_Date_Month.configure(placeholder_text="Error")
                                        Ending_Date_Year.configure(placeholder_text="Error")

                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_date} \n Ending Date:{Ending_date}\n Board{Board} \n Total amount of people:{Number_of_Adults+Number_of_Children_Aged_0_5+Number_of_Children_Aged_6_11} \n Extra Meal:Normal \n"f"Expected Price:{NoA_Price+NoA_price+NoC6_Price+(Number_of_Adults*2000)+(Number_of_Children_Aged_6_11*1000)}")
                                    Result.grid(row=11, column=0)

                                elif vale == "BBQ":
                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_date} \n Ending Date:{Ending_date}\n Board{Board} \n Total amount of people:{Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11} \n Extra Meal:BBQ \n Expected Price:{NoA_Price + NoA_price + NoC6_Price + (Number_of_Adults * 2000) + (Number_of_Children_Aged_6_11 * 1000)}")
                                    Result.grid(row=11, column=0)
                            Extra_Meals_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "Normal", "BBQ"], command=final_step)
                            Extra_Meals_ComboBox.grid(row=10, column=1)

                        Next_Button = customtkinter.CTkButton(root, text="Next", command=calculate_and_result)
                        Next_Button.grid(row=9, column=0)

                    if val == "Standard":
                        Number_of_Adults_Label = customtkinter.CTkLabel(root, text="Amount of Adults(12 & above)")
                        Number_of_Adults_Label.grid(row=6, column=0)
                        Number_of_Adults_Entry = customtkinter.CTkEntry(root)
                        Number_of_Adults_Entry.grid(row=6, column=1)

                        Number_of_Children_Aged_0_5_Label = customtkinter.CTkLabel(root, text="Amount of Children(0-5)")
                        Number_of_Children_Aged_0_5_Label.grid(row=7, column=0)
                        Number_of_Children_Aged_0_5_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_0_5_Entry.grid(row=7, column=1)

                        Number_of_Children_Aged_6_11_Label = customtkinter.CTkLabel(root,
                                                                                    text="Amount of Children(6-11")
                        Number_of_Children_Aged_6_11_Label.grid(row=8, column=0)
                        Number_of_Children_Aged_6_11_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_6_11_Entry.grid(row=8, column=1)

                        def calculate_and_result():
                            Name = (Name_Entry.get())
                            Starting_date = f"{Starting_Date_Month.get()}/{Starting_Date_Day.get()}/{Starting_Date_Year.get()}"
                            Ending_date = f"{Ending_Date_Month.get()}/{Ending_Date_Day.get()}/{Ending_Date_Year.get()}"
                            Board = Board_ComboBox.get()
                            Number_of_Adults = (Number_of_Adults_Entry.get())
                            Number_of_Children_Aged_0_5 = (Number_of_Children_Aged_0_5_Entry.get())
                            Number_of_Children_Aged_6_11 = (Number_of_Children_Aged_6_11_Entry.get())

                            try:
                                Number_of_Adults = int(Number_of_Adults)
                                Number_of_Children_Aged_0_5 = int(Number_of_Children_Aged_0_5)
                                Number_of_Children_Aged_6_11 = int(Number_of_Children_Aged_6_11)

                            except ValueError:
                                Number_of_Adults_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_Entry.configure(placeholder_text="Error")

                            if int(Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11) > 4 or int(Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11) < 2:
                                Number_of_Adults_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_Entry.configure(placeholder_text="Error")

                            if Number_of_Children_Aged_0_5 == ():
                                Number_of_Children_Aged_0_5 = 0

                            elif Number_of_Children_Aged_6_11 == ():
                                Number_of_Children_Aged_6_11 = 0

                            NoA_Price = Number_of_Adults * 12000
                            NoC6_Price = Number_of_Children_Aged_0_5 * 4000

                            match Number_of_Adults:
                                case 2:
                                    NoA_price = 18000
                                case 3:
                                    NoA_price = 23000
                                case 4:
                                    NoA_price = 27000
                            Extra_Meals_Label = customtkinter.CTkLabel(root, text="Extra Meal Options")
                            Extra_Meals_Label.grid(row=10, column=0)

                            def final_step(vale):
                                if vale == "Normal":
                                    if Starting_Date_Month == "Month" or Starting_Date_Day == "Day" or Starting_Date_Year == "Year" or Ending_Date_Month == "Month" or Ending_Date_Day == "Day" or Ending_Date_Year == "Year":
                                        Starting_Date_Day.configure(placeholder_text="Error")
                                        Starting_Date_Month.configure(placeholder_text="Error")
                                        Starting_Date_Year.configure(placeholder_text="Error")
                                        Ending_Date_Day.configure(placeholder_text="Error")
                                        Ending_Date_Month.configure(placeholder_text="Error")
                                        Ending_Date_Year.configure(placeholder_text="Error")

                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_date} \n Ending Date:{Ending_date}\n Board{Board} \n Total amount of people:{Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11} \n Extra Meal:Normal \n"f"Expected Price:{NoA_Price + NoA_price + NoC6_Price + (Number_of_Adults * 2000) + (Number_of_Children_Aged_6_11 * 1000)}")
                                    Result.grid(row=11, column=0)

                                elif vale == "BBQ":
                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_date} \n Ending Date:{Ending_date}\n Board{Board} \n Total amount of people:{Number_of_Adults + Number_of_Children_Aged_0_5 + Number_of_Children_Aged_6_11} \n Extra Meal:BBQ \n Expected Price:{NoA_Price + NoA_price + NoC6_Price + (Number_of_Adults * 2000) + (Number_of_Children_Aged_6_11 * 1000)}")
                                    Result.grid(row=11, column=0)

                            Extra_Meals_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "Normal", "BBQ"], command=final_step)
                            Extra_Meals_ComboBox.grid(row=10, column=1)

                        Next_Button = customtkinter.CTkButton(root, text="Next", command=calculate_and_result)
                        Next_Button.grid(row=9, column=0)

                Type_room_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "Deluxe", "Standard"], command=People)
                Type_room_ComboBox.grid(row=5, column=1)

            if value == "Two":
                Type_room_Label = customtkinter.CTkLabel(root, text="Type of room:")
                Type_room_Label.grid(row=5, column=0)

                def People(val):
                    if val == "Double Deluxe":
                        Room_1_Label = customtkinter.CTkLabel(root, text="Room No.1")
                        Room_1_Label.grid(row=6, column=0)

                        Number_of_Adults_Room_1_Label = customtkinter.CTkLabel(root, text="How many Adults(12 & above")
                        Number_of_Adults_Room_1_Label.grid(row=7, column=0)
                        Number_of_Adults_Room_1_Entry = customtkinter.CTkEntry(root)
                        Number_of_Adults_Room_1_Entry.grid(row=7, column=1)

                        Number_of_Children_Aged_0_5_1_Label = customtkinter.CTkLabel(root, text="How Many children(0-5)")
                        Number_of_Children_Aged_0_5_1_Label.grid(row=8, column=0)
                        Number_of_Children_Aged_0_5_1_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_0_5_1_Entry.grid(row=8, column=1)

                        Number_of_Children_Aged_6_11_1_Label = customtkinter.CTkLabel(root, text="How Many children(0-5)")
                        Number_of_Children_Aged_6_11_1_Label.grid(row=9, column=0)
                        Number_of_Children_Aged_6_11_1_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_6_11_1_Entry.grid(row=9, column=1)


                        Room_2_Label = customtkinter.CTkLabel(root, text="Room No.2")
                        Room_2_Label.grid(row=6, column=1)

                        Number_of_Adults_2_Label = customtkinter.CTkLabel(root, text="Number of Adults(12 & Above")
                        Number_of_Adults_2_Label.grid(row=7, column=2)
                        Number_of_Adults_2_Entry = customtkinter.CTkEntry(root)
                        Number_of_Adults_2_Entry.grid(row=7, column=3)

                        Number_of_Children_Aged_0_5_2_Label = customtkinter.CTkLabel(root, text="How Many Children(0-5)")
                        Number_of_Children_Aged_0_5_2_Label.grid(row=8, column=2)
                        Number_of_Children_Aged_0_5_2_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_0_5_2_Entry.grid(row=8, column=3)

                        Number_of_Children_Aged_6_11_2_Label = customtkinter.CTkLabel(root, text="How many children(6-11")
                        Number_of_Children_Aged_6_11_2_Label.grid(row=9, column=2)
                        Number_of_Children_Aged_6_11_2_Entry = customtkinter.CTkEntry(root)
                        Number_of_Children_Aged_6_11_2_Entry.grid(row=9, column=3)
                        def Calculate_Result():
                            Name = Name_Entry.get()
                            Starting_Date = f"{Starting_Date_Month.get()}/{Starting_Date_Day.get()}/{Starting_Date_Year.get()}"
                            Ending_Date = f"{Ending_Date_Month.get()}/{Ending_Date_Day.get()}/{Ending_Date_Year.get()}"
                            Board = Board_ComboBox.get()

                            Number_of_Adults_1 = Number_of_Adults_2_Entry.get()
                            Number_of_Children_Aged_0_5_1 = (Number_of_Children_Aged_0_5_2_Entry.get())
                            Number_of_Children_Aged_6_11_1 = (Number_of_Children_Aged_6_11_2_Entry.get())

                            Number_of_Adults_2 = Number_of_Adults_Room_1_Entry.get()
                            Number_of_Children_Aged_0_5_2 = (Number_of_Children_Aged_0_5_2_Entry.get())
                            Number_of_Children_Aged_6_11_2 = (Number_of_Children_Aged_6_11_1_Entry.get())

                            try:
                                Number_of_Adults_1 = int(Number_of_Adults_1)
                                Number_of_Children_Aged_0_5_1 = int(Number_of_Children_Aged_0_5_1)
                                Number_of_Children_Aged_6_11_1 = int(Number_of_Children_Aged_6_11_1)

                                Number_of_Adults_2 = int(Number_of_Adults_2)
                                Number_of_Children_Aged_0_5_2 = int(Number_of_Children_Aged_0_5_2)
                                Number_of_Children_Aged_6_11_2 = int(Number_of_Children_Aged_6_11_2)


                            except ValueError:
                                Number_of_Adults_Room_1_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_1_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_1_Entry.configure(placeholder_text="Error")

                                Number_of_Adults_2_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_2_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_2_Entry.configure(placeholder_text="Error")

                            if int(Number_of_Adults_1 + Number_of_Children_Aged_0_5_1 + Number_of_Children_Aged_6_11_1 + Number_of_Adults_2 + Number_of_Children_Aged_0_5_2 + Number_of_Children_Aged_6_11_2) > 6 or int(Number_of_Adults_1 + Number_of_Children_Aged_0_5_1 + Number_of_Children_Aged_6_11_1 + Number_of_Adults_2 + Number_of_Children_Aged_0_5_2 + Number_of_Children_Aged_6_11_2) < 2:
                                Number_of_Adults_Room_1_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_1_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_1_Entry.configure(placeholder_text="Error")

                                Number_of_Adults_2_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_0_5_2_Entry.configure(placeholder_text="Error")
                                Number_of_Children_Aged_6_11_2_Entry.configure(placeholder_text="Error")

                            if Number_of_Children_Aged_0_5_1 == ():
                                Number_of_Children_Aged_0_5_1 = 0

                            elif Number_of_Children_Aged_6_11_1 == ():
                                Number_of_Children_Aged_6_11_1 = 0

                            if Number_of_Children_Aged_0_5_2 == ():
                                Number_of_Children_Aged_0_5_2 = 0

                            elif Number_of_Children_Aged_6_11_2 == ():
                                Number_of_Children_Aged_6_11_2= 0

                            NoA_Price_1 = Number_of_Adults_1 * 12000
                            NoC6_Price_1 = Number_of_Children_Aged_0_5_1 * 4000
                            NoA_Price_2 = Number_of_Adults_2 * 12000
                            NoC6_Price_2 = Number_of_Children_Aged_0_5_2 * 4000

                            match Number_of_Adults_1:
                                case 2:
                                    NoA_price_1 = 18000
                                case 3:
                                    NoA_price_1 = 23000
                                case 4:
                                    NoA_price_1= 27000
                            match Number_of_Adults_2:
                                case 2:
                                    NoA_price_2 = 18000
                                case 3:
                                    NoA_price_1 = 23000
                                case 4:
                                    NoA_price_1 = 27000

                            def final_step(val2):
                                if val2 == "Normal":
                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_Date} \n Ending Date:{Ending_Date} \n Board:{Board} \n Total Pax:{Number_of_Adults_1+Number_of_Adults_2+Number_of_Children_Aged_0_5_1+Number_of_Children_Aged_0_5_2+Number_of_Children_Aged_6_11_1+Number_of_Children_Aged_6_11_2} \n Total Expected Price:{(NoA_Price_1+NoC6_Price_1+NoC6_Price_2 + NoA_price_1+NoA_price_2+NoA_Price_2) + (Number_of_Adults_1 + Number_of_Adults_2 * 2000) + ((Number_of_Children_Aged_6_11_1+Number_of_Children_Aged_6_11_2)*1000)}")
                                    Result.grid(row=12, column=0)
                                if val2 == "BBQ":
                                    Result = customtkinter.CTkLabel(root, text=f"Booking Summary \n Full Name:{Name} \n Starting Date:{Starting_Date} \n Ending Date:{Ending_Date} \n Board:{Board} \n Total Pax:{Number_of_Adults_1 + Number_of_Adults_2 + Number_of_Children_Aged_0_5_1 + Number_of_Children_Aged_0_5_2 + Number_of_Children_Aged_6_11_1 + Number_of_Children_Aged_6_11_2} \n Total Expected Price:{(NoA_Price_1 + NoC6_Price_1 + NoC6_Price_2 + NoA_price_1 + NoA_price_2 + NoA_Price_2) + (Number_of_Adults_1 + Number_of_Adults_2 * 4000) + ((Number_of_Children_Aged_6_11_1 + Number_of_Children_Aged_6_11_2) * 2000)}")
                                    Result.grid(row=12, column=0)

                            Extra_Meal_Label = customtkinter.CTkLabel(root, text="Extra Meal Options")
                            Extra_Meal_Label.grid(row=11, column=0)

                            Extra_Meal_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "BBQ", "Normal"], command=final_step)
                            Extra_Meal_ComboBox.grid(row=11,column=1)

                        Next_Button = customtkinter.CTkButton(root, text='Next', command=Calculate_Result)
                        Next_Button.grid(row=10, column=0)
                Type_Room_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "Double Deluxe","Double Standard", "Deluxe-Standard"], comman=People)
                Type_Room_ComboBox.grid(row=6, column=0)
        Room_Number_ComboBox = customtkinter.CTkComboBox(root, values=["Select", "One", "Two", "Three", "Four"], command=type_rooms)
        Room_Number_ComboBox.grid(row=4, column=1)

#Getting the board and the type of room in the above function

Board_Label = customtkinter.CTkLabel(root, text="Select a Board")
Board_Label.grid(row=3, column=0)
Board_ComboBox = customtkinter.CTkComboBox(root, values=["Select","BB","HB","FB"], command=next_steps)
Board_ComboBox.grid(row=3, column=1)

#Selecting a Board

root.mainloop()

#Runs the frame while the program runs