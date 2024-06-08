import streamlit as st
from google.cloud import firestore

from google.oauth2 import service_account
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-firebase-ba9da")

title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

if title and url and submit:
    doc_ref = db.collection('posts').document(title)
    doc_ref.set({
        "title":title,
        "url":url
    })
    
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
    post = doc.to_dict()
    title = post["title"]
    url = post["url"]

    st.subheader(f'Post:{title}')
    st.write(f':link: [{url}]({url})')
