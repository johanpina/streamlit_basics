import streamlit as st

st.title("Hello World!👋")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text in Streamlit")

st.markdown("This is a markdown")
st.success("This is a success message!")
st.info("This is a info message!")
st.warning("This is a warning message!")
st.error("This is a error message!")
st.exception("This is a exception message!")

st.help(range)

st.write("This is a write function")
st.write(range(10))
st.write("This is a write function", range(10))
st.write("This is a write function", range(10), 2.5, {"key": "value"})

st.markdown("---")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")
st.markdown("---")

## Elementos interativos

st.checkbox("Checkbox")
st.radio("Radio", options=["Option 1", "Option 2"])
st.selectbox("Selectbox", options=["Option 1", "Option 2"])
st.multiselect("Multiselect", options=["Option 1", "Option 2"])
st.slider("Slider", min_value=0, max_value=10)
st.select_slider("Select Slider", options=["Option 1", "Option 2"])
st.text_input("Text Input")
st.number_input("Number Input")
st.text_area("Text Area")
st.date_input("Date Input")
st.time_input("Time Input")
st.file_uploader("File Uploader")
st.color_picker("Color Picker")

## Containers

st.markdown("---")
st.markdown("# Containers")
st.markdown("---")

st.markdown("## Columns")
col1, col2 = st.columns(2)
col1.markdown("Column 1")
col2.markdown("Column 2")

st.markdown("## Expander")
expander = st.expander("Expander")
expander.markdown("This is a expander")

st.markdown("## Tabs")
tabs = st.tabs("Tabs")

## Plots

st.markdown("---")
st.markdown("# Plots")
st.markdown("---")

st.markdown("## Line Chart")
st.line_chart({"data": [1, 2, 3, 4, 5]})
st.markdown("## Area Chart")
st.area_chart({"data": [1, 2, 3, 4, 5]})
st.markdown("## Bar Chart")
st.bar_chart({"data": [1, 2, 3, 4, 5]})

import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'