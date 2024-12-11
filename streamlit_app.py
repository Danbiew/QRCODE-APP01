import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(data, box_size=10, border=4):
    """
    Generate a QR code from the input data.
    
    :param data: String to be encoded in the QR code
    :param box_size: Size of each box in the QR code
    :param border: Size of the border around the QR code
    :return: PIL Image of the QR code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image

def main():
    st.title("🔳 QR Code Generator")
    
    # Input for QR code content
    qr_content = st.text_input("Enter the content for your QR Code", 
                                placeholder="URL, text, contact info...")
    
    # Customization options
    col1, col2 = st.columns(2)
    with col1:
        box_size = st.slider("QR Code Box Size", min_value=5, max_value=20, value=10)
    with col2:
        border_size = st.slider("Border Size", min_value=1, max_value=10, value=4)
    
    # Generate QR Code button
    if st.button("Generate QR Code"):
        if qr_content:
            try:
                # Generate QR Code
                qr_image = generate_qr_code(qr_content, box_size, border_size)
                
                # Display QR Code
                st.image(qr_image, caption="Generated QR Code", use_column_width=True)
                
                # Download option
                buffered = io.BytesIO()
                qr_image.save(buffered, format="PNG")
                qr_bytes = buffered.getvalue()
                
                st.download_button(
                    label="Download QR Code",
                    data=qr_bytes,
                    file_name="qr_code.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"Error generating QR Code: {e}")
        else:
            st.warning("Please enter some content for the QR Code")

if __name__ == "__main__":
    main()
