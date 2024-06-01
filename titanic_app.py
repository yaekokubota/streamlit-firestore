import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from google.cloud import firestore
from google.oauth2 import service_account

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-firebase-ba9da")

df = sns.load_dataset('titanic')
st.subheader('データフレーム')
st.dataframe(df, height=150)
  
df["生存・死亡"]=df["survived"].map(lambda x:"生存" if x else "死亡")
df["性別"]=df["sex"].map(lambda x:"男性" if x else "女性")
classmap = {"First":"1等", "Second":"2等", "Third":"3等"}
df["客室"]=df["class"].map(lambda x:classmap[x])

st.subheader("生存者分析")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    sns.countplot(df, x="生存・死亡", hue="性別")
    ax.set_ylabel("人数")
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots()
    sns.countplot(df, x="生存・死亡", hue="客室")
    ax.set_ylabel("人数")
    st.pyplot(fig)

st.subheader("年齢分布")
fig, axes = plt.subplots(1,2, figsize=(12,4))
sns.histplot(df, x="age", ax=axes[0])
sns.histplot(df, x="age", ax=axes[1], hue="性別")
st.pyplot(fig)