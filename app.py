import streamlit as st
import cv2
import matplotlib.pyplot as plt
from Analyzer import analyze

st.set_page_config(layout="wide")
st.title("📌 Posture Analyzer")

option = st.selectbox(
    "Choose a sample video:",
    ["None", "Sample1.mp4", "Sample2.mp4"]
)

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])
input_path = None

# Logic to determine input source
if option != "None":
    input_path = option
elif uploaded_file is not None:
    # Save uploaded file to disk
    with open("input.mp4", "wb") as f:
        f.write(uploaded_file.read())
    input_path = "input.mp4"

if input_path:
    st.success(f"Processing: {input_path}")

    col1, col2 = st.columns(2)

    frame_placeholder = col1.empty()
    plot_placeholder = col2.empty()

    stop = st.button("🛑 STOP")

    # Analyze the video
    for frame, lx, ly, rx, ry in analyze(input_path):
        if stop:
            st.warning("Stopped.")
            break

        # Update Frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB", caption="Analyzed Frame")

        # Update Plot
        fig, ax = plt.subplots()
        ax.plot(lx, ly, 'r-', label="Left Knee")
        ax.plot(rx, ry, 'b-', label="Right Knee")
        ax.legend()
        ax.set_title("Knee Movement")
        
        plot_placeholder.pyplot(fig)
        plt.close(fig)