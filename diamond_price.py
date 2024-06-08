import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing

df = sns.load_dataset('diamonds')
st.dataframe(df)

st.header('ダイアモンドの価格予想')

le = preprocessing.LabelEncoder()
df['cut_no'] = le.fit_transform(df['cut'])
cut_names = le.classes_
df['col_no'] = le.fit_transform(df['color'])
col_names = le.classes_

st.dataframe(df, height=200)
df2 = df.drop(columns=['cut', 'color','clarity'], axis=1)
st.write(df2)
st.write(df2.corr())
ax = df2.plot.scatter(x='carat', y='price')
st.pyplot(ax.figure)
carat = st.slider('carat', 0.5, 2.0)
cut = st.radio('cut',df['cut'].unique(), index=0, horizontal=True)
color = st.radio('color', df['color'].unique(), index=0, horizontal=True)

clf = linear_model.LinearRegression()
clf.fit(df[['carat', 'cut_no', 'col_no']], df['price'])

cut_val = np.where(cut_names == cut)[0]
col_val = np.where(col_names == color)[0]

price = clf.predict(pd.DataFrame([[carat, cut_val, col_val]], columns=['carat','cut_no','col_no']))

st.subheader(f'予想価格は{price[0]:.2f}ドルです')
