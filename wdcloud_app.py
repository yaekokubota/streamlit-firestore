import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from google.cloud import firestore
from google.oauth2 import service_account

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-firebase-ba9da")

text = st.text_area("何でも入力してください",
"""A faster way to build and share data apps. 
Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks.
It’s all Python, open-source, and free! 
And once you’ve created an app you can use our Community Cloud platform to deploy, manage, and share your app.""",
height=150)
wcloud = WordCloud().generate(text)
fig = plt.figure(figsize=(20,20))
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig)