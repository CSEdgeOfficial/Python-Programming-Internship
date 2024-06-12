# Import all the necessary libraries 
from PIL import Image
import os
# PIL is for opening, manipulating and saving images in different formats
# os is for handling file paths


# a function for handling the conversion of image formats
def convert_image(input_path, output_path, output_format):


    try:
        # opening and saving the input image
        with Image.open(input_path) as img:
            img.save(output_path, format = output_format)
            

    # handling any possible exceptions
    except Exception as e:
        print(f"Error: {e}")


# main function
def main():

    # get input file/image path from user
    input_path = input("Enter the input Image Path:")


    # checking if the input file exists
    if not os.path.exists(input_path):
        print("The input file/image does not exist.")
        return
    

    # if input file/image exists ask user for the output format
    output_format = input("Enter the desired output format(eg., JPEG, PNG, BMP, GIF):").upper()


    # create a list for valid output formats
    valid_formats = ['JPEG', 'PNG', 'BMP', 'GIF']


    # validate the desired output format given by the user
    if output_format not in valid_formats:
        print("Invalid output format. Please choose a valid format(eg., JPEG, PNG, BMP, GIF)")
        return


    # extract the file name without file extension
    file_name_without_ext, ext_name = os.path.splitext(input_path)


    #  set the output image path
    output_path = f"{file_name_without_ext}_converted.{output_format.lower()}"


    # call the convert_image function and pass the arguments
    convert_image(input_path, output_path, output_format)


if __name__ == "__main__":
    main()