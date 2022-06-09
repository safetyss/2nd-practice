import streamlit as st

import datetime 

from PIL import Image
from PIL import Image
Img = Image.open("TrackExpense.jpg")
st.image(Img, width=700)

Img2 = Image.open("Money.jpg")
st.sidebar.image(Img2, width=300)


st.title("MY EXPENSE TRACKER")

st.header("Get a grip on your income and manage your finances better!!!")

year = st.sidebar.selectbox('Year', range(2021, 2040))

month = st.sidebar.selectbox('Month', range(1,13))



st.subheader("Income Category")

income = st.number_input('Enter your monthly income (NGN): ')
additional = st.number_input('Enter any additional income (NGN): ')

total_income = income + additional
st.write("Great! Your total income next month will be (NGN)" + str(total_income))



st.subheader('Expenditure Category')

def expense_category():
    housing = st.number_input('Housing (NGN): ')
    electricity = st.number_input('Electricity (NGN): ')
    water = st.number_input('Water (NGN): ')
    food = st.number_input('Food (NGN): ')
    fuelling = st.number_input('Fuelling (NGN): ')
    groceries= st.number_input('Groceries (NGN): ')
    transportation = st.number_input('Transportation (NGN): ')
    airtime = st.number_input('Airtime/Data (NGN): ')
    health = st.number_input('Health (NGN): ')
    clothing = st.number_input('Clothing (NGN): ')
    others = st.number_input('Others (NGN): ')
    total_expenses = housing + electricity + water + food + fuelling + groceries + transportation + airtime + health + clothing + others
    return total_expenses

expense_total = expense_category()
if(st.button('Calculate Total Expenses')):
    st.write("Your total expenses next month will be (NGN)" + str(expense_total))

difference = total_income - expense_total
if difference>= 0:
    st.success("Your total surplus next month will be (NGN)" + str(difference))
else:
    st.warning("Check your spending habit!! You are running a deficit of (NGN)" + str(difference))
        
        
st.write("Thank you for using this tool")







hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
