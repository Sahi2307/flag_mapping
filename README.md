# Flag Pattern Warping and Blending App

This is a simple interactive image processing application built with **Streamlit** and **OpenCV**. The app allows users to upload a flag image and a pattern image, then warps the pattern to match the flag's folds, blends them seamlessly, and displays a realistic final result.

---

## 📦 Features

- Perspective warping of a pattern image onto a flag
- Realistic fold deformation based on image gradients
- Soft shading effect to enhance 3D look
- Smooth alpha blending with controllable opacity
- Interactive file upload via a web UI (Streamlit)

---

## 📁 Project Structure

flag_mapping_project/
├── script.py               # Main Streamlit application
├── README.md            # Project documentation
├── flag.png         
├── pattern.png      

---

## 📋 Requirements

- Python 3.8+
- Streamlit
- OpenCV (opencv-python)
- NumPy

---

## 📦 Installation

1️⃣ Clone or download the repository.

2️⃣ Install required Python packages:

```

pip install streamlit opencv-python numpy

```

---

## 🚀 Running the Application

In your terminal, navigate to the project folder:

```

cd path\to\flag\_mapping\_project

```

Then, launch the app:

```

streamlit run script.py

```

The app will open automatically in your default web browser at:

http://localhost:8501

---

## 🖼️ How to Use

1. Upload a **flag image** (PNG, JPG, JPEG)
2. Upload a **pattern image** (PNG, JPG, JPEG)
3. View the final blended flag image with realistic warping and shading.

---

## 📸 Example Output

| Input Flag | Input Pattern | Warped & Blended |
|:------------:|:----------------:|:------------------|
| ![flag](flag_example.png) | ![pattern](pattern_example.png) | ![output](output_example.png) |

---

## 📖 Credits

Built using:
- Streamlit (https://streamlit.io/)
- OpenCV (https://opencv.org/)
- NumPy (https://numpy.org/)

---

## 📝 License

This project is open-source and available for educational and non-commercial use.
```

---

