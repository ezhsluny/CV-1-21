# CV-1-21
# Image compression

## File structure
- Script `quality.py` performs image compression at different quality levels, displays a comparison collage, and calculates file size statistics
- Folder `images` contains test and compressed images


## Description
A Python script that demonstrates image compression at different quality levels. The tool allows you to:
- Compress images with various JPEG quality settings
- Create a visual comparison collage of results
- Calculate and display file size statistics

## Features
- Command-line interface with flexible arguments
- Image loading and processing using OpenCV
- Multiple compression levels (95%, 50%, 10% quality)
- File size calculation before and after compression
- Visual comparison collage with quality labels on each image
- Input validation for file existence and quality values

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy` - dependency of OpenCV)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone or download the script to your local machine
2. Install the required dependencies as shown above
3. Prepare your test image

## Usage
1. **Prepare Your Image**:
   - Place your test image in a convenient directory

2. **Run the Script**:
   ```bash
   python3 quality.py [-h] [-o OUTPUT_DIR] input_image

   # Compress an image with default output directory
   python3 quality.py input_image.jpg

   # Compress with custom output directory
   python3 quality.py input_image.jpg -o my_compressed_images
   ```

3. **View Results**:
   - File sizes for each quality level will be displayed in the console
   - A window will open showing the comparison collage
   - Press any key to close the window

4. **Customize Parameters**:
   - Modify the `quality_list` in the `main()` function for different quality levels

## Example Output Files
After running the script, the following files will be created in the output directory:
- `compressed_images/test_compressed_95percent.jpg` - High quality compression
- `compressed_images/test_compressed_50percent.jpg` - Medium quality compression
- `compressed_images/test_compressed_10percent.jpg` - Low quality compression