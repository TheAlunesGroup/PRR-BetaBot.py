import streamlit as st
from PIL import Image
st.set_page_config(page_title = "PowerHouse River Resort", page_icon = "Logo.png")

image = Image.open("PowerHouse_River_Resort.jpg")

st.image(image, width=300)
st.header("PowerHouse River Resort", divider="green")
st.write("")
with st.form("Booking Registration"):
    st.subheader("Basic Registration")
    Name_Entry = st.text_input("Name:")
    Starting_Date = st.date_input("Check-in Date:")
    Ending_Date = st.date_input("Check-out Date:")
    Board_Select_Box = st.selectbox("Choose a Meal Plan", ["BB", "HB", "FB"])
    Amount_of_Rooms_Select_Box = st.number_input("Amount of Rooms", min_value=1, max_value=4)
    if Amount_of_Rooms_Select_Box == 1:
        Type_of_Room_1 = st.selectbox("Type of Room", ["Deluxe", "Standard"])
        st.subheader("Amount of Pax")
        if Type_of_Room_1 == "Deluxe":
            Number_of_Adults_1 = st.number_input("Adults(Aged 12 & Above)", min_value=2, max_value=3)
            Number_of_Children_0_5_1 = st.number_input("Children(Aged 0-5)", min_value=0, max_value=1)
            Number_of_Children_6_11_1 = st.number_input("Children(Aged 6-11)", min_value=0, max_value=1)
        elif Type_of_Room_1 == "Standard":
            Number_of_Adults_1 = st.number_input("Adults(Aged 12 & Above)", min_value=2, max_value=4)
            Number_of_Children_0_5_1 = st.number_input("Children(Aged 0-5)", min_value=0, max_value=2)
            Number_of_Children_6_11_1 = st.number_input("Children(Aged 6-11)", min_value=0, max_value=2)
        BN = st.selectbox("Extra Meal Options", ["BBQ", "Normal"])

    Submit = st.form_submit_button("Get Summary")
    
    if Submit:
        count = 0
        if Board_Select_Box == "BB":
           if Type_of_Room_1 == "Deluxe":
               if Board_Select_Box == "BB":
                   if Amount_of_Rooms_Select_Box == 1:
                       Number_of_Adults_1_Price = (20000 if Number_of_Adults_1 == 2 else 260000)
                       Number_of_Children_6_11_1_Price = (Number_of_Children_6_11_1 * 4000)
                       error = False
                       if Type_of_Room_1 == "Deluxe":
                           if Name_Entry == "":
                               st.markdown("<span style='color: red;'>Please Enter a Name to Continue .</span>",unsafe_allow_html=True)
                               error = True
                           if Starting_Date == Ending_Date:
                               st.markdown("<span style='color: red;'>Please Change the Date for it to not be the same.</span>",unsafe_allow_html=True)
                               error = True
                           if Starting_Date > Ending_Date:
                               st.markdown("<span style='color: red;'>The Starting Date can't be greater than the ending date.</span>",unsafe_allow_html=True)
                               error = True
                           elif error is not True:
                               if BN == "BBQ":
                                    if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 20000
                                        Number_of_Children_6_11_1_Price = Number_of_Children_6_11_1 * 4000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + Number_of_Children_6_11_1_Price + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 26000
                                        Number_of_Children_6_11_1_Price = Number_of_Children_6_11_1 * 4000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + Number_of_Children_6_11_1_Price + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 20000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_0_5_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + (Number_of_Adults_1 * 4000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 26000
                                        Number_of_Children_6_11_1_Price = Number_of_Children_6_11_1 * 4000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_0_5_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + (Number_of_Adults_1 * 4000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 2 and Number_of_Children_6_11_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 20000
                                        Number_of_Children_6_11_1_Price = Number_of_Children_6_11_1 * 4000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_6_11_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + Number_of_Children_6_11_1_Price + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 3 and Number_of_Children_6_11_1 == 1:
                                        count = 1
                                        Number_of_Adults_1_Price = 26000
                                        Number_of_Children_6_11_1_Price = Number_of_Children_6_11_1 * 4000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1 + Number_of_Children_6_11_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + Number_of_Children_6_11_1_Price + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000)}</strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                                        count = 0
                                        Number_of_Adults_1_Price = 20000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + (Number_of_Adults_1 * 4000)} </strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
                                    elif Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                                        count = 0
                                        Number_of_Adults_1_Price = 26000
                                        st.markdown(f'<div style="background:linear-gradient(135deg,#f9fafb,#eef2f7);border-left:6px solid #4a90e2;padding:1.2rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);font-family:\'Segoe UI\',sans-serif;margin-top:1rem;"><h3 style=\'margin:0 0 0.5rem 0;color:#2c3e50;font-size:1.25rem;\'>Booking Summary</h3><p style=\'margin:0;font-size:1rem;line-height:1.5;color:#34495e;\'>Name: <strong>{Name_Entry}</strong><br>Check-in Date: <strong>{Starting_Date}</strong><br>Check-out Date: <strong>{Ending_Date}</strong><br>Meal Plan: <strong>{Board_Select_Box}</strong><br>Amount of Rooms: <strong> 1 </strong> <br> Type of Room: <strong>Deluxe</strong><br>Amount of People: <strong>{Number_of_Adults_1}</strong><br>Total Price: <strong>{Number_of_Adults_1_Price + (Number_of_Adults_1 * 4000)} </strong></p></div>',unsafe_allow_html=True)
                                        st.write("")
st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© Powerhouse River Resort.")
