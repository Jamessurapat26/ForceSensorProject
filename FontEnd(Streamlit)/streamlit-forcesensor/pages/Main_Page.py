import streamlit as st
import random
import string
from getApi import getApi
from chart import chart
import numpy as np

# เพิ่มส่วนของโปรไฟล์
st.title("User Profile")

# Initialize session state for profile
if 'profile' not in st.session_state:
    st.session_state.profile = {
        'name': '',
        'age': 0,
        'gender': ''
    }

# สร้าง columns สำหรับข้อมูลโปรไฟล์
st.session_state.profile['name'] = st.text_input("Name", st.session_state.profile['name'])
st.session_state.profile['age'] = st.number_input("Age", min_value=0, max_value=120, value=st.session_state.profile['age'])
st.session_state.profile['gender'] = st.selectbox("Gender", ['', 'Male', 'Female', 'Other'], index=0 if not st.session_state.profile['gender'] else ['', 'Male', 'Female', 'Other'].index(st.session_state.profile['gender']))

# ปุ่มบันทึกโปรไฟล์
if st.button("Save Profile"):
    st.success("Profile saved successfully!")
    st.write("Profile Information:")
    st.write(f"Name: {st.session_state.profile['name']}")
    st.write(f"Age: {st.session_state.profile['age']}")
    st.write(f"Gender: {st.session_state.profile['gender']}")

st.divider()  # เพิ่มเส้นแบ่งระหว่างส่วนโปรไฟล์และส่วนอื่นๆ

# โค้ดเดิมทั้งหมด
if 'count' not in st.session_state:
    st.session_state.count = 0

def add_new_row():
    st.text_input("Please input something",key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

if st.button("Add Note"):
    st.session_state.count += 1
    add_new_row()
    if st.session_state.count>1:
        for i in range(st.session_state.count-1):
            add_new_row()

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

col1, col2 = st.columns(2)

with col1:
    st.header("Left Foot")
    st.write(reshaped_data_l)

with col2:
    st.header("Right Foot")
    st.write(reshaped_data_r)

chart()