from logging import error
import streamlit as st
import datetime
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
import psycopg2

# /Users/apple/Documents/GitHub/SummerSession_2021/st_db_demo.py

# Initialize connection.
# Uses st.cache to only run once.
# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def run_insert(insert):
    with conn.cursor() as cur:
        cur.execute(insert)




def get_all_dogs():
    rows = run_query("SELECT * from dogs;")
    dog_dict = {
        'id':rows[0],
        'name':rows[1],
        'resign':rows[2],
        'birthday':rows[3],
        'male':rows[4],
        'species':rows[5]
    }
    return df(dog_dict)

def get_dogs_by_name(name):
    dogs = get_all_dogs()
    return dogs[dogs['name']==name]

def resign_dogs(name,birthday,male,species):
    run_insert('''
        insert into dogs (name, resign, birthday, male, species) VALUES 
            ({},now(),{},{},{});
        '''.format(name,birthday,male,species))







