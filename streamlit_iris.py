import streamlit as st
import pandas as pd
from google.cloud import firestore
import seaborn as sns

db = firestore.Client.from_service_account_json('serviceAccountKey.json')
docs = db.collection('iris').stream()
data =[]
for d in docs:
    data.append(d.to_dict())

species = st.sidebar.selectbox('species',["setosa","versicolor","virginica"])
df = pd.DataFrame(data)
df = df[df['species'] == species].reset_index(drop=True)
st.write(df)
st.scatter_chart(df, x='sepal_length', y='sepal_width')
