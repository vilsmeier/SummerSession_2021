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

st.set_page_config('betaGo') # web name
st.title("betaGo")
# define the account

user_name =''
user_pass =''
switch =0 # close


def test():
    # if switch !=1:
    #     return st.warning('no account')

    # st.write('here is test')

    # # 导入数据并显示出数据
    # st.text("the data list:")
    # df =pd.read_csv("position.csv")
    # st.table(df)


    # # 左侧栏列表
    # name_list =df["dog_name"].unique()
    # name_type =st.sidebar.selectbox(
    #     "name:",
    #     name_list
    # )

    # event_list =df["event_type"].unique()
    # event_type =st.sidebar.selectbox(
    #     "event:",
    #     event_list
    # )



    # part_df =df[(df['dog_name'] ==name_type) & (df['event_type'] ==event_type)]
    # print(part_df)
    # st.write(f"According to your selection, there is/are {len(part_df)} raws.")

    # 在图上标出点的位置，？？？如何更改样式
    # map_raw_1
    # st.map(part_df)
    # def map(data, lat, lon, zoom):
    #     st.write(pdk.Deck(
    #         map_style="mapbox://styles/mapbox/light-v9",
    #         initial_view_state={
    #             "latitude": lat,
    #             "longitude": lon,
    #             "zoom": zoom,
    #             "pitch": 50,
    #         },
    #         layers=[
    #             pdk.Layer(
    #                 "HexagonLayer",
    #                 data=data,
    #                 get_position=["lon", "lat"],
    #                 radius=100,
    #                 elevation_scale=4,
    #                 elevation_range=[0, 1000],
    #                 pickable=True,
    #                 extruded=True,
    #             ),
    #         ]
    #     ))
    # map()

    # add_selectbox =st.sidebar.selectbox(
    #     "How do youlike to be cntacted?",
    #     ("Email","Home phone","Mobile phone")
    # )

    # slider_val =0
    
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

    # form2 =st.form("my_form2")
    # form2.slider("Inside the form2")# 在form2里面合在一起
    # st.slider("form2")# 独立的一个项
    # # now add a submit button to the form
    # form2.form_submit_button("Submit")

    # ## 


    # agree = st.checkbox('hahaha')
    # if agree:
    #     st.write('gagaga')

    # st.write(add_selectbox)

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
        

    # if st.button('hi'):
    #     st.write('hi')
    # else:
    #     st.write('fuck you!')

    # ge =st.radio("piapiapia",('a','b','c'))

    # if ge=='a':
    #     st.write('gua')
    # elif ge=='b':
    #     st.write('pia')


    # va =st.slider("sasasasa", 0.0,100.0,(25.0,75.0))
    # st.write("it is",va)

    # color = st.select_slider(
    #     'Select a color of the rainbow',
    # options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    # st.write('My favorite color is', color)

    # number = st.number_input('Insert a number')
    # st.write('The current number is ', number)

    # txt = st.text_area('Text to analyze', '''
    #     I feel very sad because there is no hope for my future
    #     ''')
    # st.write('Sentiment:', (txt))

    # d = st.date_input(
    #     "When's your birthday",
    #     datetime.date(2019, 7, 6))
    # st.write('Your birthday is:', d)

    # t = st.time_input('Set an alarm for', datetime.time(8, 45))
    # st.write('Alarm is set for', t)

    # color = st.color_picker('Pick A Color', '#00f900')
    # st.write('The current color is', color)

