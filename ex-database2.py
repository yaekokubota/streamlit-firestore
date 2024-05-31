import seaborn as sns
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-firebase-ba9da")

import matplotlib.pyplot as plt
import pandas as pd

docs = db.collection('penguins').stream()
data =[]
for d in docs:
    data.append(d.to_dict())

species = st.sidebar.selectbox('species',["Adelie","Chinstrap","Gentoo"])

df = pd.DataFrame(data)
df = df[df['species'] == species].reset_index(drop=True)
st.write(df)
st.scatter_chart(df, x='bill_length_mm', y='body_mass_g')