# QR Code Generator

## Description
This project is a simple QR code generator built with Python. It allows users to create QR codes containing text, URLs, or any other information that can be encoded as a QR code.

## Features
- Generate QR codes for any text or URL
- Save QR codes as images (PNG, JPG, etc.)
- Customizable QR code design (size, color, etc.)

## Installation
Make sure you have Python installed. Then install the required package:
```bash
pip install qrcode[pil]
```

## Usage
Here’s a basic example:
```python
import qrcode

# Create instance of QRCode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code
qr.add_data('https://example.com')
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save('qrcode.png')
```

## Example
```python
# Generate a QR Code for 'Hello, World!'
import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data('Hello, World!')
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('hello_world_qr.png')
```
