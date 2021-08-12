from logging import error
import streamlit as st
import datetime
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
import psycopg2

import DogService as ss

'''
streamlit run /Users/apple/Documents/GitHub/SummerSession_2021/st_show.py
'''


st.dataframe(ss.get_all_dogs())
st.dataframe(ss.get_dogs_by_name('Taikong'))

dog_name =  st.text_input('search the dog:')
dog_info = ss.get_dogs_by_name(dog_name)

st.dataframe(dog_info)


if dog_name=='':
    st.write('please enter the dog name!')
elif len(dog_info)==0:
    st.write('dog not found!')
else:
    sel = st.selectbox('You have selected {}! Please select the info you wonder:'.format(dog_name),['birthday','gender','species'])
    st.write(dog_info[sel])



resign_flag = st.sidebar.checkbox('Resign a dog!')
commit_flag = False
cancel_flag = False

print('resign_flag is: ',resign_flag)
print('Commit_flag is: ',commit_flag)


if resign_flag and commit_flag==False:
    name = st.text_input('Dog\'s name:')
    birthday = st.date_input('Birthday:')
    gender = 'true' if st.selectbox('Gender:',['Male','Female'])=='Male' else 'false'
    species = st.text_input('Dog\'s species:')
    if name != '' and species != '':
        commit_flag = st.button('Commit!') 
    
    if commit_flag:
        ss.resign_dogs(name,birthday,gender,species)
        resign_flag = False
        commit_flag = False

hr = ss.get_heart_rate(1).set_index(['time'])
st.dataframe(hr)
st.line_chart(hr['heart_rate'])

