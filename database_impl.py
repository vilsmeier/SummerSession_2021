import psycopg2
import streamlit as st

def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

