import pickle
import streamlit as st
import pandas as pd
from PIL import Image

pd = pd.read_csv('Salary_Data.csv')

model = pickle.load(open('Salary.sav', 'rb'))

def run():

    img = Image.open('logo 1.png')
    # img = img.resize((1000,1000))
    st.image(img)
    st.title('Salary Prediction')
    st.text('by Muhammad Raihan Fadilah (201351086)')
    
run()



check_data = st.checkbox("Lihat Simpel Data")
if check_data:
    st.write(pd[1:6])

years = st.number_input('years of experience')


predict = ''

if st.button('Calculate Salary'):
    predict = model.predict([[years]]
    )
    st.write ('The Estimated Salary (USD) : ', predict)
    st.write ('Perkiraan Gaji (IDR) :', predict*15000)

