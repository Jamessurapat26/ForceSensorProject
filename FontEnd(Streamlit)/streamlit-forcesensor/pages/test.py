import streamlit as st
import cv2
import numpy as np
from getApi import getApi
import datetime  # เพิ่มการนำเข้าโมดูล datetime


def create_foot_pressure_image():

    sensor_data = getApi()
    sensor_data = sensor_data[-1]

    l_foot = []
    r_foot = []

    l_foot.append(sensor_data['L1'])
    l_foot.append(sensor_data['L2'])
    l_foot.append(sensor_data['L3'])
    l_foot.append(sensor_data['L4'])
    l_foot.append(sensor_data['L5'])
    l_foot.append(0)
    l_foot.append(sensor_data['L6'])
    l_foot.append(sensor_data['L7'])
    l_foot.append(sensor_data['L8'])
    l_foot.append(sensor_data['L9'])
    l_foot.append(sensor_data['L10'])
    l_foot.append(0)
    l_foot.append(sensor_data['L11'])
    l_foot.append(sensor_data['L12'])
    l_foot.append(sensor_data['L13'])
    l_foot.append(sensor_data['L14'])
    l_foot.append(sensor_data['L15'])
    l_foot.append(sensor_data['L16'])

    r_foot.append(sensor_data['R1'])
    r_foot.append(sensor_data['R2'])
    r_foot.append(sensor_data['R3'])
    r_foot.append(0)
    r_foot.append(sensor_data['R4'])
    r_foot.append(sensor_data['R5'])
    r_foot.append(sensor_data['R6'])
    r_foot.append(sensor_data['R7'])
    r_foot.append(sensor_data['R8'])
    r_foot.append(0)
    r_foot.append(sensor_data['R9'])
    r_foot.append(sensor_data['R10'])
    r_foot.append(sensor_data['R11'])
    r_foot.append(sensor_data['R12'])
    r_foot.append(sensor_data['R13'])
    r_foot.append(sensor_data['R14'])
    r_foot.append(sensor_data['R15'])
    r_foot.append(sensor_data['R16'])


    reshaped_data_l = np.array(l_foot).reshape(6, 3)
    reshaped_data_r = np.array(r_foot).reshape(6, 3)
    # Create a black image
    img = np.zeros((600, 800, 3), dtype=np.uint8)
    
    # Define data
    left_foot = reshaped_data_l
    
    right_foot = reshaped_data_r
    
    # Function to get color based on value
    def get_color(value):
        if value == 0:
            return (0, 0, 0)
        elif value <= 2024:
            return (0, 255, int(255/2024 * value))
        else:
            green_value = int(255 - ((255 / 2024) * (value - 2024)))
            return (0, green_value, 255)
    
    # Function to draw foot data
    def draw_foot(data, start_x, start_y, title):
        cv2.putText(img, title, (start_x + 50, start_y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                x = start_x + j * 100
                y = start_y + i * 80
                color = get_color(value)
                cv2.rectangle(img, (x, y), (x + 90, y + 70), color, -1)  # Filled rectangle
                cv2.rectangle(img, (x, y), (x + 90, y + 70), (255, 255, 255), 1)  # White border
                if value != 0:
                    text_color = (0, 0, 0) if value <= 2024 else (255, 255, 255)
                    cv2.putText(img, str(value), (x + 10, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
    
    # Draw left and right foot data
    draw_foot(left_foot, 50, 50, "Left Foot")
    draw_foot(right_foot, 450, 50, "Right Foot")
    
    return img

# Streamlit app
st.title("Foot Pressure Visualization")

# Create the image
foot_pressure_img = create_foot_pressure_image()

# Convert BGR to RGB (OpenCV uses BGR, but Streamlit expects RGB)
foot_pressure_img_rgb = cv2.cvtColor(foot_pressure_img, cv2.COLOR_BGR2RGB)

# Display the image in Streamlit
st.image(foot_pressure_img_rgb, caption="Foot Pressure Data", use_column_width=True)

# Initialize session state for recommendations if it doesn't exist
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = []

# Add a text input field for recommendations
recommendation = st.text_input("Recommendation:", "Enter your recommendation here...")

# Add a button to save the recommendation
if st.button("Save Recommendation"):
    if recommendation != "Enter your recommendation here..." and recommendation.strip() != "":
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state['recommendations'].append((timestamp, recommendation))
        st.success("Recommendation saved successfully!")

# Display all saved recommendations
if 'recommendations' in st.session_state and st.session_state['recommendations']:
    st.write("Saved Recommendations:")
    for i, (timestamp, rec) in enumerate(st.session_state['recommendations'], 1):
        st.write(f"Record #{i} - {timestamp}: {rec}")
else:
    st.write("No recommendations saved yet.")