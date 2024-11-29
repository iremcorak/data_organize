# Data Organize

This repository contains Python scripts designed to organize and filter datasets containing image and XML annotation pairs. These tools are particularly useful for managing labeled datasets used in machine learning and computer vision projects.

## Scripts Overview

### 1. `organize_images_by_label.py`

This script organizes image and XML files into subdirectories based on the label (`<name>`) specified in the XML files.

#### Features:
- Scans a source directory for `.png` or `.jpg` images and their corresponding `.xml` files.
- Extracts the `<name>` tag from each XML file.
- Creates subdirectories named after the extracted label.
- Moves image and XML files into the appropriate subdirectory.
- Handles duplicate file overwrites with informative messages.

#### Usage:
1. Specify the source directory containing the image-XML pairs (`root_directory`).
2. Specify the output directory where labeled subdirectories will be created (`output_directory`).
3. Run the script.
