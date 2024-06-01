import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('streamlit-firestore/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

import seaborn as sns

df = sns.load_dataset('titanic')
for index, row in df.iterrows():
    db.collection('titanic').add(row.to_dict())
    