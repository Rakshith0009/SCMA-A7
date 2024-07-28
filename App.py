import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'Exercise', 'Water Intake (L)', 'Sleep (hours)'])

# Page title
st.title('Health and Fitness Tracker')

# Input fields
date = st.date_input('Date', datetime.today())
exercise = st.text_input('Exercise (e.g., running, cycling, etc.)')
water_intake = st.number_input('Water Intake (liters)', min_value=0.0, step=0.1)
sleep_hours = st.number_input('Sleep (hours)', min_value=0.0, step=0.1)

# Submit button
if st.button('Add Entry'):
    new_entry = pd.DataFrame({
        'Date': [date],
        'Exercise': [exercise],
        'Water Intake (L)': [water_intake],
        'Sleep (hours)': [sleep_hours]
    })
    st.session_state['data'] = pd.concat([st.session_state['data'], new_entry], ignore_index=True)

# Display data
st.subheader('Logged Entries')
st.write(st.session_state['data'])

# Statistics
st.subheader('Statistics')
if not st.session_state['data'].empty:
    avg_water_intake = st.session_state['data']['Water Intake (L)'].mean()
    avg_sleep_hours = st.session_state['data']['Sleep (hours)'].mean()
    st.write(f'Average Water Intake: {avg_water_intake:.2f} liters/day')
    st.write(f'Average Sleep: {avg_sleep_hours:.2f} hours/night')
else:
    st.write('No data to display statistics.')

# Export data
st.subheader('Export Data')
if st.button('Export to CSV'):
    st.session_state['data'].to_csv('health_fitness_data.csv', index=False)
    st.success('Data exported successfully!')

# Footer
st.write('Made with ❤️ using Streamlit')
