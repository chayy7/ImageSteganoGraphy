🕵️‍♂️ Image Steganography with Python
A simple yet effective Python project to hide and reveal secret messages inside images using LSB (Least Significant Bit) steganography. This project uses the stegano library to encode text within PNG images in a way that’s invisible to the human eye but can be programmatically revealed.

🔐 Features
🔏 Hide secret text inside an image without altering its visual appearance

🔓 Extract hidden text from the encoded image

📂 Save encrypted images with custom names

💡 Easy to use and modify for educational or practical purposes

🧠 How It Works
This project uses Least Significant Bit (LSB) steganography, where message bits are inserted into the least significant bits of an image’s pixel values. Since the changes are so subtle, the human eye can’t detect them — but the message remains intact inside the file.

🛠️ Technologies Used
Python 3
stegano library
PNG images (for lossless encoding)
