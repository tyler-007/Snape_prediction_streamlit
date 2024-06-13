import streamlit as st
import pandas as pd
import numpy as np
from model_predict import *
import streamlit as st
import pandas as pd
'''
# Read the CSV file
data = pd.read_csv("/Users/aayushjain/codes/projects/company assignements/Snape/City Heatmap/model/demand.csv")

# Extract the last 24 rows of data
data = data.tail(24)

# Select the 'y' column
data = data['y']
st.title('Expected requests across day')
# Display the line chart
st.line_chart(data)
st.title("Predicted Requests in the next hour")

'''
regions = predicted_values
cols = st.columns(len(regions))


# Iterate over regions and create buttons and text
for i, (region, value) in enumerate(regions.items()):
    with cols[i]:
        st.button(str(value), key=f"btn_{region}")
        st.write(region)