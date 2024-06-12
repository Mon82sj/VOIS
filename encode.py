from PIL import Image

def embed_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    message += '####'  # Delimiter to signify end of message
    message_bits = ''.join([format(ord(i), '08b') for i in message])

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                if data_index < len(message_bits):
                    pixel[n] = pixel[n] & ~1 | int(message_bits[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))

    encoded.save(output_path)

# Usage
embed_message('W1.jpg', 'Your Image is Encrypted', 'W12.png')
