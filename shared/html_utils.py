"""
Utility functions for HTML to JasperReport conversion.

This module contains reusable functions for parsing, manipulating, and converting HTML files.
"""

import re
import os
import datetime
from shared.constants import HTML_HEIGHT

# Try to import BeautifulSoup, but don't fail if it's not installed
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Warning: BeautifulSoup is not installed. Some functions may not work.")
    # Define a placeholder for BeautifulSoup to avoid syntax errors
    class BeautifulSoup:
        def __init__(self, *args, **kwargs):
            pass

def parse_html(html_code):
    """
    Parse HTML code with BeautifulSoup.
    
    Args:
        html_code (str): The HTML code to parse
        
    Returns:
        BeautifulSoup: The parsed HTML document
    """
    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error parsing HTML code: {e}")
        return None

def extract_css_styles(soup):
    """
    Extract CSS styles from the HTML document.
    
    Args:
        soup (BeautifulSoup): The parsed HTML document
        
    Returns:
        dict: A dictionary with element IDs as keys and styles as values
    """
    styles = {}
    
    # Extract styles from style tags
    style_tags = soup.find_all('style')
    for style_tag in style_tags:
        css_content = style_tag.string
        if css_content:
            # Regex to extract selectors and their styles
            style_matches = re.findall(r'#([\w]+)\s*{([^}]+)}', css_content)
            for selector, style_text in style_matches:
                # Convert styles to a dictionary
                style_dict = {}
                style_parts = style_text.split(';')
                for part in style_parts:
                    if ':' in part:
                        prop, value = part.split(':', 1)
                        style_dict[prop.strip()] = value.strip()
                styles[selector] = style_dict
    
    return styles

def extract_elements(soup):
    """
    Extract relevant elements from the HTML document.
    
    Args:
        soup (BeautifulSoup): The parsed HTML document
        
    Returns:
        dict: A dictionary with element types as keys and lists of elements as values
    """
    elements = {
        'div': soup.find_all('div'),
        'table': soup.find_all('table'),
        'img': soup.find_all('img'),
        'p': soup.find_all('p'),
        'span': soup.find_all('span')
    }
    
    return elements

def convert_bottom_to_top(html_string, offset_x=0, offset_y=0):
    """
    Convert bottom-positioned elements to top-positioned elements in HTML.
    
    Args:
        html_string (str): The HTML string containing bottom-positioned elements
        offset_x (int, optional): Horizontal offset to apply to left values (positive = right, negative = left). Defaults to 0.
        offset_y (int, optional): Vertical offset to apply to top values (positive = down, negative = up). Defaults to 0.
    
    Returns:
        str: The modified HTML string with bottom positions converted to top positions
    """
    # Define a pattern to find CSS rules with bottom property
    pattern = r'([^{]+)\{([^}]+)\}'
    
    # Define a function to replace bottom with top in CSS rules
    def replace_css_rule(match):
        selector = match.group(1)
        properties = match.group(2)
        
        # Find bottom property
        bottom_match = re.search(r'bottom:(\d+\.?\d*)px', properties)
        if bottom_match:
            bottom_px = float(bottom_match.group(1))
            # Calculate top value: top = HTML_HEIGHT - bottom
            top_px = HTML_HEIGHT - bottom_px
            
            # Apply vertical offset if provided
            if offset_y != 0:
                top_px += offset_y
            
            # Replace bottom with top
            properties = re.sub(r'bottom:(\d+\.?\d*)px', f'top:{top_px:.0f}px', properties)
        
        # Apply horizontal offset to left property if provided
        if offset_x != 0:
            left_match = re.search(r'left:(\d+\.?\d*)px', properties)
            if left_match:
                left_px = float(left_match.group(1))
                new_left_px = left_px + offset_x
                properties = re.sub(r'left:(\d+\.?\d*)px', f'left:{new_left_px:.0f}px', properties)
        
        return f'{selector}{{{properties}}}'
    
    # Find all style tags in the HTML
    style_pattern = r'<style[^>]*>(.*?)</style>'
    
    # Function to process style content
    def process_style(style_match):
        style_tag_start = style_match.group(0).split('>')[0] + '>'
        style_content = style_match.group(1)
        
        # Apply the CSS rule replacement
        new_style_content = re.sub(pattern, replace_css_rule, style_content)
        
        return f"{style_tag_start}{new_style_content}</style>"
    
    # Replace style tags with processed content
    result_html = re.sub(style_pattern, process_style, html_string, flags=re.DOTALL)
    
    return result_html

