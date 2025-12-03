import streamlit as st
from sentence_transformers import SentenceTransformer, util
from processor import extract_frames

# @st.cache_resource tells Streamlit: "Load this ONCE and keep it in memory."
# This makes your app super fast after the first load.
@st.cache_resource
def load_model():
    return SentenceTransformer('clip-ViT-B-32')

# Load the model immediately
model = load_model()

def search_video(video_path, text_query):
    # 1. Break video into images
    frames, timestamps = extract_frames(video_path)
    
    # 2. Convert Text Query to Vector
    text_emb = model.encode(text_query)
    
    # 3. Convert Video Frames to Vectors
    frame_embs = model.encode(frames)
    
    # 4. Find the best match using Cosine Similarity
    scores = util.cos_sim(text_emb, frame_embs)
    
    # Get the highest score and its index
    best_match_idx = scores.argmax().item()
    best_score = scores[0][best_match_idx].item()
    
    return frames[best_match_idx], timestamps[best_match_idx], best_score