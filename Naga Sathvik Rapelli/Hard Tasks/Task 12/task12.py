from PIL import Image
import os

def compress_image(input_path, output_path, quality=60):
    """
    Compresses an input image while maintaining quality.

    Parameters:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image file.
        quality (int): Compression quality (0 - 95). Default is 60.
    
    Returns:
        None
    """
    input_image = Image.open(input_path)

    if input_image.mode == 'RGBA':
        input_image = input_image.convert('RGB')

    compressed_image = input_image.copy()
    compressed_image.save(output_path, quality=quality)

    print(f"Compressed image saved at: {output_path}")

def main():
    input_path = 'C:/Users/SATHVIK/OneDrive/Desktop/Motive.png'
    output_folder = 'compressed_images'
    os.makedirs(output_folder, exist_ok=True) 

    quality = 60

    # Compress image
    output_path = os.path.join(output_folder, 'compressed_image.jpg')
    compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    main()