def apply_offset(html_string, offset_x=0, offset_y=0):
    """
    Apply offset to left and top values in HTML.
    
    Args:
        html_string (str): The HTML string to modify
        offset_x (int, optional): Horizontal offset to apply to left values (positive = right, negative = left). Defaults to 0.
        offset_y (int, optional): Vertical offset to apply to top values (positive = down, negative = up). Defaults to 0.
    
    Returns:
        str: The modified HTML string with offsets applied
    """
    # If no offset is provided, return the original HTML
    if offset_x == 0 and offset_y == 0:
        return html_string
    
    # Define a pattern to find CSS rules
    pattern = r'([^{]+)\{([^}]+)\}'
    
    # Define a function to apply offsets to CSS rules
    def apply_offset_to_rule(match):
        selector = match.group(1)
        properties = match.group(2)
        
        # Apply horizontal offset to left property
        if offset_x != 0:
            left_match = re.search(r'left:(\d+\.?\d*)px', properties)
            if left_match:
                left_px = float(left_match.group(1))
                new_left_px = left_px + offset_x
                properties = re.sub(r'left:(\d+\.?\d*)px', f'left:{new_left_px:.0f}px', properties)
        
        # Apply vertical offset to top property
        if offset_y != 0:
            top_match = re.search(r'top:(\d+\.?\d*)px', properties)
            if top_match:
                top_px = float(top_match.group(1))
                new_top_px = top_px + offset_y
                properties = re.sub(r'top:(\d+\.?\d*)px', f'top:{new_top_px:.0f}px', properties)
        
        return f'{selector}{{{properties}}}'
    
    # Find all style tags in the HTML
    style_pattern = r'<style[^>]*>(.*?)</style>'
    
    # Function to process style content
    def process_style(style_match):
        style_tag_start = style_match.group(0).split('>')[0] + '>'
        style_content = style_match.group(1)
        
        # Apply the CSS rule replacement
        new_style_content = re.sub(pattern, apply_offset_to_rule, style_content)
        
        return f"{style_tag_start}{new_style_content}</style>"
    
    # Replace style tags with processed content
    result_html = re.sub(style_pattern, process_style, html_string, flags=re.DOTALL)
    
    return result_html

def extract_positions(html_string):
    """
    Extract position information (top/left) from HTML elements.
    
    Args:
        html_string (str): The HTML string to extract positions from
    
    Returns:
        list: A list of dictionaries with element IDs and their positions
    """
    positions = []
    
    # Parse the HTML
    soup = parse_html(html_string)
    if not soup:
        return positions
    
    # Extract CSS styles
    css_styles = extract_css_styles(soup)
    
    # Extract positions from CSS styles
    for element_id, style_dict in css_styles.items():
        position = {'id': element_id}
        
        if 'left' in style_dict:
            match = re.search(r'(\d+\.?\d*)px', style_dict['left'])
            if match:
                position['left'] = float(match.group(1))
        
        if 'top' in style_dict:
            match = re.search(r'(\d+\.?\d*)px', style_dict['top'])
            if match:
                position['top'] = float(match.group(1))
        
        if 'bottom' in style_dict:
            match = re.search(r'(\d+\.?\d*)px', style_dict['bottom'])
            if match:
                position['bottom'] = float(match.group(1))
        
        positions.append(position)
    
    return positions

def load_html_from_file(file_path):
    """
    Load HTML from a file.
    
    Args:
        file_path (str): The path to the HTML file
    
    Returns:
        str: The HTML string loaded from the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""

def save_html_to_file(html_string, function_name="converted", timestamp=None):
    """
    Save HTML string to a file with a timestamp in the filename.
    
    Args:
        html_string (str): The HTML string to save
        function_name (str, optional): The name of the function to include in the filename. 
                                      Defaults to "converted".
        timestamp (str, optional): A custom timestamp to use in the filename.
                                  If None, the current time will be used.
    
    Returns:
        str: The path to the saved file
    """
    # Create output directory if it doesn't exist
    output_dir = "data/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp if not provided
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Create filename
    filename = f"{function_name}_{timestamp}.html"
    file_path = os.path.join(output_dir, filename)
    
    # Save the HTML to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_string)
    
    print(f"HTML saved to: {file_path}")
    return file_path

def save_original_html(html_string, timestamp=None):
    """
    Save the original HTML string to a file in the original directory.
    
    Args:
        html_string (str): The original HTML string to save
        timestamp (str, optional): A custom timestamp to use in the filename.
                                  If None, the current time will be used.
    
    Returns:
        str: The path to the saved file
    """
    # Create original directory if it doesn't exist
    original_dir = "data/original"
    os.makedirs(original_dir, exist_ok=True)
    
    # Generate timestamp if not provided
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Create filename
    filename = f"original_{timestamp}.html"
    file_path = os.path.join(original_dir, filename)
    
    # Save the HTML to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_string)
    
    print(f"Original HTML saved to: {file_path}")
    return file_path

def batch_convert_folder(input_folder="data/original", output_folder="data/output", 
                         conversion_function=convert_bottom_to_top, **kwargs):
    """
    Batch convert all HTML files in a folder.
    
    Args:
        input_folder (str, optional): The folder containing HTML files to convert. 
                                     Defaults to "data/original".
        output_folder (str, optional): The folder to save converted HTML files. 
                                      Defaults to "data/output".
        conversion_function (function, optional): The function to use for conversion. 
                                                Defaults to convert_bottom_to_top.
        **kwargs: Additional arguments to pass to the conversion function.
    
    Returns:
        list: A list of paths to the converted files
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all HTML files in the input folder
    html_files = [f for f in os.listdir(input_folder) if f.endswith('.html')]
    
    converted_files = []
    
    # Convert each HTML file
    for html_file in html_files:
        input_path = os.path.join(input_folder, html_file)
        
        # Load HTML from file
        html_string = load_html_from_file(input_path)
        
        # Skip empty files
        if not html_string:
            continue
        
        # Convert HTML
        converted_html = conversion_function(html_string, **kwargs)
        
        # Generate output filename
        function_name = conversion_function.__name__
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        output_filename = f"{function_name}_{os.path.splitext(html_file)[0]}_{timestamp}.html"
        output_path = os.path.join(output_folder, output_filename)
        
        # Save converted HTML
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(converted_html)
        
        print(f"Converted {html_file} to {output_filename}")
        converted_files.append(output_path)
    
    return converted_files