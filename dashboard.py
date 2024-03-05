# Import semua library yang dibutuhkan
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pandas as pd
import streamlit as st

Q1 = pd.read_csv("./data/Q1ok.csv")
Q2 = pd.read_csv("./data/Q2ok.csv")

st.title("DASHBOARD PENJUALAN DAN REVIEW SCORE PRODUK")

st.subheader("BAR PLOT BANYAK PENJUALAN PRODUK")
# Mendefinisikan top5 sebagai data yang mengandung 5 produk dengan penjualan terbaik
top5 = Q1.groupby(by="product_category_name").count().sort_values(by="order_item_id",ascending=False).head(5)
# Mendefinisikan bot5 sebagai data yang mengandung 5 produk dengan penjualan terburuk
bot5 = Q1.groupby(by="product_category_name").count().sort_values(by="order_item_id",ascending=True).head(5)

# Membuat kanvas kosong dengan object berupa fig dan ax
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# Mendefinisikan palet warna yang akan digunakan
colorstop = ["#99BD98", "#F2ECEC", "#F2ECEC", "#F2ECEC", "#F2ECEC"]
colorsbot = ["#BF3A02", "#F2ECEC", "#F2ECEC", "#F2ECEC", "#F2ECEC"]

# Membuat bar plot untuk produk dengan penjualan terbaik
sns.barplot(x="order_item_id", y="product_category_name", data=top5, palette=colorstop, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk dengan Penjualan Terbaik", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

# Membuat bar plot untuk produk dengan penjualan terburuk
sns.barplot(x="order_item_id", y="product_category_name", data=bot5, palette=colorsbot, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk dengan Penjualan Terburuk", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

# Memberikan judul pada visualisasi data
plt.suptitle("Produk dengan Penjualan Terbaik dan Terburuk", fontsize=20)

# Streamlit part
# Display the plots in the Streamlit app
st.pyplot(fig)

st.subheader("BAR PLOT REVIEW SCORE PRODUK")

# Mendefinisikan rs1 sebagai data yang mengandung 5 produk dengan review score 1 terbanyak
rs1 = Q2.groupby(by=["product_category_name", "review_score"]).count().loc[(slice(None), 1), :].sort_values(by="order_id",ascending=False).head(5)
# Mendefinisikan rs1 sebagai data yang mengandung 5 produk dengan review score 5 terbanyak
rs5 = Q2.groupby(by=["product_category_name", "review_score"]).count().loc[(slice(None), 5), :].sort_values(by="order_id",ascending=False).head(5)
# Membuat kanvas kosong dengan object berupa fig dan ax
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# Mendefinisikan palet warna yang akan digunakan
colors1 = ["#F22B35", "#F2ECEC", "#F2ECEC", "#F2ECEC", "#F2ECEC"]
colors5 = ["#7AC003", "#F2ECEC", "#F2ECEC", "#F2ECEC", "#F2ECEC"]

# Membuat bar plot untuk produk dengan review score 1 terbanyak
sns.barplot(x="order_id", y="product_category_name", data=rs1, palette=colors1, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk dengan Review Score 1 Terbanyak", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

# Membuat bar plot untuk produk dengan review score 5 terbanyak
sns.barplot(x="order_id", y="product_category_name", data=rs5, palette=colors5, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk dengan Review Score 5 Terbanyak", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

# Memberikan judul pada visualisasi data
plt.suptitle("Produk dengan Review Score 1 dan 5 Terbanyak", fontsize=20)

# Streamlit part
# Display the plots in the Streamlit app
st.pyplot(fig)