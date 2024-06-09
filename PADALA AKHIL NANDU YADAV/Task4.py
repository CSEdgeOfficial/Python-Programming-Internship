from PIL import Image
import os

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format.
    e.g: 1253656 => '1.20MB', 1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    # Print the file path for debugging
    print(f"[*] Attempting to open file: {image_name}")
    
    # Load the image into memory
    img = Image.open(image_name)

    # Print the original image shape
    print("[*] Image shape:", img.size)

    # Get the original image size in bytes
    image_size = os.path.getsize(image_name)
    print("[*] Size before compression:", get_size_format(image_size))

    if new_size_ratio < 1.0:
        # If resizing ratio is below 1.0, multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
    elif width and height:
        # If width and height are set, resize with them instead
        img = img.resize((width, height), Image.LANCZOS)

    # Split the filename and extension
    filename, ext = os.path.splitext(image_name)

    # Convert RGBA to RGB if saving as JPEG
    if to_jpg and img.mode == 'RGBA':
        img = img.convert('RGB')

    # Make a new filename appending "_compressed" to the original file name
    if to_jpg:
        # Change the extension to JPEG
        new_filename = f"{filename}_compressed.jpg"
    else:
        # Retain the same extension of the original image
        new_filename = f"{filename}_compressed{ext}"

    # Save the compressed image
    img.save(new_filename, optimize=True, quality=quality)

    # Print the new image shape
    print("[+] New Image shape:", img.size)
    print(f"[*] Compressed image saved as: {new_filename}")

# Example usage:
compress_img(r"C:\Users\sarayu sree\Pictures\Picture1.png", new_size_ratio=0.8, quality=80, width=800, height=600)
