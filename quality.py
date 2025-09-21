"""
Image Compression

This script demonstrates image compression at different quality levels,
displays a comparison collage, and calculates file size statistics.
"""

import os
import cv2
import argparse


def get_file_size(filename):
    """
    Get the size of a file in bytes.

    Args:
        filename (str): Path to the file

    Returns:
        int: File size in bytes

    Raises:
        FileNotFoundError: If the file does not exist
        OSError: If there are issues accessing the file
    """
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except OSError as e:
        raise OSError(f"Error accessing file {filename}: {e}")


def validate_quality_values(quality_list):
    """
    Validate quality values to ensure they are within valid range (0-100).
    
    Args:
        quality_list (list): List of quality values to validate
        
    Raises:
        ValueError: If any quality value is not in range 0-100
    """
    for quality in quality_list:
        if not 0 <= quality <= 100:
            raise ValueError(f"Quality value {quality} is not in valid range (0-100)")


def change_quality(filename, quality_list, output_dir='CV-1-21/images'):
    """
    Compress image at different quality levels and collect results.
    
    Args:
        filename (str): Path to the source image file
        quality_list (list): List of quality percentages for compression
        output_dir (str): Directory to save compressed images
        
    Returns:
        dict: Dictionary containing processed images and file sizes
        
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If quality values are invalid
        Exception: For other processing errors
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Input file not found: {filename}")
    
    # Validate file is an image
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        print(f"Warning: {filename} may not be a supported image format")

    validate_quality_values(quality_list)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the original image
    img = cv2.imread(filename)
    if img is None:
        raise ValueError(f"Failed to read image file: {filename}")
    
    # Initialize results dictionary
    results = {
        'images': [img.copy()],
        'file_sizes': {},
        'compressed_filenames': []
    }
    
    # Process original image - get its file size
    try:
        original_size = get_file_size(filename)
        results['file_sizes']['100%'] = original_size
    except (FileNotFoundError, OSError) as e:
        raise e

    # Process each compression level in the quality list
    for quality in quality_list:
        compressed_filename = os.path.join(output_dir, f'compressed_{quality}percent.jpg')
        results['compressed_filenames'].append(compressed_filename)
        
        try:
            # Save image with specified JPEG quality
            success = cv2.imwrite(compressed_filename, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
            if not success:
                raise RuntimeError(f"Failed to save image: {compressed_filename}")
            
            file_size = get_file_size(compressed_filename)
            results['file_sizes'][f'{quality}%'] = file_size
            
            # Load the compressed image for collage display
            compressed_img = cv2.imread(compressed_filename)
            if compressed_img is None:
                raise RuntimeError(f"Failed to read compressed image: {compressed_filename}")
            
            # Add labels of quality on processed images
            compressed_img = cv2.putText(compressed_img, f"{quality}%", (10, 50),
                                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                                         3)
            results['images'].append(compressed_img)
            
        except Exception as e:
            # Clean up partially created files
            if os.path.exists(compressed_filename):
                os.remove(compressed_filename)
            raise e

    return results

def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(description='Image compression tool with quality comparison')
    
    parser.add_argument('input_image', 
                       help='Path to the input image file')
    
    parser.add_argument('-o', '--output-dir', 
                       default='images',
                       help='Output directory for compressed images (default: compressed_images)')
    
    return parser.parse_args()


def main():
    try:
        # Parse command line arguments
        args = parse_arguments()

        print(f"Processing image: {args.input_image}")
        print(f"Output directory: {args.output_dir}")
        
        # Compression quality levels to test
        quality_list = [95, 50, 10]

        results = change_quality(args.input_image, quality_list, args.output_dir)
        
        # Print file sizes
        print("File sizes (quality %: size in bytes)")
        for quality, size in results['file_sizes'].items():
            print(f"{quality}: {size} bytes")
        
        # --- Optional visualization ---
        # Create horizontal collage by concatenating all images
        collage = cv2.hconcat(results['images'])
        
        cv2.imshow('Image Compression Comparison', collage)  
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()