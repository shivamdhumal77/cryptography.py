# DFTK Cryptography Tool

## Overview
DFTK Cryptography Tool is a secure file encryption and decryption application designed for digital forensics. It uses the robust Fernet symmetric encryption from the Python `cryptography` library to protect sensitive data with ease. Built with Streamlit, the app provides a user-friendly interface for generating encryption keys, encrypting files, and decrypting them securely.

## Features
- **Key Generation:** Generate a secure encryption key and download it for safekeeping.
- **File Encryption:** Encrypt any file with your key, ensuring data confidentiality.
- **File Decryption:** Decrypt files using the same key, recovering the original content.
- **User-Friendly Interface:** Clean and simple UI powered by Streamlit.

## Prerequisites
- Python 3.8 or higher
- Docker (Optional for containerized deployment)

## Usage
Run the Streamlit app locally:
```bash
streamlit run cryptography_1.py
```
Access the app at: `http://localhost:8501`

## Docker Deployment
1. Build the Docker image:
```bash
docker build -t dftk-crypto-tool .
```
2. Run the container:
```bash
docker run -p 8501:8501 dftk-crypto-tool
```
Access the app at: `http://localhost:8501`

## Key Generation
1. Navigate to the "Generate Key" section.
2. Click the **Generate Key** button.
3. Download the key file and keep it secure.

## File Encryption
1. Go to the "Encrypt File" section.
2. Upload your key file.
3. Select the file you want to encrypt.
4. Click **Encrypt** and download the encrypted file.

## File Decryption
1. Access the "Decrypt File" section.
2. Upload the same key used during encryption.
3. Upload the encrypted file.
4. Click **Decrypt** and download the decrypted file.

## Security Note
- Keep the encryption key safe. Without it, decryption is impossible.
- Do not share keys or encrypted files publicly.

## File Types Supported
The app can handle any file type for encryption and decryption, making it highly versatile.

## Requirements
- `streamlit`
- `cryptography`

## Author
- **Shivam Dhumal**

## License
This project is licensed under the MIT License.

## Acknowledgments
- Built with [Streamlit](https://streamlit.io/)
- Encryption powered by [Cryptography](https://cryptography.io/)

Enjoy secure encryption and decryption with ease! ✅

