from PIL import Image

def extract_message(image_path):
    image = Image.open(image_path)
    width, height = image.size
    bits = []

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            for n in range(3):
                bits.append(pixel[n] & 1)

    message_bits = ''.join([str(bit) for bit in bits])
    message_bytes = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in message_bytes])
    return message.split('####')[0]

# Usage
hidden_message = extract_message('W12.png')
print(hidden_message)
