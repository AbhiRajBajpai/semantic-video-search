# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set the working directory to the user's home directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# --- SPEED UP FIX ---
# Install the lightweight CPU-only version of PyTorch first.
# This saves about 2GB of download size and prevents memory crashes.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Now install the rest (Streamlit, etc.)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Create a non-root user and switch to it (Security Best Practice)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

# Hugging Face Spaces expect applications to run on port 7860
EXPOSE 7860

# Run the application on port 7860
# CRITICAL FIX: We added --server.enableCORS=false and --server.enableXsrfProtection=false 
# This fixes the "403 Forbidden" / "AxiosError" on Hugging Face
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
