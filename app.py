import streamlit as st
import tempfile
import os
import io
from search_engine import search_video

# --- Page Config ---
st.set_page_config(page_title="AI Video Search", page_icon="🔍")

st.title(" 🔍 Semantic Video Search Engine")
st.markdown("Use **Artificial Intelligence** to find specific events inside a video.")

# --- Sidebar for Settings ---
with st.sidebar:
    st.header("⚙️ Settings")
    # Feature 1: Confidence Threshold Slider
    confidence_threshold = st.slider("Minimum Confidence", 0.0, 1.0, 0.20, 0.01)
    st.info("Adjust this to filter out weak matches.")

# --- Main Interface ---

# 1. File Uploader
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

# 2. Text Input
query = st.text_input("Describe the scene you are looking for:", placeholder="e.g. A red car turning left")

# 3. Search Button
if st.button("Search Video", type="primary"):
    if uploaded_file is not None and query:
        
        # Save uploaded file to a temporary file on disk
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        
        with st.spinner('AI is watching the video... (This might take a moment)'):
            try:
                # Call the AI logic
                best_frame, timestamp, score = search_video(video_path, query)
                
                # --- Result Logic ---
                if score < confidence_threshold:
                    st.error(f"No good match found! (Best score: {round(score,2)}) - Try lowering the threshold.")
                else:
                    st.success(f"Match Found at {round(timestamp, 2)} seconds!")
                    st.metric(label="AI Confidence Score", value=f"{round(score * 100, 1)}%")

                    # Feature 2: Jump to Timestamp (Video Player)
                    st.write("### 🎥 Watch the Event")
                    st.video(video_path, start_time=int(timestamp))

                    # Feature 3: Download Proof
                    st.write("### 📸 Proof of Event")
                    st.image(best_frame, caption="Analyzed Frame", use_column_width=True)
                    
                    # Convert image to bytes for download
                    buf = io.BytesIO()
                    best_frame.save(buf, format="JPEG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="Download Frame",
                        data=byte_im,
                        file_name="evidence_frame.jpg",
                        mime="image/jpeg"
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
            
            finally:
                # Cleanup: Close file and remove temp file
                tfile.close()
                os.unlink(video_path)

    else:
        st.warning("Please upload a video and enter a text description.")