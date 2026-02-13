from PIL import Image
import sys
import os
import random

def resize_image(input_path, output_path=None):
    # Open the image
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return False
    
    # Generate random dimensions between 64x64 and 100x100
    new_width = random.randint(64, 100)
    new_height = random.randint(64, 100)
    
    # Resize the image 
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Create output path if not provided
    if output_path is None:
        filename, ext = os.path.splitext(input_path)
        output_path = f"{filename}_resized_{new_width}x{new_height}{ext}"
    
    # Save the resized image
    try:
        resized_img.save(output_path)
        print(f"Image resized to {new_width}x{new_height} and saved as {output_path}")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python resize_image.py input_image.jpg [output_image.jpg]")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        resize_image(input_path, output_path) 