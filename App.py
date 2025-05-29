import streamlit as st

st.header("PowerHouse River Resort", divider="green")
st.write("Enter the following information")

Name_Entry = st.text_input("Name:")
Starting_Date = st.date_input("Starting Date:")
Ending_Date = st.date_input("Ending Date:")
Board = st.write("Select a Board")

def BB_Func():
        if "Select_a_Board" not in st.session_state:
            st.session_state.Select_a_Board = False
        if  st.button("BB"):
            st.session_state.Select_a_Board = not st.session_state.Select_a_Board
        if st.session_state.Select_a_Board:
            st.write("Amount of Rooms")
            if "Amount_of_Rooms" not in st.session_state:
                st.session_state.Amount_of_Rooms = False
            if st.button("One"):
                st.session_state.Amount_of_Rooms = not st.session_state.Amount_of_Rooms
            if st.session_state.Amount_of_Rooms:
                st.write("Type of Room")
                if "Type_of_Room" not in st.session_state:
                    st.session_state.Type_of_Room = False
                if st.button("Deluxe"):
                    st.session_state.Type_of_Room = not st.session_state.Type_of_Room
                if st.session_state.Type_of_Room:

                    st.write("Enter the amount of Pax")
                    Number_of_Adults = (st.text_input("Amount of Adults(12&above)"))
                    Number_of_Children_0_5 = (st.text_input("Amount of Children(0-5)"))
                    Number_of_Children_6_11 = (st.text_input("Amount 0f Children(6-11)"))

                    if "TAG" not in st.session_state:
                        st.session_state.TAG = False
                    if st.button("Next"):
                        st.session_state.TAG = not st.session_state.TAG
                    if st.session_state.TAG:
                        if not Name_Entry:
                            st.error("Please enter the name to continue")
                        if Ending_Date < Starting_Date:
                            st.error("The Ending Date cannot be set before the starting date")
                        if Starting_Date > Ending_Date:
                            st.error("The Starting Date cannot be greater than the ending date")
                        if Starting_Date == Ending_Date:
                            st.error("Both Dates cannot be in the same day")
                        try:
                            Number_of_Adults = int(Number_of_Adults)
                            Number_of_Children_0_5 = int(Number_of_Children_0_5)
                            Number_of_Children_6_11 = int(Number_of_Children_6_11)
                        except ValueError or int(Number_of_Adults+Number_of_Children_0_5+Number_of_Children_6_11) > 3:
                             st.error("The amount of people cannot go passed 3 people / Please enter an integer")
                        if Number_of_Adults == ():
                            st.error("There should be an integer")
                        if Number_of_Adults < 2:
                            st.error("It should not be less than 2 pax")
                        if Number_of_Children_0_5 == ():
                            Number_of_Children_0_5 = 0
                        if Number_of_Children_6_11 == ():
                            Number_of_Children_6_11 = 0
                        Number_of_Adults_Guest_Price = Number_of_Adults * 12000
                        Number_of_Children_6_11_Guest_Price = Number_of_Children_6_11 * 4000

                        match Number_of_Adults:
                            case 2:
                                Number_of_Adults_Room_Price = 20000
                            case 3:
                                Number_of_Adults_Room_Price = 26000
                            case _:
                                st.error("Error")

                        st.write("BBQ / Normal")

                        if "FOOD" not in st.session_state:
                            st.session_state.FOOD = False
                        if st.button("BBQ"):
                            st.session_state.FOOD = not st.session_state.FOOD
                        if st.session_state.FOOD:
                            st.header("Booking Summary")
                            st.write(f"Name:{Name_Entry}")
                            st.write(f"Starting Date:{Starting_Date}")
                            st.write(f"Ending Date:{Ending_Date}")
                            st.write(f"Board{Board}")
                            st.write("Amount of rooms:One")
                            st.write("Type of Room: Deluxe")
                            st.write(f"Amount of People:{Number_of_Adults+Number_of_Children_0_5+Number_of_Children_6_11}")
                            st.write(f"Total Price:{Number_of_Adults_Room_Price+Number_of_Children_6_11_Guest_Price+Number_of_Adults_Guest_Price+(Number_of_Adults*4000)+(Number_of_Children_6_11*2000)}")

BB_Func()
