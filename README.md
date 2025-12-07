# 🖼️ Image Steganography Tool (Python)

 A simple & efficient **image steganography tool** built in Python that allows you to **hide & extract secret messages inside images** using the **Least Significant Bit (LSB)** technique.  

 This project demonstrates practical concepts of steganography, image processing, & bit-level data manipulation.

## 🚀 Features
 
 - Hide secret text inside image files.
 - Extract hidden text from steganographic images.
 - Uses LSB (Least Significant Bit) technique on RGB pixels.
 - Automatic end-of-message detection.
 - Command-line interface using `argparse`.
 - Supports common lossless image formats (PNG, BMP).
 - Clean & beginner-friendly code structure.

## 🧠 How It Works

 - Each character is converted into an **8-bit binary representation**.
 - Binary bits are embedded into the **LSBs of RGB pixel values**.
 - **3 pixels store one character**.
 - A **terminator bit** marks the end of the hidden message.
 - During decoding, bits are read until the terminator is detected.
  
## 📂 Project Structure

 ```tree
 📁 steganography
 ├── main.py
 └── README.md
 ```

## 📦 Requirements

 Install dependencies via pip:

 ```bash
 pip install pillow
 ```

## 1️⃣ Clone the Repository

 ```bash
 git clone https://github.com/m-rishad78/steganography.git
 ```

## 2️⃣ Navigate to the Project Directory

 ```bash
 cd steganography
 ```

## ▶️ Usage

 **🔐 Encode Data**

 ```text
 python main.py -m e -f input.png -d "Secret Message" -o output.png
 ```

 | Flag     | Description       |
 |----------|-------------------|
 | `-m e`   | Encode mode       |
 | `-f`     | Input image file  |
 | `-d`     | Text data to hide |
 | `-o`     | Output image file |

 **🔓 Decode Data**

 ```text
 python main.py -m d -f output.png
 ```

## 📏 Data Capacity

 - Each character requires **3 pixels**
 - Maximum characters supported:

   ```text
   ((image_width * image_height) / 3)
   ```
 
 An error is raised if the data exceeds image capacity.

## ⚠️ Limitations

 - No encryption applied to hidden data.
 - Image resizing, compression, or re-saving may corrupt hidden data.
 - Works best with **lossless image formats**.
 - Intended for educational & learning purposes only.

## 📖 Learning Objectives

 - Fundamentals of steganography
 - Bit-level data representation
 - Image processing with `Pillow`
 - Secure data hiding techniques
 - Command-line application design

## ⭐ Contributing

 Contributions are welcome!  
 Feel free to open issues & submit pull requests.

## 📜 License

 This project is licensed under the **MIT License**.  
 You are free to use, modify, & distribute it.
