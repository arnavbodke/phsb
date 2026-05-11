import streamlit as st
import os
from video_processor import process_video

# Create folders if not exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

st.set_page_config(
    page_title="RAD",
    layout="wide"
)

st.title("Road Anomaly Detection")


uploaded_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_file is not None:

    input_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    output_path = os.path.join(
        "outputs",
        f"processed_{uploaded_file.name}"
    )

    # Save uploaded video
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())


    if st.button("Run Detection"):

        with st.spinner("Processing Video"):

            process_video(input_path, output_path)

        st.success("Detection Complete")



        with open(output_path, "rb") as file:

            st.download_button(
                label="Download Marked Video",
                data=file,
                file_name=f"Marked-{uploaded_file.name}",
                mime="video/mp4"
            )