from logging import error
import streamlit as st
import datetime
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
import psycopg2

import st_db_demo as ss


st.dataframe(ss.get_all_dogs())
st.dataframe(ss.get_dogs_by_name('Taikong'))