pet_name ='gaga'
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

    st.dataframe(ss.get_all_dogs())
    st.dataframe(ss.get_dogs_by_name('Taikong'))



    st.write('here is data')
    ## -----------------------------------------
    ## daily part

    # ========= raw 0: user's info ================
    ## here you have to gain the image from your user about their dogs, also with the label
    ## if no, there is a default setting
    def daily():
        st.write('here is daily')
        img_def =Image.open('neko.jpeg')
        cap_def ='my dog'
        st.image(img_def,cap_def)
        them_color ='green'

        st.sidebar.subheader('time scale')
        data_timescale =st.sidebar.radio('',('today','longterm'))
        if data_timescale =='today':
            # ========= raw 1:pet report ==================



            # ========= raw 2:heart rate ==================
            st.subheader('heart rate')
            heart_rate =pd.read_csv('heart_daily_'+pet_name+'.csv')
            st.dataframe(heart_rate)

            opt = np.array(heart_rate['time']).tolist()

            raw2_1,raw2_2,raw_2_25,raw2_4,raw2_3 =st.beta_columns((1,1,2,1,1))
            # with raw2_1:
            #     date_start = st.date_input('start date',datetime.date(2019, 7, 6))
            with raw2_2:
                time_start = st.selectbox('start time', options=opt)
            with raw_2_25:
                st.image('lung.png')
            # with raw2_3:
            #     date_end = st.date_input('end date',datetime.date(2019, 7, 6))
            with raw2_4:
                time_end = st.selectbox('end time', options=opt)
            
            
            raw2_6,raw2_7 =st.beta_columns((1,1))
            with raw2_6:
                st.write("starting:",time_start)
            with raw2_7:
                st.write("ending:",time_end)

            #setting index as date
            # heart_rate['time'] = pd.to_datetime(heart_rate.time, unit='h',origin=pd.Timestamp(now))
            # heart_rate.index = heart_rate['time']
    
            heart_rate = heart_rate[time_start:time_end+1]
            st.dataframe(heart_rate)

            st.altair_chart(
                alt.Chart(heart_rate).mark_area(
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
            st.write('your dog is suuuuuuper great!')

            # ========= raw 3:breath rate ==================
            st.subheader('breath rate')


            # ========= raw 5: GPS =========================
            st.subheader('GPS')
            position =pd.read_csv('position'+'.csv')
            # st.dataframe(position)

            import pydeck as pdk

            st.map(position)

            # =========== raw 6: calorie =====================
            st.subheader('calorie')


            # =========== raw 7: pose =======================
            st.subheader('pose')
            raw7_1,raw7_2,raw7_3,raw7_4 =st.beta_columns((1,1,1,1))
            with raw7_1:
                sitting_num =2
                st.image(Image.open('sit.png'),f'sitting {sitting_num} times')

            with raw7_2:
                sleeping_time =4
                st.image(Image.open('sleep.png'),f'sitting {sleeping_time} hours')

            with raw7_3:
                standing_num =5
                st.image(Image.open('stand.png'),f'sitting {standing_num} times')

            with raw7_4:
                down_num =3
                st.image(Image.open('down.png'),f'sitting {down_num} times')

            # =========== raw 8: bark =======================
            st.subheader('bark')

        # ------------- long term --------------
        import plotly.figure_factory as ff
        heart_long =pd.read_csv('heart_longterm_'+pet_name+'.csv')
    daily()

# sign in


st.sidebar.subheader('Account')
sign_in =st.sidebar.radio('',('sign in','sign up'))
# sign_butt=False

# if st.sidebar.button('enter'):
#     sign_butt = True

if sign_in =='sign in':
    st.write('sign_in')
    acc =st.sidebar.text_input('Name')
    pw = st.sidebar.text_input('password')
    if len(acc) ==0:
        st.warning('input you account here')
        st.stop()
    if len(acc) != 0 and pw!='1':
        st.warning('Please input the right account or password!')
        st.stop()
    else:
        user_name =acc
        switch =1 # open
    st.success('welcome !')
elif sign_in =='sign up':
    acc =st.sidebar.text_input('Name ')
    pw = st.sidebar.text_input('password ')
    if len(acc) ==0:
        st.warning('creat you account here')
        st.stop()
    if len(acc) =='momoc':
        st.warning('This name already exists')
        st.stop()
    else:
        st.write('welcome!')
        user_name =acc
        user_pass =pw
        switch =1
        
    st.success('you have a new account now!')


CEO =st.selectbox('',options=['home','data','diary'])
if CEO =='diary':
    test()
elif CEO =='home':
    user()
elif CEO =='data':
    data()


