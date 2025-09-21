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
- Image loading and processing using OpenCV
- Multiple compression levels (95%, 50%, 10% quality)
- File size calculation before and after compression
- Horizontal collage creation for visual comparison

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)

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
   - Place your test image in the `CV-1-21/images/` directory
   - Name the file `test.jpg` or modify the path in the code

2. **Run the Script**:
   ```bash
   python3 image_compression.py
   ```

3. **View Results**:
   - File sizes for each quality level will be displayed in the console
   - A window will open showing the comparison collage
   - Press any key to close the window

4. **Customize Parameters**:
   - Modify the `quality_list` in the `main()` function for different quality levels
   - Change the `orig_file` path to use a different image
   - Change the `output_dir` path to use a different directory to store processed images

## Example Output Files
After running the script, the following files will be created in `CV-1-21/images/`:
- `compressed_95percent.jpg` - High quality compression
- `compressed_50percent.jpg` - Medium quality compression
- `compressed_10percent.jpg` - Low quality compression