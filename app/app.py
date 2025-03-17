import streamlit as st
from cryptography.fernet import Fernet, InvalidToken
from PIL import Image
import struct
import io

# Page Config
st.set_page_config(page_title="DFTK Crypto-Stego Tool", layout="wide")

# Main Header
st.title("🔐 DFTK Crypto-Stego Tool")
st.markdown("**Secure Digital Forensics Toolkit for Cryptographic Operations & Steganographic Analysis**")

# Description Section
st.markdown("""
## 🌟 Welcome to DFTK Forensic Toolkit

**A unified platform for secure file operations and covert communication analysis**  
            
This tool combines advanced cryptographic methods with image steganography techniques to help forensic investigators:
- 🔒 Protect sensitive case files
- 📨 Securely communicate findings
- 🔍 Detect hidden information in digital media
""")

st.markdown("---")

# Cryptography Section Description
st.markdown("""
## 🔐 Cryptographic Module
**Secure File Encryption & Decryption**

Features:
- 🗝️ AES-128 encryption with Fernet keys
- 🔄 Batch file processing capability
- ⚡ On-demand key generation
- 🛡️ Tamper-proof encrypted outputs

*Ideal for:*  
- Securing case evidence packages  
- Protecting sensitive investigation documents  
- Encrypting forensic audit reports
""")

st.markdown("---")

# Steganography Section Description
st.markdown("""
## 🖼️ Steganography Module
**Covert Message Embedding & Extraction**

Features:
- 📸 PNG image carrier support
- 🔍 Least Significant Bit (LSB) encoding
- 📝 Text message obfuscation
- 🔎 Hidden message detection

*Ideal for:*  
- Secure investigator communications  
- Metadata concealment  
- Covert operations documentation
""")



# ... (keep the rest of your original code for Cryptography and Steganography functionality)

st.caption("DFTK Forensic Toolkit | Crypto-Stego Module v1.0 | Confidential Operations Only")