from logging import error
import streamlit as st
import datetime
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
import psycopg2

# streamlit run /Users/apple/Documents/GitHub/SummerSession_2021/DogService.py

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

def execute_sql(insert):
    with conn.cursor() as cur:
        cur.execute(insert)
        conn.commit()


def get_all_dogs():
    dog_entries = run_query("SELECT * from dogs;")
    # print(rows[0])

    id_list = []
    name_list = []
    resign_list = []
    birthday_list = []
    gender_list = []
    species_list = []

    for r in dog_entries:
        id_list.append(r[0])
        name_list.append(r[1])
        resign_list.append(r[2])
        birthday_list.append(r[3])
        gender_list.append('male' if r[4]==1 else 'female')
        species_list.append(r[5])

    dog_dict = {
        'id':id_list,
        'name':name_list,
        'resign':resign_list,
        'birthday':birthday_list,
        'gender':gender_list,
        'species':species_list
    }
    return df(dog_dict).set_index(['id'])

def get_dogs_by_name(name):
    dogs = get_all_dogs()
    return dogs[dogs['name']==name]

def resign_dogs(name,birthday,male,species):
    x = '''
        insert into dogs (name, resign, birthday, male, species) VALUES 
            (\'{}\',now(),\'{}\',{},\'{}\');
        '''.format(name,birthday,male,species)
    execute_sql(x)
    print(x)
    print('done!')

def delete_dogs(name):
    execute_sql('''
        delete from dogs where name=\'{}\';
    '''.format(name))


if __name__ == '__main__':
    print(get_all_dogs())
    resign_dogs('Gammago','2017-4-9','false','Hashiqi')
    print('execute!')







