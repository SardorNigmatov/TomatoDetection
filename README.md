# TomatoDetection

TomatoDetection is a computer vision project based on the YOLOv11 model to detect tomatoes in images. The model is trained and evaluated on a custom dataset to ensure accurate and robust predictions.

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Model Architecture](#model-architecture)
3. [Training Details](#training-details)
4. [Results](#results)
5. [Examples](#examples)
6. [Usage](#usage)
7. [Acknowledgments](#acknowledgments)

---

## 🌟 Project Overview

This project utilizes YOLOv11 for detecting tomatoes in images. The main goals include:
- High accuracy in detecting tomatoes in various environments.
- Fast and efficient inference.
- Easy integration into real-world applications.

---

## 🏗 Model Architecture

YOLOv11 is an advanced object detection model designed for speed and accuracy. It features:
- Backbone: CSPNet for feature extraction.
- Neck: PANet for feature aggregation.
- Head: YOLO layers for object detection.

---

## 🔧 Training Details

- **Dataset**: Custom dataset containing labeled images of tomatoes.
- **Optimizer**: Adam
- **Loss Function**: Binary cross-entropy loss with IoU.
- **Learning Rate**: 0.001 with cosine annealing scheduler.
- **Epochs**: 100
- **Batch Size**: 8
---

## 📊 Results

### Performance

(![F1_curve](https://github.com/user-attachments/assets/8124882c-c428-4498-ae9d-5bb77df15ae3))

(![P_curve]((https://github.com/user-attachments/assets/a76a3715-916d-4342-8004-bfa66378b070))

(![PR_curve](https://github.com/user-attachments/assets/4e0506e2-3f69-4a4d-a1f0-6adc35c87c68))

(![results](https://github.com/user-attachments/assets/528fe25e-aa79-4938-aa50-1f5f929eafdf))

---

## 🖼 Examples

Below are some examples of the model's predictions on test images.

### Example 1
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
|(![test_img1](https://github.com/user-attachments/assets/ee868f02-1e76-48fd-9b78-57403b0fadbf) |(![test_img1](https://github.com/user-attachments/assets/5ac32383-c3cd-4928-b3e4-08854af33142)) |

### Example 2
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
|(![test_img2](https://github.com/user-attachments/assets/9c273d67-1f92-42ed-bd23-739df467b718)) | (![test_img2](https://github.com/user-attachments/assets/0487079d-a4f7-4d43-a4ad-ca0ffc1ebc89)) |

### Example 3
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
|(![test_img3](https://github.com/user-attachments/assets/e23f867c-2077-4a73-abcd-70fb24686ab4)) | (![test_img3](https://github.com/user-attachments/assets/fbfb40ea-630c-4fe8-a340-8e3e87941534)) |

---

## 🤝 Acknowledgments

- YOLOv11 authors for the amazing model architecture.
- Dataset contributors for providing labeled tomato images.

---

## Dataset
https://www.kaggle.com/datasets/sardornigmatov/tomatodetectiondataset
