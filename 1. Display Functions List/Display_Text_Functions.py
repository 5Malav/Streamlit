import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#--------- Title & Headers ----------

st.title("Student Performance Dashboard")

st.header("Analyze the data and visualize results")

st.write("This is the mini Streamlit Appliacation")

st.markdown("----")

#---------- Side bar inputs-----------

st.sidebar.header("User input section:- ")

name = st.sidebar.text_input("Enter the Name:- ")

age = st.sidebar.number_input("Enter Age:- ",10,60,18)

score_slider = st.sidebar.slider("Select Score Range:- ",0,100,(30,90))

grade_choice = st.sidebar.selectbox("Select Class Grade :- ",["A","B","C","D"])

st.write (f"Hello {name}, Age {age} , Selected Grade {grade_choice}")


# Sample data

data = {
    "Name": ['Malav','Maya','Mrugesh'],
    "Machine Learning": [88,77,90],
    "Natural Laguage Processing" : [92,70,85]
}
df = pd.DataFrame(data)

st.subheader("Student Data Table")
st.dataframe(df)
st.table(df.head())


# Charts

st.subheader(" Performance Charts")

st.line_chart(df.set_index('Name'))

st.bar_chart(df.set_index('Name'))

# Matplotlib Example

fig,ax = plt.subplots()
ax.plot(df['Name'],df['Machine Learning'],marker='o')
ax.set_title("Machine Learning Score")
st.pyplot(fig)

# Media
st.subheader("📷 Sample Media Display")
st.image("https://via.placeholder.com/300", caption="Sample Image")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# Layout Example

col1,col2 = st.columns(2)
with col1:
    st.write("Left Column Content")
with col2:
    st.write("Right Column Content")

tab1,tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.write("Content inside tab1")
with tab2:
    st.write("Content inside tab2")
    
st.markdown("***")
st.write("My First Mini App... ")