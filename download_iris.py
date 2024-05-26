from google.cloud import firestore
db = firestore.Client.from_service_account_json('streamlit-firestore/serviceAccountKey.json')
docs = db.collection('iris').stream()
for d in docs:
    print(d.to_dict())
    
# import seaborn as sns
# df = sns.load_dataset('iris')
# print(df)
