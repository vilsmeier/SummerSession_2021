from typing import ChainMap, Optional
from altair.vegalite.v4.api import value
from altair.vegalite.v4.schema.channels import Longitude
from altair.vegalite.v4.schema.core import Gradient, GradientStop
from pandas.core.tools.datetimes import Scalar
import streamlit as st 
import numpy as np 
import pandas as pd
from streamlit.proto.Button_pb2 import Button 
import datetime
import altair as alt
import matplotlib.pyplot as plt 
from PIL import Image
from streamlit.type_util import is_pandas_version_less_than

import  DogService as ss
 



# D:\temp\betaGo>streamlit run web.py
icon = Image.open("logo.png")
st.set_page_config(layout='wide', page_title='betaGo',page_icon= icon) # web name
st.sidebar.title("betaGo")
st.sidebar.write('-------')
# define the account

user_name =''
user_pass =''
switch =0 # close


def test():
    with st.form("mood"):
        st.write("How is your dog today")
        mood_score =st.slider("Score for activity")
        workout =st.checkbox("Did you work out today")

        # Every form must have a submit button.
        submitted1 =st.form_submit_button("Submit")
        if submitted1:
            st.write("mood:",mood_score,", work out:",workout)
    # st.write("Outside the form")
    # st.write(slider_val)

    with st.form("food"):
        st.write("How is your dog's diet today")
        food_score =st.slider("Score for appetite")

        # Every form must have a submit button.
        submitted2 =st.form_submit_button("Submit")
        if submitted2:
            st.write("mood:",food_score)

    with st.form('recording'): 
        record = st.text_area('what\'s interesting today')
        submitted3 =st.form_submit_button("Submit")
        if submitted3:
            st.write("remembered")

    with st.form('picture'):
        file =st.file_uploader("today's moment")
        if file is not None:
            st.image(file)
        submitted4 =st.form_submit_button("Submit")
        if submitted4:
            st.write("submited")

age =9
now ='2021-7-31'
ini_lat = 22
ini_lon = 114

def user():
    if switch !=1:
        return st.warning('no account')

    st.sidebar.write('refrash')
    # if switch ==2:
        # pet_name =

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
        picture =st.file_uploader("photo")
        if name != '' and species != '':
            commit_flag = st.button('Commit!') 
        
        if commit_flag:
            ss.resign_dogs(name,birthday,gender,species,picture)
            resign_flag = False
            commit_flag = False

    search_dog =st.sidebar


    user_info =st.sidebar.checkbox('check my imformation')
    if user_info:
        st.title(user_name)
        null0_1,row0_2,null0_2,row0_3,null0_3 =st.beta_columns((0.23,5,0.3,5,0.17))
        row0_2.image(Image.open("neko.jpeg"), use_column_width =True, caption ='my photo')
        with row0_2:
            st.write('there should be a place to shift the photo that has been uploaded')
        with row0_3:
            st.write('''
            ### **Introduction**
            ''')
        with row0_3:
            st.write('there should be some thing you want to show about yourself')
        with row0_3:
            st.dataframe(ss.get_all_dogs())
            st.write(len(ss.get_all_dogs()))

    def my_dog(name, pic, health):
        null1_1,row1_2,null1_3,row1_4,null1_5,row1_6,null1_7 =st.beta_columns((0.1,4,0.2,4,0.2,5,0.1))
        with row1_2:
            st.write(name)
        # with row1_4:



