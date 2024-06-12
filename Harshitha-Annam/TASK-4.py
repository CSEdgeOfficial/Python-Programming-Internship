# import necessary libraries
from PIL import Image
import os


def get_size_format(b, factor = 1024, suffix = 'B'):
    """
    Scale bytes to its proper byte format.
    e.g, 1253656 => '1.20MB', 1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
    

def compress_image(image_path, new_size_ratio = 0.9, quality = 90, width = None, height = None, to_jpg = True):
    try:
        # load image into memory
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return 

    # print the original image shape
    print("[*] Original Image Shape: ", img.size)

    # get original image size in bytes
    try:
        image_size = os.path.getsize(image_path)
        print("[*] Size before compression: ", get_size_format(image_size))
    except Exception as e :
        print(f"Error getting image size: {e}")
        return

    # resize the image if necessary
    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
    elif width and height:
        img = img.resize((width, height), Image.LANCZOS)

    # split the filename and extension
    filename, ext = os.path.splitext(image_path)

    # make new file name appending compressed to the original file name
    new_name = f"{filename}_compressed.jpg" if to_jpg else f"{filename}_compressed.{ext}"


    # save the compressed image
    try:
        img.save(new_name, optimize = True, quality = quality)
    except Exception as e :
        print(f"Error saving compressed file: {e}")
        return 

    # print the new image shape
    print("[+] New Image Shape:", img.size)

    try:
        # get new image size in bytes
        new_img_size = os.path.getsize(new_name)
        print("[*] Size after compression:", get_size_format(new_img_size))
        print(f"[*] Compressed image saved as: {new_name}")
    except Exception as e:
        print(f"Error getting new image size: {e}")

# Example usage
if __name__ == "__main__":
    image_path = input("Enter the path of the image to compress: ")
    compress_image(image_path, new_size_ratio=0.8, quality=80, width=800, height=600)
    