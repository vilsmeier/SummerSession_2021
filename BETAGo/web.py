from typing import ChainMap, Optional
from altair.vegalite.v4.api import value
from altair.vegalite.v4.schema.channels import Longitude, Opacity, YValue
from altair.vegalite.v4.schema.core import Gradient, GradientStop
from ipywidgets.widgets import widget
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
import plotly.graph_objects as go

import  DogService as ss
 



# D:\temp\betaGo>streamlit run web.py
icon = Image.open("logo.png")
st.set_page_config(layout='wide', page_title='betaGo',page_icon= icon,
                    # primaryColor="#F63366"
                     # backgroundColor="#FFFFFF"
                    # secondaryBackgroundColor="#F0F2F6"
                    # textColor="#262730"
                    # font="sans serif"
                    ) # web name
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
        with row0_2:
            dog_n =st.selectbox('  ',ss.get_all_dogs()['name'])
            st.write(ss.get_dog_id_by_name(dog_n).values)
            st.image(ss.get_photo(ss.get_dog_id_by_name(dog_n).values[0])[0], use_column_width =True, caption ='my photo')

            st.write('there should be a place to shift the photo that has been uploaded')
        with row0_3:
            st.write('''
            ### **Introduction**
            ''')
        with row0_3:
            st.write('there should be some thing you want to show about yourself')
        with row0_3:
            st.dataframe(ss.get_all_dogs())
            st.write('you have :'+len(ss.get_all_dogs())+'dogs')
        



