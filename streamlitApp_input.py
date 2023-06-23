import streamlit as st
import cv2
import pickle
import os
import tensorflow as tf

new_model = tf.keras.models.load_model('saved_model/main_bilstm_model')


st.set_page_config(page_title="SafetyNet", page_icon=":camera:", layout="wide")

def read_video(video_path):
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame, channels='RGB')

with st.container():
    st.title("SafetyNet")
    st.subheader("A Threat Detection System using Artificial Neural Networks")
    st.write("Law enforcement officials struggle to assess the intentions of individuals during patrols, leading to misinterpretation of actions and numerous loss of innocent lives. This project aims to develop an AI-based pose detection model that segregates potential threats from harmless civilian actions using CNN+LSTM model. By leveraging AI and ML, we aim to enhance safety and prevent loss of life.")
    st.write("[GitHub](https://github.com/ananyaraju)")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("CCTV/BodyCam Footage Input")
        st.write("Input video:")
        video_file = st.file_uploader("Upload a video", type=["mp4", "avi"])
        if video_file is not None:
            st.video(video_file)
        else:
            st.write("No video files found in the selected folder.")
    with right_column:
        st.header("Output")
        st.write("Result:")
        
