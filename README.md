# 👁️ GodsEye: Drone-Based Surveillance & Violence Detection

![Python](https://img.shields.io/badge/Python-3.7-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

> **Awarded "Best Project" at Department Level**

**GodsEye** is an intelligent surveillance system designed for drones and static cameras. It utilizes Deep Learning (YOLOv3) and Pose Estimation to automatically detect violent behavior in real-time video streams. By analyzing human posture and interaction, the system achieves **90% accuracy** in distinguishing between normal activities and violent altercations.

---

## 🚀 Features

* **Real-Time Violence Detection:** Processes live video feeds to identify aggressive behavior instantly.
* **Posture Analysis:** Uses Multipose models to analyze skeleton keypoints, distinguishing complex actions beyond simple object detection.
* **Drone Integration:** Optimized for aerial footage processing, handling varying angles and distances.
* **Web Dashboard:** A Django-based control center for viewing live streams and system alerts.
* **High Accuracy:** Fine-tuned YOLOv3 integration achieving 90% validation accuracy on test datasets.

---

## 🛠️ Technology Stack

* **Core Logic:** Python 3.7
* **Deep Learning:** TensorFlow, Keras, YOLOv3 (You Only Look Once)
* **Computer Vision:** OpenCV
* **Backend/Web Framework:** Django
* **Pose Estimation:** Multi-Person Pose Estimation Model

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.7** installed. This project relies on specific dependencies that may not be compatible with newer Python versions.

### 2. Clone the Repository
```bash
git clone [https://github.com/MasterShifu619/GodsEye.git](https://github.com/MasterShifu619/GodsEye.git)
cd GodsEye
```

download multipose model from the following google drive link:
https://drive.google.com/open?id=125ZjLLjpcFJ9i4yTclwTS1v5gO6OoXt7

download complete virtual environment from:
https://drive.google.com/open?id=1h_RCAJUY3StHYtdX9ovE2dC-lhb6cwXO

To run the program:
s1>change directory to the api folder
s2>python manage.py runserver

Python 3.7 should be used and the site-packages from the venv should be copy-pasted into the site-packages of python 3.7 excluding the py_cache folder

django admin. (has to be creatd using command: "python manage.py createsuperuser"
username: bipingowda
pwd.: godseye
