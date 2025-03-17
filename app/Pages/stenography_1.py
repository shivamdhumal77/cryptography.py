import streamlit as st
from PIL import Image
import struct
import io

def encode_image(image, message):
    # Convert to RGB
    img = image.convert('RGB')
    pixels = list(img.getdata())
    width, height = img.size
    
    # Prepare the message
    message_bytes = message.encode('utf-8')
    message_len = len(message_bytes)
    
    # Create header with message length (4 bytes)
    header = struct.pack('>I', message_len)
    header_bits = ''.join(format(byte, '08b') for byte in header)
    message_bits = ''.join(format(byte, '08b') for byte in message_bytes)
    all_bits = header_bits + message_bits
    
    # Check if image can store the message
    required_bits = len(all_bits)
    available_bits = len(pixels) * 3
    if required_bits > available_bits:
        raise ValueError("Message too long for the image")
    
    # Modify pixels to encode message
    new_pixels = []
    bit_index = 0
    for pixel in pixels:
        r, g, b = pixel
        if bit_index < required_bits:
            r = (r & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        if bit_index < required_bits:
            g = (g & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        if bit_index < required_bits:
            b = (b & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        new_pixels.append((r, g, b))
    
    # Save the new image
    encoded_img = Image.new('RGB', (width, height))
    encoded_img.putdata(new_pixels)
    output = io.BytesIO()
    encoded_img.save(output, format='PNG')
    return output.getvalue()

def decode_image(image):
    # Convert to RGB
    img = image.convert('RGB')
    pixels = list(img.getdata())
    
    # Extract LSB from each color channel
    bit_stream = []
    for r, g, b in pixels:
        bit_stream.append(r & 1)
        bit_stream.append(g & 1)
        bit_stream.append(b & 1)
    
    # Convert to bit string
    bit_string = ''.join(str(bit) for bit in bit_stream)
    
    # Extract header (first 32 bits)
    if len(bit_string) < 32:
        raise ValueError("Invalid image format")
    header_bits = bit_string[:32]
    
    # Convert header to message length
    header_bytes = [int(header_bits[i*8:(i+1)*8], 2) for i in range(4)]
    message_len = struct.unpack('>I', bytes(header_bytes))[0]
    
    # Extract message bits
    start_idx = 32
    end_idx = start_idx + message_len * 8
    if end_idx > len(bit_string):
        raise ValueError("Message corrupted or incomplete")
    message_bits = bit_string[start_idx:end_idx]
    
    # Convert to bytes
    message_bytes = bytearray()
    for i in range(0, len(message_bits), 8):
        byte_bits = message_bits[i:i+8]
        message_bytes.append(int(byte_bits, 2))
    
    return message_bytes.decode('utf-8', errors='replace')

# Streamlit App
st.title("Steganography: Hide Messages in Images")

operation = st.radio("Choose Operation", ["Encode", "Decode"])

if operation == "Encode":
    st.header("Encode a Message")
    uploaded_image = st.file_uploader("Upload an Image (PNG)", type=["png"])
    message = st.text_area("Enter the message to hide")
    
    if st.button("Encode and Download"):
        if uploaded_image and message:
            image = Image.open(uploaded_image)
            try:
                encoded_image = encode_image(image, message)
                st.success("Message encoded successfully!")
                st.download_button("Download Encoded Image", encoded_image, file_name="encoded_image.png", mime="image/png")
            except ValueError as e:
                st.error(f"Error: {e}")

elif operation == "Decode":
    st.header("Decode a Message")
    uploaded_image = st.file_uploader("Upload an Encoded Image (PNG)", type=["png"])
    
    if st.button("Decode Message"):
        if uploaded_image:
            image = Image.open(uploaded_image)
            try:
                decoded_message = decode_image(image)
                st.success("Message decoded successfully!")
                st.text_area("Decoded Message", decoded_message, height=200, disabled=True)
            except ValueError as e:
                st.error(f"Error: {e}")
