from PIL import Image
import os

def get_size_format(bytes_, factor=1024, suffixes=["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB"]):
  """
  Scales bytes to its proper byte format with IEC binary prefixes.

  Args:
      bytes_: The size in bytes to format.
      factor (int, optional): The base unit for scaling (default: 1024).
      suffixes (list, optional): The list of suffixes to use (default: IEC binary prefixes).

  Returns:
      str: The formatted size string (e.g., 1.20 MiB).
  """

  for suffix in suffixes:
    if bytes_ < factor:
      return f"{bytes_:.2f}{suffix}"
    bytes_ /= factor
  return f"{bytes_:.2f}{suffixes[-1]}"  # Use the last suffix for large sizes

def compress_image(image_path, output_path=None, new_size_ratio=0.9, quality=90, max_width=None, max_height=None, to_jpeg=True):
  """
  Compresses an image with resizing and quality adjustments.

  Args:
      image_path (str): Path to the image file to compress.
      output_path (str, optional): Path to save the compressed image. If not provided, a new filename with "_compressed" is generated next to the original image.
      new_size_ratio (float, optional): Ratio to reduce the image size (default: 0.9).
      quality (int, optional): JPEG quality for saving (default: 90).
      max_width (int, optional): Maximum width for resizing (default: None).
      max_height (int, optional): Maximum height for resizing (default: None).
      to_jpeg (bool, optional): Whether to convert the output to JPEG format (default: True).

  Raises:
      ValueError: If both output_path and to_jpeg are False.
  """

  # Load the image
  try:
    img = Image.open(image_path)
  except FileNotFoundError:
    print(f"Error: Image file not found - {image_path}")
    return

  # Print original image details
  print(f"[*] Image: {image_path}")
  print(f"[*] Original size: {img.size}")

  # Get original image size in bytes
  image_size = os.path.getsize(image_path)
  print(f"[*] Size before compression: {get_size_format(image_size)}")

  # Resizing logic
  if new_size_ratio < 1.0:
    new_size = (int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio))
  elif max_width and max_height:
    new_size = (min(max_width, img.size[0]), min(max_height, img.size[1]))
  else:
    new_size = img.size  # No resizing if no ratio or dimensions provided

  if new_size != img.size:
    img = img.resize(new_size, Image.ANTIALIAS)

  # Generate output filename
  if not output_path:
    filename, ext = os.path.splitext(image_path)
    new_filename = f"{filename}_compressed{ext}" if to_jpeg else f"{filename}_compressed{ext}"
  else:
    new_filename = output_path

  # Validate output format
  if not to_jpeg and not new_filename.lower().endswith((".png", ".bmp", ".gif")):
    print("Warning: Output format not supported. Keeping the original format.")

  # Save the compressed image
  img.save(new_filename, optimize=True, quality=quality)

  # Print results
  print(f"[+] New size: {img.size}")
  print(f"[+] Compressed image saved as: {new_filename}")

# Example usage
image_path = input("Enter the image path: ")
compress_image(image_path)
