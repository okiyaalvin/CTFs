from PIL import Image

# Load the image
img = Image.open("stego_rabbit.png")  # Replace with your filename
pixels = img.load()

width, height = img.size

bits = []

# Loop over the first few pixels (let's say 200 for a short message)
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y][:3]
        bits.append(b & 1)  # Get the LSB of the blue channel

        # Stop after enough bits (e.g., 8 bits × 100 characters)
        if len(bits) >= 8 * 100:
            break
    if len(bits) >= 8 * 100:
        break

# Group into bytes
chars = []
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) < 8:
        continue
    char = chr(int(''.join(map(str, byte)), 2))
    if char == '\x00':  # Null terminator (common end of message)
        break
    chars.append(char)

message = ''.join(chars)
print("Hidden message:", message)

