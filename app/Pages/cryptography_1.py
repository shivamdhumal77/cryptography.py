import streamlit as st
from cryptography.fernet import Fernet, InvalidToken

# Set page config
st.set_page_config(page_title="DFTK Cryptography Tool", layout="wide")
st.title("\U0001F512 DFTK Cryptography Tool")
st.markdown("Secure File Encryption/Decryption for Digital Forensics")

# Functions
@st.cache_data
def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

# Sidebar Operations
operation = st.sidebar.radio("Select Operation", ["Generate Key", "Encrypt File", "Decrypt File"])

# Key Generation
if operation == "Generate Key":
    st.header("\U0001F511 Generate Encryption Key")
    key_name = st.text_input("Key File Name", "forensic.key")
    if st.button("Generate Key"):
        key = generate_key()
        st.success(f"Key generated and saved as {key_name}")
        st.download_button("Download Key", key, file_name=key_name, mime="application/octet-stream")

# Encryption
elif operation == "Encrypt File":
    st.header("\U0001F510 Encrypt File")
    key_file = st.file_uploader("Upload Key File", type=["key"], key="encrypt_key")
    input_file = st.file_uploader("Select File to Encrypt", key="encrypt_file")

    if key_file and input_file:
        key = key_file.read()
        if len(key) != 44:
            st.error("Invalid key! Please upload a valid .key file.")
        else:
            data = input_file.read()
            if st.button("Encrypt"):
                encrypted_data = encrypt_data(data, key)
                encrypted_filename = f"encrypted_{input_file.name}.enc"
                st.success("File encrypted successfully!")
                st.download_button("Download Encrypted File", encrypted_data, file_name=encrypted_filename, mime="application/octet-stream")

# Decryption
elif operation == "Decrypt File":
    st.header("\U0001F513 Decrypt File")
    key_file = st.file_uploader("Upload Key File", type=["key"], key="decrypt_key")
    encrypted_file = st.file_uploader("Select Encrypted File", type=["enc", "bin"], key="decrypt_file")

    if key_file and encrypted_file:
        key = key_file.read()
        if len(key) != 44:
            st.error("Invalid key! Please upload a valid .key file.")
        else:
            encrypted_data = encrypted_file.read()
            if st.button("Decrypt"):
                try:
                    decrypted_data = decrypt_data(encrypted_data, key)

                    # Fix filename reconstruction
                    original_filename = encrypted_file.name
                    if original_filename.startswith("encrypted_"):
                        original_filename = original_filename[len("encrypted_"):]
                    if original_filename.endswith(".enc"):
                        original_filename = original_filename[:-4]

                    decrypted_filename = f"decrypted_{original_filename}"

                    st.success("File decrypted successfully!")
                    st.download_button("Download Decrypted File", 
                                       decrypted_data, 
                                       file_name=decrypted_filename,
                                       mime="application/octet-stream")
                except InvalidToken:
                    st.error("Decryption failed! Invalid key or corrupted data.")

# User Guide
with st.expander("\U0001F4D6 User Guide"):
    st.markdown(
        """
        ## DFTK Cryptography Tool Guide
        **1. Generate Key**
        - Click 'Generate Key' button
        - Download and store securely

        **2. Encrypt File**
        - Upload generated key file
        - Select file to encrypt
        - Click 'Encrypt' and download the encrypted file

        **3. Decrypt File**
        - Upload same key used for encryption
        - Select encrypted file
        - Click 'Decrypt' and download the decrypted file

        ⚠️ **Important:** Never share encryption keys or encrypted files publicly.
        """
    )

st.markdown("---")
st.caption("DFTK Forensic Toolkit | Secure Cryptographic Operations Module v1.0")
