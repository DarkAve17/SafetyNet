import streamlit as st
import cv2

st.set_page_config(page_title="TDS", page_icon=":camera:", layout="wide")

with st.container():
    st.title("Threat Detection")
    st.subheader("Team 4")
    st.write("Law enforcement officials struggle to assess the intentions of individuals during patrols, leading to misinterpretation of actions and numerous loss of innocent lives. This project aims to develop an AI-based pose detection model that segregates potential threats from harmless civilian actions using CNN+LSTM model. By leveraging AI and ML, we aim to enhance safety and prevent loss of life.")
    st.write("[GitHub](https://github.com/ananyaraju)")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Instructions")
        st.write("1. Click on 'Run' checkbox to start streaming livefeed to ML API")
        st.write("2. The ML API analyses the video in 5 second duration videos")
        st.write("3. Get an analysis on the threat level of the livestreamed video")
    with right_column:
        st.header("Live camera feed")
        run = st.checkbox("Run")
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            while run:
                _, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                FRAME_WINDOW.image(frame)
            else:
                st.write("Click the box to start livefeed")
        else:
            st.write("Cannot open camera. Please retry.")
