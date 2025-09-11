"""
Image Compression

This script demonstrates image compression at different quality levels,
displays a comparison collage, and calculates file size statistics.
"""

import os
import cv2
import numpy as np


def resizing(img, qual):
    """
    Resize an image by a given quality percentage.

    Args:
        img (numpy.ndarray): Input image to be resized
        qual (int): Quality percentage for resizing (1-100)

    Returns:
        numpy.ndarray: Resized image using nearest neighbor interpolation
    """
    img_h, img_w = img.shape[:2] # Height and width of original image
    new_w = int(img_w*qual/100) # Height and width for resizing
    new_h = int(img_h*qual/100)
    res_img = cv2.resize(img, (new_w, new_h), cv2.INTER_NEAREST)

    return res_img

def center_image(orig_img, compr_img):
    """
    Center a compressed image on a black background of original dimensions 
    for further convinient visualisation.

    Args:
        orig_img (numpy.ndarray): Original image for dimensions
        compr_img (numpy.ndarray): Compressed image to be centered

    Returns:
        numpy.ndarray: Image with compressed content centered on black background
    """
    h, w = orig_img.shape[:2] # Height and width of original image
    comp_h, comp_w = compr_img.shape[:2] # Height and width of compressed image
    
    # Black background with original image dimensions
    black_background = np.zeros((h, w, 3), dtype=np.uint8)
    
    # Calculate center position for the compressed image
    x_center = (w - comp_w) // 2
    y_center = (h - comp_h) // 2
    
    # Place compressed image at the center
    black_background[y_center:y_center+comp_h, x_center:x_center+comp_w] = compr_img
    
    return black_background

def get_file_size(filename):
    """
    Get the size of a file in bytes.

    Args:
        filename (str): Path to the file

    Returns:
        int: File size in bytes
    """
    return os.path.getsize(filename)

def main():
    # Path to the original image
    orig_file = 'CV-1-21/images/test.jpg'
    
    img = cv2.imread(orig_file)
    if img is None:
        print("Error: failed to open image")
        exit()
    
    # Initialize lists and dictionaries for storing results
    centered_images = []
    file_sizes = {}

    # Process original image
    original_size = get_file_size(orig_file)
    file_sizes['100%'] = original_size
    centered_images.append(img)  # Add original image to comparison list

    # Compression levels
    quality_list = [95, 50, 10]
    
    # Process each compression level
    for quality in quality_list:
        # Resize image
        compr_img = resizing(img, quality)
        
        # Center the compressed image
        centered_img = center_image(img, compr_img)
        centered_images.append(centered_img)

        # Save the compressed image
        filename = f'CV-1-21/images/compressed_{quality}percent.jpg'
        cv2.imwrite(filename, compr_img)
        print(f"Saved: {filename}")

        # Calculate compression statistics
        file_size = get_file_size(filename)
        file_sizes[f'{quality}%'] = file_size
        
    # Print file sizes for all processed images
    print("File sizes (quality %: size in bytes)\n", file_sizes)

    # Create a horizontal collage of all images for visual comparison
    collage = cv2.hconcat(centered_images)

    cv2.imshow('Images Comparison', collage)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()