import psycopg2

def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

