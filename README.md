# 🏁 Flag Pattern Warping & Blending 

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An interactive web application that allows users to **map any pattern onto a flag image** realistically by warping, blending, and shading. Powered by **Streamlit**, **OpenCV**, and **NumPy**, this app gives users a smooth, browser-based image processing experience.


## ✨ Features

Warp a pattern image onto the folds of a flag  
Preserve realistic deformation using image gradients  
Smooth alpha blending with opacity control  
Interactive drag-and-drop image upload  
Built using only open-source Python libraries

---

## 🎬 Demo

Launch the app locally:

```bash
streamlit run script.py
````

Once running, visit: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```plaintext
flag_mapping/
├── script.py          
├── README.md          
├── flag.png           
├── pattern.png        
├── requirements.txt
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sahi2307/flag_mapping.git
cd flag_mapping
```

### 2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed. Then, install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, run:

```bash
pip install streamlit opencv-python numpy
```

---

## 🚀 Usage

In your terminal, navigate to the project directory and run:

```bash
streamlit run script.py
```

Then:

1. Upload a **flag image** (formats: PNG, JPG, JPEG)
2. Upload a **pattern image**
3. The application will:

   * Warp the pattern onto the folds of the flag
   * Apply realistic shading and blending
4. View/download the final output directly from the UI

---

## ⚙️ Technologies Used

* [Python 3.8+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the MIT License.
Feel free to use it for **educational** and **non-commercial** purposes.

---

## 🙌 Acknowledgments

Thanks to the open-source community and the developers of:

* Streamlit
* OpenCV
* NumPy

---

*Built with ❤️ for creative image processing*

```
