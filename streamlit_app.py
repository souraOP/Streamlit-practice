import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np
import altair as alt

st.title('SOURA STREAMLIT');
st.subheader("Example 1")

st.write("Hello _Niggas!_ :sunglasses:");

st.code('for i in range(8): foo()')

# Example 3
st.write(1234)
st.text("SOURASISH ")
#example 4
df = pd.DataFrame({
    'first column': [23, 34, 65, 23],
    'second column': [-34, -346, 23, 6]
})
st.write(df);

st.write("Above is a Dataframe:", df, "Below is a dataframe");

# Example 5

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
chart = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b','c']
)
st.write(df2)
st.write(chart)

st.title("St.slider example")
st.subheader("Slider");

age = st.slider("what is your age signora?", 0, 120, 20);
st.write("My age is ", age, "years old");

st.subheader("Range subheader");

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 50.0)
);

st.write('Values:', values);

st.subheader("Range-Time Slider");

my_pontu = st.slider(
    "Schedule when to meet pontu",
    value=(time(11, 30), time(12, 45))
)
st.write("Timing: ", my_pontu);

st.subheader("Datetime slider");

souraSlider = st.slider(
    "When do you start",
    value=datetime(2024, 1, 1, 9, 30),
    format="DD/MM/YY - hh:mm"
)

st.write("Which date?", souraSlider);


st.title("st.line_chart example");

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(chart_data);
st.line_chart(chart_data);

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)

st.title("st.select_box example");

options = st.selectbox(
    "What your fav nigga?",
    ('african', 'american', 'indian')
)
st.write("Your favourite nigga is: ", options);

