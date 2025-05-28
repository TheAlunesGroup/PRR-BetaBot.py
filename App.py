import streamlit as st

st.header("PowerHouse River Resort", divider="green")
st.write("Enter the following information")


Name = st.text_input("Name:")
Starting_Date = st.date_input("Starting Date:")
Ending_Date = st.date_input("Ending Date:")
Board = st.write("Board")

Board_Choice = st.radio("Choose the board", ["BB", 'HB', 'FB'], horizontal=True)

Amount_of_Rooms = st.radio("Amount of Rooms", ["One Room", 'Two Rooms', 'Three Rooms', "Four Rooms"], horizontal=True)

Type_of_Room = st.radio("Type of Room", ["Deluxe", "Standard"], horizontal=True)

Number_of_Adults = (st.text_input("Amount of Adults(12&above)"))
Number_of_Children_0_5 = (st.text_input("Amount of Children(0-5)"))
Number_of_Children_6_11 = (st.text_input("Amount 0f Children(6-11)"))




