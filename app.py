# Streamlit Sales Analysis Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv('SampleSuperstore.csv', encoding='latin1')
df = df.dropna().drop_duplicates()

# Handling negative or unrealistic values
sales_array = np.array(df['Sales'])
quantity_array = np.array(df['Quantity'])

# Replace negative sales (if any) with mean sales
mean_sales = np.mean(sales_array[sales_array > 0])
sales_array = np.where(sales_array < 0, mean_sales, sales_array)
df['Sales'] = sales_array

# Add calculated columns using NumPy
profit_array = np.array(df['Profit'])

#Profit Margin Calculation
df['Profit Margin (%)'] = np.round((profit_array / sales_array) * 100, 2)

num_cols = ['Sales', 'Quantity', 'Discount', 'Profit', 'Profit Margin (%)']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

# -----------------------------
# 2. Streamlit App Layout
# -----------------------------
st.set_page_config(page_title='Sales Analysis Dashboard', layout='wide')
st.header('Sales Analysis Dashboard', divider='rainbow')

# Sidebar filters
st.sidebar.header('Filters')
regions = st.sidebar.multiselect('Select Regions', df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect('Select Categories', df['Category'].unique(), default=df['Category'].unique())
segments = st.sidebar.multiselect('Select Segments', df['Segment'].unique(), default=df['Segment'].unique())

# Filter dataset
filtered_df = df[(df['Region'].isin(regions)) & (df['Category'].isin(categories)) & (df['Segment'].isin(segments))]

# -----------------------------
# 3. Display Metrics
# -----------------------------
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
avg_sales = filtered_df['Sales'].mean()
avg_profit = filtered_df['Profit'].mean()
total_quantity = filtered_df['Quantity'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Sales', f'${total_sales:,.2f}')
col2.metric('Total Profit', f'${total_profit:,.2f}')
col3.metric('Average Sale', f'${avg_sales:,.2f}')
col4.metric('Average Profit', f'${avg_profit:,.2f}')

st.subheader('Filtered Dataset')
st.dataframe(filtered_df)

# -----------------------------
# 4. Visualizations
# -----------------------------

# -----------------------------
# Sales by Region - Bar Plot
# -----------------------------
st.subheader('Sales by Region')
region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots()
sns.barplot(x=region_sales.index, y=region_sales.values, palette='viridis', ax=ax1)
ax1.set_xlabel('Region')
ax1.set_ylabel('Sales')
st.pyplot(fig1)

# -----------------------------
# Sales by Category - Pie Chart
# -----------------------------
st.subheader('Sales Distribution by Category')
category_sales = filtered_df.groupby('Category')['Sales'].sum()
fig2, ax2 = plt.subplots()
ax2.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
st.pyplot(fig2)

# -----------------------------
# Quantity Sold per Sub-Category - Horizontal Bar Plot
# -----------------------------
st.subheader('Quantity Sold per Sub-Category')
subcat_quantity = filtered_df.groupby('Sub-Category')['Quantity'].sum().sort_values()
fig3, ax3 = plt.subplots()
sns.barplot(x=subcat_quantity.values, y=subcat_quantity.index, palette='coolwarm', ax=ax3)
st.pyplot(fig3)

# -----------------------------
# Sales vs Profit - Scatter Plot
# -----------------------------
st.subheader('Sales vs Profit by Category')
fig4, ax4 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Sales', y='Profit', hue='Category', palette='Set2', alpha=0.7, ax=ax4)
st.pyplot(fig4)

# -----------------------------
# Profit Distribution by Category - Box Plot
# -----------------------------
st.subheader('Profit Distribution by Category')
fig5, ax5 = plt.subplots()
sns.boxplot(data=filtered_df, x='Category', y='Profit', palette='Set3', ax=ax5)
st.pyplot(fig5)

# -----------------------------
# Correlation Heatmap
# -----------------------------
st.subheader('Correlation Heatmap of Numerical Features')
fig6, ax6 = plt.subplots(figsize=(8,6))
sns.heatmap(filtered_df[num_cols].corr(), annot=True, cmap='YlGnBu', fmt='.2f', ax=ax6)
st.pyplot(fig6)

# -----------------------------
# Pair Plot
# -----------------------------
st.subheader('Pair Plot of Sales, Profit, Quantity by Category')
sns.set(style='ticks')
fig7 = sns.pairplot(filtered_df[['Sales', 'Profit', 'Quantity', 'Category']], hue='Category', palette='Set2')
st.pyplot(fig7.fig)

# -----------------------------
# Count Plot of Ship Mode
# -----------------------------
st.subheader('Count of Orders by Ship Mode')
fig8, ax8 = plt.subplots(figsize=(7,5))
sns.countplot(data=filtered_df, x='Ship Mode', palette='pastel', ax=ax8)
st.pyplot(fig8)

# -----------------------------
# Stacked Bar Plot - Sales by Region and Category
# -----------------------------
st.subheader('Stacked Bar: Sales by Region and Category')
sales_region_category = filtered_df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')
fig9, ax9 = plt.subplots(figsize=(10,6))
sales_region_category.plot(kind='bar', stacked=True, colormap='Accent', ax=ax9)
st.pyplot(fig9)

# -----------------------------
# Histogram of Profit Margin
# -----------------------------
st.subheader('Histogram of Profit Margin (%)')
fig10, ax10 = plt.subplots(figsize=(8,5))
ax10.hist(filtered_df['Profit Margin (%)'], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig10)