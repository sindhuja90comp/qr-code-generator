"""
QR Code Generator
Author: Sindhuja Martha
Description: This script generates a QR code for a given URL and saves it as an image.
"""

import qrcode

def generate_qr(url: str, filename: str = "qrcode.png"):
    """
    Generates a QR code for the given URL and saves it as an image file.
    
    Args:
        url (str): The URL to be encoded in the QR code.
        filename (str): The name of the output file (default: 'qrcode.png').
    """
    # Create qr object
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        box_size=10,  
        border=4,  
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code generated and saved as {filename}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print(" 🔹 WELCOME TO THE QR CODE GENERATOR 🔹 ")
    print("="*50 + "\n")
    print("This program will generate a QR code for any text or URL you provide.\n")
    
    input_url = input("👉 Enter the text or URL to generate QR Code: ")
    generate_qr(input_url, "my_qrcode.png")
