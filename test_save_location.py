#!/usr/bin/env python3
"""
Test script to verify that HTML files are saved to the correct location.
This script simulates what the notebook does, but runs from a different directory
to ensure that the absolute path handling works correctly.
"""

import os
import sys
import datetime

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Import the utility functions
from shared.html_utils import convert_bottom_to_top, save_html_to_file, save_original_html

# Simple HTML example
example_html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta charset="utf-8" />
</head>
<body>
    <style>
        #t1{left:18px;bottom:804px;}
        #t2{left:128px;bottom:804px;}
    </style>
    <div class="text-container">
        <span id="t1">Test</span>
        <span id="t2">Test 2</span>
    </div>
</body>
</html>
"""

def main():
    """Main function to test the save location."""
    print(f"Current working directory: {os.getcwd()}")
    
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Save original HTML
    original_path = save_original_html(example_html, timestamp)
    print(f"Original path: {original_path}")
    print(f"Original file exists: {os.path.exists(original_path)}")
    
    # Convert HTML
    converted_html = convert_bottom_to_top(example_html)
    
    # Save converted HTML
    output_path = save_html_to_file(converted_html, "test_convert", timestamp)
    print(f"Output path: {output_path}")
    print(f"Output file exists: {os.path.exists(output_path)}")
    
    # Verify that the files are saved to the correct location
    expected_original_path = os.path.join(project_root, "data", "original", f"original_{timestamp}.html")
    expected_output_path = os.path.join(project_root, "data", "output", f"test_convert_{timestamp}.html")
    
    print(f"Expected original path: {expected_original_path}")
    print(f"Original path matches expected: {original_path == expected_original_path}")
    
    print(f"Expected output path: {expected_output_path}")
    print(f"Output path matches expected: {output_path == expected_output_path}")

if __name__ == "__main__":
    main()