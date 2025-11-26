# 🧍‍♂️ Posture Analyzer (OpenCV + MediaPipe + Streamlit + Docker)

This project is a **Posture Analysis System** built using **OpenCV**, **MediaPipe**, and **Streamlit**, capable of tracking knee movement, drawing pose landmarks, and visualizing joint motion paths.  
The entire application is **Dockerized**, making it extremely easy to run anywhere without dependency issues.

---

## 🚀 Features

- Real-time posture estimation using **MediaPipe Pose**
- Knee tracking with live plotted trajectories
- Visual output of pose skeleton
- Streamlit interface for:
  - Uploading custom videos  
  - Using built-in sample videos  
  - Running analysis with a single click
- Fully containerized using Docker
- Works consistently across systems due to Docker isolation

---

## 📁 Project Structure

```text
PostureAnalysis/
│── Analyzer.py
│── app.py
│── Sample1.mp4
│── Sample2.mp4
│── requirements.txt
│── Dockerfile
└── README.md
```

---

## 🧠 How It Works

- The **`Analyzer.py`** file handles all processing:
  - Reads video frames
  - Extracts pose landmarks
  - Tracks knee positions
  - Displays pose and extracted keypoints
- The **Streamlit app** provides a simple UI for interacting with the analyzer.
- With **Docker**, everything runs the same on any machine.

---

## 🖥️ Running Locally (Without Docker)

### 1️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate it

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit app

```bash
streamlit run app.py
```

---

# 🐳 Running Using Docker (Recommended)

## 1️⃣ Build Docker Image

Run this inside your project folder:

```bash
docker build -t marti18/analyzer .
```

---

## 2️⃣ Run the Container

```bash
docker run -p 8501:8501 marti18/analyzer
```

Now open your browser and go to:

👉 **[http://localhost:8501](http://localhost:8501)**

---

## 3️⃣ Push Image to Docker Hub

### Login
```bash
docker login
```

### Tag image
```bash
docker tag marti18/analyzer marti18/analyzer:latest
```

### Push image
```bash
docker push marti18/analyzer:latest
```

You can now pull it from anywhere using:
```bash
docker pull marti18/analyzer
docker run -p 8501:8501 marti18/analyzer
```

---

# 🧪 Example Usage

### ▶ Run analysis on:
* Uploaded video
* Sample1.mp4
* Sample2.mp4

Streamlit provides:
* Pose skeleton window
* Extracted pose window
* Knee trajectory plot

---

# 📦 Requirements

All dependencies are listed inside **requirements.txt**:

```text
opencv-python
mediapipe
numpy
matplotlib
streamlit
```

---

# 🛠 Technologies Used

* **Python**
* **OpenCV**
* **MediaPipe**
* **Matplotlib**
* **Streamlit**
* **Docker**

---

# ✨ Author
**Aditya Pratap Singh**
