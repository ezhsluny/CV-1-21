"""
Image Compression

This script demonstrates image compression at different quality levels,
displays a comparison collage, and calculates file size statistics.
"""

import os
import cv2


def get_file_size(filename):
    """
    Get the size of a file in bytes.

    Args:
        filename (str): Path to the file

    Returns:
        int: File size in bytes
    """
    return os.path.getsize(filename)

def change_quality(filename, quality_list):
    """
    Compress image at different quality levels and collect results.
    
    Args:
        filename (str): Path to the source image file
        quality_list (list): List of quality percentages for compression
        
    Returns:
        list: List of images including original and compressed versions
    """
    # Load the original image
    img = cv2.imread(filename)
    if img is None:
        print("Error: failed to open image")
        exit()
    
    # Initialize dictionary for storing file sizes
    file_sizes = {}
    processed_images = [img.copy()]

    # Process original image - get its file size
    original_size = get_file_size(filename)
    file_sizes['100%'] = original_size
    
    # Process each compression level in the quality list
    for quality in quality_list:
        # Generate filename for compressed image
        compressed_filename = f'CV-1-21/images/compressed_{quality}percent.jpg'
        
        # Save image with specified JPEG quality
        cv2.imwrite(compressed_filename, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
        print(f"Saved: {compressed_filename}")

        # Calculate compression statistics
        file_size = get_file_size(compressed_filename)
        file_sizes[f'{quality}%'] = file_size
        
        # Load the compressed image for collage display
        compressed_img = cv2.imread(compressed_filename)
        processed_images.append(compressed_img)
        
    # Print file sizes for all processed images (original + compressed)
    print("File sizes (quality %: size in bytes)\n", file_sizes)

    return processed_images

def main():
    # Path to the original image file
    orig_file = '/home/ezhsluny/Documents/iir_proj/CV-1-21/images/test.jpg'

    # Compression quality levels to test
    quality_list = [95, 50, 10]

    # Generate compressed images and collect them for collage
    images_for_collage = change_quality(orig_file, quality_list)
    
    # --- Optional visualization ---
    # Create horizontal collage by concatenating all images
    collage = cv2.hconcat(images_for_collage)
    
    # Display the comparison collage
    cv2.imshow('Image Compression Comparison', collage)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()