def data():
    if switch !=1:
        return st.warning('no account')
    them_color ='green'

    @st.cache(allow_output_mutation =True)
    def fetch_data(pet_name):
        heart_rate =pd.read_csv('heart_daily_'+pet_name+'.csv')
        return heart_rate

    # @st.cache(ttl=300)
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
        null_10_0,row11_1,row13_3,null14_4 =st.beta_columns((0.1,2.5,1,0.1))
        null_30_0,row31_1,row33_3,null34_4 =st.beta_columns((0.1,2.5,1,0.1))
        # row11_1,row13_3 =st.beta_columns((1,0.5))
        with row1_1:
            heart_check =st.checkbox('heart rate')
            st.image('heart.png', caption='heart rate is '+heart+' beat/min',width =100)
            if heart_check:
                with row11_1:
                    # df = fetch_data('gaga')
                    df_sh = ss.get_heart_rate(2)
                    # st.dataframe(df_s)
                    st.altair_chart(
                            alt.Chart(df_sh,
                                height =200
                                ).mark_area(
                                line ={'color':'#C84B05'},
                                color =alt.Gradient(
                                    gradient ='linear',
                                    stops =[alt.GradientStop(color ='white',offset =0.2), # color could be changed with theme
                                            alt.GradientStop(color ='#C84B05', offset =1)],
                                            x1=1,x2=1,y1=1,y2=0
                                )
                                ).encode(
                            alt.X('time', type='quantitative',title='hour of day'),
                            alt.Y('heart_rate', type='quantitative', title='heart beat',scale =alt.Scale(domain=[min(df_sh['heart_rate'])-1,max(df_sh['heart_rate'])+1]))),
                            use_container_width= True 
                        )
                with row13_3:
                    st.write('''
                    ### illustration:
                    ''')
                    st.write('''
                     some description about dog's heart health condition, and a button to illustrate the criterion
                    ''')
                    st.write(
                            """
                            ### [🐕](https://sustech.edu.cn)
                            """) 

        with row1_3:
            breath_check =st.checkbox('respiration')
            st.image('lung.png', caption='respiration rate is '+respiration+' times/min',width =100)
            if breath_check:
                with row31_1:
                    df_sb = fetch_data('gaga')
                    st.altair_chart(
                            alt.Chart(df_sb,
                            height =200
                            # ,width = 100.0
                            ).mark_area(
                                line ={'color':'#C84B05'},
                                color =alt.Gradient(
                                    gradient ='linear',
                                    stops =[alt.GradientStop(color ='white',offset =0.2), # color could be changed with theme
                                            alt.GradientStop(color ='#C84B05', offset =1)],
                                            x1=1,x2=1,y1=1,y2=0
                                )
                                ).encode(
                            alt.X('time', type='quantitative',title='hour of day'),
                            alt.Y('data', type='quantitative', title='breath beat',scale =alt.Scale(domain=[min(df_sb['data'])-1,max(df_sb['data'])+1]))),
                            use_container_width= True
                            
                        )
                with row33_3:
                    st.write('''
                    ### illustration:
                    ''')
                    st.write('''
                     some description about dog's breath health condition, and a button to illustrate the criterion
                    ''')
                    st.write("""
                    ### [🐕](https://sustech.edu.cn) """)

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
            st.write('''
                    ###### [learn more about dog's pose](https://www.baidu.com)
            ''')
        with row2_6:
            step_df =pd.DataFrame([step],columns=['step'])
            st.bar_chart(step_df,width= 10, use_container_width= True)


    def long_term(pic,gender,mood_index,heart_rate,breath_rate,pose):
        row0_2,row0_4,row0_6 =st.beta_columns((0.01,0.02,0.01))
        with row0_4:
            get_name2 =st.selectbox('NAME',options=ss.get_all_dogs()['name'])
        with row0_2:
            if len(get_name2) !=0:
                st.image(pic,use_column_width =True, caption ='my photo')     
        with row0_6:
            if gender ==1:
                st.image('male.png', use_column_width =True)
            if gender ==0:
                st.image('female.png',use_column_width =True)

        # ================row 1======================
        st.write('-------')
        st.write('''
        * ## **mood index**
        ''')
        fig, ax = plt.subplots()
        ax.hist(mood_index, bins=20)
        st.pyplot(fig)
        # ================row 2======================
        st.write('----------')
        st.write('''* ## **Health data**''')
        select_heart_breath =st.selectbox(' ',options=['heart rate','respiration'])
        if select_heart_breath =='heart rate':
            df_l =heart_rate
            fig1 =go.Figure()
            fig1.add_trace(go.Scatter(x =df_l['date'], y =df_l['data'],
                            name ='Heart rate', opacity =0.7,
                            line =dict(color =them_color,width =2)))
            fig1.add_vrect(x0 =str(df_l['date'][0]),x1 =str(df_l['date'][len(df_l['date'])-1]),
                            line_width =0, fillcolor =them_color, opacity =0.2, annotation_text =get_name2,
                            annotation_position ='inside top left',
                            annotation =dict(font_size =14,font_family ="Comic Sans MS"))
            fig1.update_xaxes(
                rangeselector_activecolor="#EBD2B9",
                rangeslider_visible=True
            )
            fig1.update_layout(
                xaxis_title ='date',
                yaxis_title ='heart rate',
                height =600
            )
            st.plotly_chart(fig1)
        elif select_heart_breath =='respiration':
            df_lb =breath_rate
            fig2 =go.Figure()
            fig2.add_trace(go.Scatter(x =df_lb['date'], y =df_lb['data'],
                            name ='respiration rate', opacity =0.7,
                            line =dict(color =them_color,width =2)))
            fig2.add_vrect(x0 =str(df_lb['date'][0]),x1 =str(df_lb['date'][len(df_lb['date'])-1]),
                            line_width =0, fillcolor =them_color, opacity =0.2, annotation_text =get_name2,
                            annotation_position ='inside top left',
                            annotation =dict(font_size =14,font_family ="Comic Sans MS"))
            fig2.update_xaxes(
                rangeselector_activecolor="#EBD2B9",
                rangeslider_visible=True
            )
            fig2.update_layout(
                xaxis_title ='date',
                yaxis_title ='breath rate',
                height =600
            )
            st.plotly_chart(fig2)  
        # ===============row 3===============
        st.write('-----------')
        st.write('''
                * ## **Activity**
                ''')
        df_lb =pd.read_csv('heart_longterm_gaga.csv')
        fig3 =go.Figure()
        fig3.add_trace(go.Scatter(x =df_lb['date'], y =df_lb['data'],
                        name ='respiration rate', opacity =0.7,
                        line =dict(color =them_color,width =2)))
        fig3.add_vrect(x0 =str(df_lb['date'][0]),x1 =str(df_lb['date'][len(df_lb['date'])-1]),
                        line_width =0, fillcolor =them_color, opacity =0.2, annotation_text =get_name2,
                        annotation_position ='inside top left',
                        annotation =dict(font_size =14,font_family ="Comic Sans MS"))
        fig3.update_xaxes(
            rangeselector_activecolor="#EBD2B9",
            rangeslider_visible=True
        )
        fig3.update_layout(
            xaxis_title ='date',
            yaxis_title ='breath rate',
            height =600
        )
        st.plotly_chart(fig3) 

        # ================row 4==================
        st.write('--------------')
        st.write('''
                * ## **pose**
                ''')

        row4_1,row4_2 =st.beta_columns((1,1))
        with row4_1:
            labels = ['down', 'lay', 'stand', 'sit', 'others']
            sizes = [15, 30, 40, 10,5]
            explode = [0, 0, 0, 0, 0]  # only "explode" the 2nd slice (i.e. 'Hogs')
            explode[sizes.index(max(sizes))] =0.1

            fig4, ax4 = plt.subplots()
            ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig4)
        with row4_2:
            st.write('''
                    your dog likes
                    ''')
            st.write('''
                    # {}
                    '''.format(labels[sizes.index(max(sizes))]))
            st.write('most')
            
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
            gender =0, # male
            mood_index =np.random.normal(1, 1, size=100),
            heart_rate =pd.read_csv('heart_longterm_gaga.csv'),
            breath_rate =pd.read_csv('heart_longterm_gaga.csv'),
            pose =pd.DataFrame(data ={'labels': ['down', 'lay', 'stand', 'sit', 'others'],'sizes': [15, 30, 40, 10,5]})
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





