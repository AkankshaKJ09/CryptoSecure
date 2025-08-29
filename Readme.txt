AES Cryptography Tool 

A modern web-based implementation of Advanced Encryption Standard (AES-256) using PyCryptodome library. This tool provides secure encryption and decryption through an intuitive browser interface.


Features:

🔐 AES-256 encryption with CBC mode

🖥️ Clean, responsive web interface

📋 Copy-to-clipboard functionality

🔑 Automatic key derivation (SHA-256)

☁️ Ready for cloud deployment



Technology Stack:

Backend: Python (PyCryptodome)

Frontend: HTML5, CSS3, JavaScript

Server: Flask with Gunicorn

Security: AES-CBC with PKCS#7 padding and random IV generation



Installation:

bash
# Clone repository
git clone https://github.com/Abhims898/AES-Guardian

# Install dependencies
pip install -r requirements.txt
Usage



Encryption Tab:

Enter plaintext in the input field

Provide any secret key

Click "Encrypt" to generate Base64-encoded ciphertext



Decryption Tab:

Paste Base64 ciphertext

Enter the original secret key

Click "Decrypt" to recover the original message



Security Features:

SHA-256 key derivation from any input

Random 16-byte IV for each encryption

PKCS#7 padding validation

Secure CBC mode implementation

Server-side key zeroization after processing


Live Demo:

Experience the application live at: https://cryptosecure-9r5r.onrender.com



Contributing:

Contributions are welcome! Please submit pull requests for:

Implementation of additional AES modes (GCM, CTR)

Enhanced key management features

Improved UI/UX components

Security audit recommendations



Repository:

GitHub Repository: https://github.com/AkankshaKJ09/CryptoSecure