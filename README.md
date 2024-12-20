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

| Metric           | Value       |
|------------------|-------------|
| Training Accuracy| 96.5%       |
| Validation Accuracy| 94.8%     |
| mAP@50           | 92.7%       |

---

## 📊 Results

### Training Performance

![Training Accuracy](![P_curve](https://github.com/user-attachments/assets/0401308a-432f-47e3-8278-5c98067f756f)


### Validation Performance

![Validation Accuracy](![F1_curve](https://github.com/user-attachments/assets/dac63c8f-9cfc-4412-bc78-f4608cc9ae03)


---

## 🖼 Examples

Below are some examples of the model's predictions on test images.

### Example 1
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
| ![Original](path_to_original_image1.png) | ![Prediction](path_to_predicted_image1.png) |

### Example 2
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
| ![Original](path_to_original_image2.png) | ![Prediction](path_to_predicted_image2.png) |

### Example 3
| Original Image            | Predicted Output        |
|---------------------------|-------------------------|
| ![Original](path_to_original_image3.png) | ![Prediction](path_to_predicted_image3.png) |

---

## 🚀 Usage

### Installation

```bash
# Clone the repository
git clone https://github.com/your_username/TomatoDetection.git

# Navigate to the project directory
cd TomatoDetection

# Install dependencies
pip install -r requirements.txt
```

### Running Inference

```bash
python detect.py --source /path_to_image_folder --weights yolov11_weights.pth
```

---

## 🤝 Acknowledgments

- YOLOv11 authors for the amazing model architecture.
- Dataset contributors for providing labeled tomato images.

---

**Author**: [Nigmatov Sardor]

For more details, check out the full project repository on [GitHub](https://github.com/your_username/TomatoDetection).
