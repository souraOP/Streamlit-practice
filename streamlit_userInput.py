import streamlit as st
import pandas as pd
from st_chat_message import message

st.set_page_config(
     layout='wide',
     page_title="Soura Day1",
     page_icon="💦",
);

st.title("st.multiselect")

options = st.multiselect(
     'What are you favourite colour',
     ['Green', 'Blue', 'Black', 'Violet'],
     ['Blue', 'Black'])


st.write('You selected this:', options)

st.title("st.checkbox example");

st.text("What would you like to order?");

icecream = st.checkbox("Ice Cream");
paneer = st.checkbox("Paneer");
chicken = st.checkbox("Chicken");

if icecream:
    st.write("Great! take some more 🍨");

if paneer:
    st.write("Take some paneer nigga");

if chicken:
    st.write("Here's some chicken 🍗");


message("Hello Pontu!", is_user=True)
message("Hi Ponti How are you ?")
message("io sono bene, come stai?", is_user=True)

st.title("latex example");

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

st.title("st.file_upload");
st.subheader("Input CSV File");

uploaded_file = st.file_uploader("Choose a file");

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file);
    st.text("Dataframe");
    st.write(df);
    st.text("Descriptive statistics");
    st.write(df.describe());
else:
    st.info("👆🏻 Upload a CSV File");

st.title("Streamlit Layout by soura");

with st.expander("About this app"):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Inputs');
userName = st.sidebar.text_input("What is your name?");
userEmoji = st.sidebar.selectbox("Select your favourite emoji", ['', '😾', '🙌🏻', '💋' ,'👯‍♀️', '🫳🏻']);
userFood = st.sidebar.selectbox("Select your favourite food", ['', 'biryani', 'burger', 'pizza', 'meifoon', 'pontu']);

st.header('Output');

col1, col2, col3 = st.columns(3);

with col1:
    if userName != '':
        st.write(f"Hello {userName}! 🙏🏼");
    else:
        st.write("Please enter your **name** !");

with col2:
  if userEmoji != '':
    st.write(f'{userEmoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if userFood != '':
    st.write(f'🍴 **{userFood}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')