def data():
    if switch !=1:
        return st.warning('no account')


    ## -----------------------------------------
    ## daily part

    # ========= raw 0: user's info ================
    # here you have to gain the image from your user about their dogs, also with the label
    # if no, there is a default setting
    # st.write('here is daily')
    # img_def =Image.open('neko.jpeg')
    # cap_def ='my dog'
    # st.image(img_def,cap_def)
    them_color ='green'


        # st.subheader('heart rate')
        # heart_rate =pd.read_csv('heart_daily_'+pet_name+'.csv')
        # st.dataframe(heart_rate)

        # opt = np.array(heart_rate['time']).tolist()

        # raw2_1,raw2_2,raw_2_25,raw2_4,raw2_3 =st.beta_columns((1,1,2,1,1))
        # # with raw2_1:
        # #     date_start = st.date_input('start date',datetime.date(2019, 7, 6))
        # with raw2_2:
    #         time_start = st.selectbox('start time', options=opt)
    #     with raw_2_25:
    #         st.image('lung.png')
    #     # with raw2_3:
    #     #     date_end = st.date_input('end date',datetime.date(2019, 7, 6))
    #     with raw2_4:
    #         time_end = st.selectbox('end time', options=opt)
        
        
    #     raw2_6,raw2_7 =st.beta_columns((1,1))
    #     with raw2_6:
    #         st.write("starting:",time_start)
    #     with raw2_7:
    #         st.write("ending:",time_end)

    #     #setting index as date
    #     # heart_rate['time'] = pd.to_datetime(heart_rate.time, unit='h',origin=pd.Timestamp(now))
    #     # heart_rate.index = heart_rate['time']

    #     heart_rate = heart_rate[time_start:time_end+1]
    #     st.dataframe(heart_rate)

    #     st.altair_chart(
    #         alt.Chart(heart_rate).mark_area(
    #             line ={'color':them_color},
    #             color =alt.Gradient(
    #                 gradient ='linear',
    #                 stops =[alt.GradientStop(color ='white',offset =0.2), # color could be changed with theme
    #                         alt.GradientStop(color =them_color, offset =1)],
    #                         x1=1,x2=1,y1=1,y2=0
    #             )
    #             ).encode(
    #         alt.X('time', type='quantitative',title='hour of day'),
    #         alt.Y('data', type='quantitative', title='heart beat')),
            
    #     )
    #     st.write('your dog is suuuuuuper great!')

    #     # ========= raw 3:breath rate ==================
    #     st.subheader('breath rate')


    #     # ========= raw 5: GPS =========================
    #     st.subheader('GPS')
    #     position =pd.read_csv('position'+'.csv')
    #     # st.dataframe(position)

    #     import pydeck as pdk

    #     st.map(position)

    #     # =========== raw 6: calorie =====================
    #     st.subheader('calorie')


    #     # =========== raw 7: pose =======================
    #     st.subheader('pose')
    #     raw7_1,raw7_2,raw7_3,raw7_4 =st.beta_columns((1,1,1,1))
    #     with raw7_1:
    #         sitting_num =2
    #         st.image(Image.open('sit.png'),f'sitting {sitting_num} times')

    #     with raw7_2:
    #         sleeping_time =4
    #         st.image(Image.open('sleep.png'),f'sitting {sleeping_time} hours')

    #     with raw7_3:
    #         standing_num =5
    #         st.image(Image.open('stand.png'),f'sitting {standing_num} times')

    #     with raw7_4:
    #         down_num =3
    #         st.image(Image.open('down.png'),f'sitting {down_num} times')

    #     # =========== raw 8: bark =======================
    #     st.subheader('bark')

    # # ------------- long term --------------
    # import plotly.figure_factory as ff
    # heart_long =pd.read_csv('heart_longterm_'+pet_name+'.csv')

    @st.cache(allow_output_mutation =True)
    def fetch_data(pet_name):
        heart_rate =pd.read_csv('heart_daily_'+pet_name+'.csv')
        return heart_rate

    def present(pic,mood,heart,respiration,temp,pose,step):
        # ====================row 0====================
        row0_2,row0_4,row0_6 =st.beta_columns((0.01,0.02,0.01))
        with row0_4:
            get_name =st.selectbox('NAME',options=ss.get_all_dogs()['name'])
        with row0_2:
            if len(get_name) !=0:
                st.image(pic,use_column_width =True, caption ='my photo')
        ## birthday
        # with row0_4:
        #     if len(get_name) ==0:
        #         st.write('''
        #         choose your dog please
        #         ''')
        #     else:
        #         # birth_d =datetime.datetime.strptime(ss.get_dogs_by_name(get_name)['birthday'],'%Y-%m-%d')
        #         # st.write(ss.get_dogs_by_name(get_name)['birthday'])
        #         # st.write(type(pd.DataFrame(ss.get_dogs_by_name(get_name))['birthday']))
        #         st.write('''
        #         your dog is **\'{}** years old
        #         '''.format((ss.get_dogs_by_name(get_name))['birthday'])
        ##         )
        with row0_6:
            st.image(mood, use_column_width =True, caption ='mood')

        null0,row0,null1 =st.beta_columns((0.5,1,0.5))
        # row0.write('====================================')
        st.write('-------')
        st.success('hearth data')
        
        # =====================row 1===================
        row1_1,null1_2,row1_3 =st.beta_columns((1,0.5,1))
        null_10_0,row11_1,row13_3,null14_4 =st.beta_columns((0.01,1,0.5,0.01))
        # row11_1,row13_3 =st.beta_columns((1,0.5))
        with row1_1:
            heart_check =st.checkbox('heart rate')
            st.image('heart.png',use_column_width= 1, caption='heart rate is '+heart+' bit/min')
            if heart_check:
                with row11_1:
                    # st.dataframe(heart_rate)
                    st.altair_chart(
                        alt.Chart(fetch_data('gaga')).mark_area(# name shoule be get_name
                            line ={'color':them_color},
                            color =alt.Gradient(
                                gradient ='linear',
                                stops =[alt.GradientStop(color ='white',offset =0.2), # color could be changed with theme
                                        alt.GradientStop(color =them_color, offset =1)],
                                        x1=1,x2=1,y1=1,y2=0
                            )
                            ).encode(
                        alt.X('time', type='quantitative',title='hour of day'),
                        alt.Y('data', type='quantitative', title='heart beat')),
                        
                    )
                with row13_3:
                    st.write('''
                    ### illustration:
                    ''')
                    st.write('''
                     some description about dog's heart health condition, and a button to illustrate the criterion
                    ''')
                    st.write("""
                    #### **Learn more**
                    [!['link']('\\icon.png')](https://baidu.com)
                    """)

        with row1_3:
            heart_check =st.checkbox('respiration')
            st.image('lung.png', caption='respiration rate is '+respiration+' times/min')

        st.write('-------')
        st.success('activity')
        # ====================row 2====================
        row2_2,row2_4,null2_5,row2_6,null2_7 =st.beta_columns((0.1,0.2,0.05,0.1,0.01))
        with row2_2:
            # fig,ax =plt.subplot()
            temp_df =pd.DataFrame([temp],columns=['temp'])
            st.bar_chart(temp_df,width= 10, use_container_width= True)
            # st.pyplot(plt.bar(x ='temperature', height =temp))
        with row2_4:
            pose_sr =['down.png','sit.png','sleep.png','stand.png']
            pose_intro =['downward','sitting','sleeping','standing']
            st.write('my doy is \'{} now'.format(pose_intro[pose]))
            st.image(pose_sr[pose],use_column_width= True)
        with row2_6:
            step_df =pd.DataFrame([step],columns=['step'])
            st.bar_chart(step_df,width= 10, use_container_width= True)

    def long_term(pic,gender,mood_index):
        row0_2,row0_4,row0_6 =st.beta_columns((0.01,0.02,0.01))
        with row0_4:
            get_name =st.selectbox('NAME',options=ss.get_all_dogs()['name'])
        with row0_2:
            if len(get_name) !=0:
                st.image(pic,use_column_width =True, caption ='my photo')     
        with row0_6:
            if gender ==1:
                st.image('male.png', use_column_width =True)
            if gender ==0:
                st.image('female.png',use_column_width =True)

        # ================row 1======================
        st.write('''
        * mood index
        ''')
        fig, ax = plt.subplots()
        ax.hist(mood_index, bins=20)
        st.pyplot(fig)



    # sidebar
    st.sidebar.subheader('time scale')
    data_timescale =st.sidebar.radio('',('today','longterm'))
    if data_timescale =='today':
        present(
            pic ='neko.jpeg',
            mood ='neko.jpeg', 
            heart ='90',
            respiration ='16',
            temp = 33,
            pose =2,
            step =23
            )
    if data_timescale =='longterm':
        long_term(
            pic ='neko.jpeg',
            gender =1, # male
            mood_index =np.random.normal(1, 1, size=100)
        )







# sign in


st.sidebar.subheader('Account')
sign_in =st.sidebar.radio('',('sign in','sign up'))
# sign_butt=False

# if st.sidebar.button('enter'):
#     sign_butt = True

if sign_in =='sign in':
    # st.write('sign_in')
    acc =st.sidebar.text_input('Name')
    pw = st.sidebar.text_input('password')
    if len(acc) ==0:
        st.warning('input you account on the side bar')
        st.stop()
    if len(acc) != 0 and pw!='1':
        st.warning('Please input the right account or password!')
        st.stop()
    else:
        user_name =acc
        switch =1 # open
    # st.success('welcome !')
elif sign_in =='sign up':
    acc =st.sidebar.text_input('Name ')
    pw = st.sidebar.text_input('password ')
    if len(acc) ==0:
        st.warning('creat you account on the side bar')
        st.stop()
    if len(acc) =='momoc':
        st.warning('This name already exists')
        st.stop()
    else:
        st.write('welcome!')
        user_name =acc
        user_pass =pw
        switch =1

    # st.success('you have a new account now!')
st.sidebar.write('-------')

CEO =st.selectbox('',options=['home','data','diary'])
if CEO =='diary':
    test()
elif CEO =='home':
    user()
elif CEO =='data':
    data()


