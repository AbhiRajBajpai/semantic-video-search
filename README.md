🔍 Semantic Video Search Engine (AI-Powered)

A multimodal AI tool that allows users to search for specific events or scenes inside a video using natural language queries (e.g., "A red car turning left" or "Someone laughing"). It leverages OpenAI's CLIP model to understand the semantic relationship between video frames and text, enabling zero-shot search capabilities without manual tagging.

Live Link :- https://huggingface.co/spaces/AbhiRajBajpai123/semantic-video-search

🏗️ System Architecture

The system follows a modular pipeline approach, processing video data into vector embeddings and performing similarity searches in real-time.

graph TD
    User([User]) -->|1. Uploads Video| UI[Streamlit Frontend]
    User -->|2. Enters Text Query| UI
    
    subgraph "Processing Pipeline"
        UI -->|Video File| OpenCV[Frame Processor (OpenCV)]
        OpenCV -->|Extracts 1 Frame/2s| Frames[Frame Buffer]
        Frames -->|Batch Images| CLIP[CLIP AI Model]
        UI -->|Text Query| CLIP
    end
    
    subgraph "Search Engine"
        CLIP -->|Image Embeddings| VectorSpace[Vector Space]
        CLIP -->|Text Embedding| VectorSpace
        VectorSpace -->|Cosine Similarity| Ranker[Ranking Logic]
    end
    
    Ranker -->|3. Best Timestamp & Confidence| UI
    UI -->|4. Auto-Jump Video Player| User


✨ Key Features

🧠 Multimodal AI: Uses OpenAI's CLIP (Contrastive Language-Image Pre-Training) to map text and images to a shared vector space.

🕵️‍♂️ Natural Language Search: Users can search using abstract concepts or specific descriptions, not just pre-defined tags.

⏱️ Precise Timestamping: Identifies the exact second an event occurs and automatically cues the video player to that moment.

🎚️ Confidence Filtering: Includes a user-adjustable threshold slider to filter out low-confidence matches.

📸 Evidence Extraction: Allows users to download the exact frame where the event was detected as a high-quality JPEG.

🛠️ Tech Stack

Component

Technology

Purpose

Frontend

Streamlit

Web Interface and Video Player

AI Model

Sentence-Transformers (CLIP)

Generating Vector Embeddings

Computer Vision

OpenCV

Video Frame Extraction & Processing

Deployment

Docker & Hugging Face Spaces

Cloud Hosting & Containerization

Backend Logic

Python 3.9

Core Application Logic

🚀 Installation & Local Setup

Follow these steps to run the project locally on your machine.

Prerequisites

Python 3.8 or higher

Git

1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/semantic-video-search.git](https://github.com/YOUR_USERNAME/semantic-video-search.git)
cd semantic-video-search


2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the Application

streamlit run app.py


The app will automatically open in your browser at http://localhost:8501.

📂 Project Structure

semantic-video-search/
├── app.py                # Main Streamlit application (Frontend)
├── processor.py          # Video processing logic (OpenCV)
├── search_engine.py      # AI Model loading and Vector Search logic
├── requirements.txt      # List of dependencies
├── Dockerfile            # Container configuration for Deployment
└── README.md             # Project documentation


🤝 Contribution

Contributions are welcome! Please open an issue or submit a pull request for any bugs or improvements.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
