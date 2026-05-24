<div align="center">

<img src="https://img.shields.io/badge/AWARD-Best%20Project%20%F0%9F%8F%86-gold?style=for-the-badge" alt="Award"/>

# 👁️ GodsEye

### Intelligent Surveillance & Automated Violence Detection

*Drone-ready. Multi-environment. 90% accurate.*

[![Python](https://img.shields.io/badge/Python-3.7-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-2.3-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Django](https://img.shields.io/badge/Django-3.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.22-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

</div>

---

## 📌 What is GodsEye?

GodsEye is an automated violence detection system built for drones and static surveillance cameras. It processes raw video feeds — no human monitoring required — and flags violent behavior in real time by analyzing human body posture and joint movement patterns.

Upload a video. Select an environment. GodsEye returns an annotated output video with violent frames highlighted and a dashboard summary.

> Awarded **Best Project** at the Department Level.

---

## 🎬 Demo

| Input Frame | Pose Skeleton | Output (Violence Detected) |
|:-----------:|:-------------:|:--------------------------:|
| Raw video frame | OpenPose skeleton overlay | Red skeleton = violent, Green = non-violent |

> *(Add demo GIF or screenshots here)*

---

## 🧠 How It Works

GodsEye uses a **3-stage pipeline**:

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────────┐     ┌─────────────┐
│  Video File  │────▶│  Frame Sampling  │────▶│   OpenPose (CMU)    │────▶│  Classifier │
│  (.mp4)     │     │  N frames/sec    │     │  18 keypoints/person│     │  SVM / RF   │
└─────────────┘     └──────────────────┘     └──────────┬──────────┘     └──────┬──────┘
                                                         │ pose fails?           │
                                                         ▼                       ▼
                                               ┌──────────────────┐    ┌─────────────────┐
                                               │   CNN Fallback   │    │  V  = 🔴 Red     │
                                               │  (50x50 grayscale│    │  NV = 🟢 Green   │
                                               └──────────────────┘    └─────────────────┘
                                                                                 │
                                                         ┌───────────────────────┘
                                                         ▼
                                               ┌──────────────────┐
                                               │  ffmpeg → .mp4   │
                                               │  Django Dashboard │
                                               └──────────────────┘
```

### Stage 1 — Frame Sampling
Randomly samples `N` frames per second-block (configurable 1–10). Skips corrupt frames automatically.

### Stage 2 — Multi-Person Pose Estimation (OpenPose)
- **Model:** CMU OpenPose Caffe (`pose_iter_440000.caffemodel`)
- Outputs **18 heatmaps** (one per body joint) + **38 Part Affinity Fields (PAFs)**
- Joints: `Nose, Neck, R-Shoulder, R-Elbow, R-Wrist, L-Shoulder, L-Elbow, L-Wrist, R-Hip, R-Knee, R-Ankle, L-Hip, L-Knee, L-Ankle, R-Eye, L-Eye, R-Ear, L-Ear`
- PAFs encode limb direction — used to correctly assign joints to individual people in crowded scenes
- Persons with >7 missing joints are discarded

### Stage 3 — Feature Extraction & Classification

**Feature vector (12 values):** Euclidean distances from the **Neck** joint to each of the 12 body joints below it. This encodes body posture as a compact, scale-invariant signature.

```
Feature = [dist(Neck→R-Sho), dist(Neck→L-Sho), dist(Neck→R-Elb), dist(Neck→L-Elb),
           dist(Neck→R-Wr),  dist(Neck→L-Wr),  dist(Neck→R-Hip), dist(Neck→L-Hip),
           dist(Neck→R-Knee),dist(Neck→L-Knee), dist(Neck→R-Ank), dist(Neck→L-Ank)]
```

| Classifier | Algorithm | Use Case |
|:----------:|:---------:|:--------:|
| Primary | Support Vector Machine (SVM) | ATM surveillance |
| Primary | Random Forest (100 trees) | Sports venues |
| Fallback | CNN (TensorFlow/Keras) | When pose estimation fails |

**CNN Fallback:** When OpenPose cannot reliably detect skeletons (low-quality frames, extreme angles), the system falls back to a grayscale CNN classifier on the raw frame (50×50 input).

---

## ✨ Features

- 🎯 **90% Accuracy** on test datasets
- 👥 **Multi-Person** — detects and classifies every person in the frame simultaneously
- 🏟️ **Multi-Environment** — separate trained models for ATM and Sports scenarios
- 🔄 **Dual Classifier** — SVM/Random Forest with CNN fallback for robustness
- 🌐 **Web Dashboard** — upload, process, and review results in a browser
- 🖼️ **Photo Grid** — all flagged violent frames displayed for review
- 📹 **Annotated Video Output** — output `.mp4` with colored skeleton overlays
- 🚁 **Drone-Ready** — handles aerial footage angles and distances

---

## 🛠️ Tech Stack

| Layer | Technology |
|:------|:-----------|
| Language | Python 3.7 |
| Computer Vision | OpenCV 4.1 |
| Pose Estimation | OpenPose (CMU Caffe model) |
| Deep Learning | TensorFlow 2.0, Keras 2.3 |
| ML Classifiers | scikit-learn 0.22 (SVM, Random Forest) |
| Web Framework | Django 3.0 |
| Video Processing | ffmpeg |
| Database | SQLite |
| Frontend | HTML/CSS/JS, Bootstrap |

---

## ⚙️ Installation

### Prerequisites

- Python **3.7** (required — dependencies not compatible with 3.8+)
- ffmpeg installed and on PATH
- Windows OS (paths currently hardcoded for Windows)

### 1. Clone the repository

```bash
git clone https://github.com/MasterShifu619/GodsEye.git
cd GodsEye
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the OpenPose model

Download `multipose_model/` (prototxt + caffemodel) from Google Drive and place it in the project root:

📥 [Download multipose_model](https://drive.google.com/open?id=125ZjLLjpcFJ9i4yTclwTS1v5gO6OoXt7)

```
GodsEye/
└── multipose_model/
    ├── pose_deploy_linevec.prototxt
    └── pose_iter_440000.caffemodel
```

### 4. (Optional) Download pre-built virtual environment

If you want to skip dependency installation entirely:

📥 [Download venv](https://drive.google.com/open?id=1h_RCAJUY3StHYtdX9ovE2dC-lhb6cwXO)

Copy the contents of `venv/Lib/site-packages/` into your Python 3.7 `site-packages/` (exclude `__pycache__`).

### 5. Run the server

```bash
cd api
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## 🚀 Usage

### 1. Upload a video
Navigate to **Preview Video** → upload your `.mp4` file.

### 2. Generate output
Navigate to **Generate Output** → select:
- **Video** — choose from uploaded videos
- **Environment** — `ATM` or `Sports`
- **Frames/sec** — how many frames per second to analyze (1–10; higher = slower but more thorough)

### 3. Review results
- Annotated output video plays directly in the browser
- **Photo Grid** shows every flagged violent frame
- Dashboard displays: input FPS, output FPS, people detected, violence found, processing time

---

## 📊 Training Your Own Model

Training data is stored as CSV with 12 distance features + label:

```
Name, R-Sho, L-Sho, R-Elb, L-Elb, R-Wr, L-Wr, R-Hip, L-Hip, R-Knee, L-Knee, R-Ank, L-Ank, Color, Class
```

**Generate training data from videos:**

```bash
# Sampled frames (recommended)
python main.py          # edit video_name inside the script

# All frames
python main_all.py      # edit video_name inside the script
```

**Train classifiers:**

```bash
python random_forest.py   # trains Random Forest, saves .sav
python svm.py             # trains SVM, saves .sav
```

Trained models are saved as `.sav` (pickle) files. Place them in the project root and update the environment mapping in `main_test.py`.

---

## 📁 Project Structure

```
GodsEye/
├── multipose.py            # OpenPose inference + feature extraction (training mode)
├── multipose_test.py       # OpenPose inference + classification (inference mode)
├── main.py                 # Training data generator (sampled frames)
├── main_all.py             # Training data generator (all frames)
├── main_test.py            # Inference pipeline (called by Django)
├── classification.py       # Loads .sav model, returns V/NV prediction
├── img_classification.py   # CNN fallback classifier
├── random_forest.py        # Random Forest training script
├── svm.py                  # SVM training script
├── output/
│   └── generate_video.py   # ffmpeg frame → mp4 stitcher
├── api/                    # Django project
│   ├── first_app/
│   │   ├── views.py        # Upload, process, display logic
│   │   ├── models.py       # Video, Video_info models
│   │   └── forms.py        # VideoForm, fps slider
│   └── templates/
│       └── first_app/      # HTML templates
├── training.csv            # ATM training dataset
├── sports.csv              # Sports training dataset
├── model_jairaj_home.sav   # Trained SVM (ATM)
├── sports.sav              # Trained Random Forest (Sports)
├── model_jairaj_home.h5    # CNN fallback (ATM)
└── sports.h5               # CNN fallback (Sports)
```

---

## ⚠️ Known Limitations

- Hardcoded Windows paths (`C:/Users/Bipin Gowda/...`) — requires path updates before use on another machine
- Python 3.7 only — TensorFlow 2.0 and older scikit-learn are incompatible with 3.8+
- CNN fallback accuracy lower than pose-based classifier
- Processing is CPU-bound and slow on large videos (no GPU acceleration configured)

---

## 🤝 Contributing

Pull requests welcome. For major changes, open an issue first.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

<div align="center">

Built with ❤️ | Awarded Best Project 🏆

</div>
