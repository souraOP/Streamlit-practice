import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('st.write example');
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