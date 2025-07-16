import re
import os
import datetime

# Constants for HTML page size
HTML_WIDTH = 1210
HTML_HEIGHT = 825
HTML_MARGIN_TOP = 0
HTML_MARGIN_RIGHT = 0
HTML_MARGIN_BOTTOM = 0
HTML_MARGIN_LEFT = 0

def convert_bottom_to_top(html_string: str, offset_x: int = 0, offset_y: int = 0) -> str:
    """
    Converts bottom-positioned elements to top-positioned elements in HTML.
    
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

def save_html_with_timestamp(html_string: str, function_name: str = "convert_bottom_to_top") -> str:
    """
    Saves HTML string to a file with a timestamp in the filename.
    
    Args:
        html_string (str): The HTML string to save
        function_name (str, optional): The name of the function to include in the filename. 
                                      Defaults to "convert_bottom_to_top".
    
    Returns:
        str: The path to the saved file
    """
    # Create output directory if it doesn't exist
    output_dir = "data/output_files"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Create filename
    filename = f"{function_name}_{timestamp}.html"
    file_path = os.path.join(output_dir, filename)
    
    # Save the HTML to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_string)
    
    print(f"HTML saved to: {file_path}")
    return file_path

def load_html_from_file(file_path: str) -> str:
    """
    Loads HTML from a file.
    
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

def save_original_html(html_string: str) -> str:
    """
    Saves the original HTML string to a file in the original_files directory.
    
    Args:
        html_string (str): The original HTML string to save
    
    Returns:
        str: The path to the saved file
    """
    # Create original files directory if it doesn't exist
    original_dir = "data/original_files"
    os.makedirs(original_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Create filename
    filename = f"original_{timestamp}.html"
    file_path = os.path.join(original_dir, filename)
    
    # Save the HTML to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_string)
    
    print(f"Original HTML saved to: {file_path}")
    return file_path

# Example usage
if __name__ == "__main__":
    # Example HTML with bottom-positioned elements
    example_html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta charset="utf-8" />
</head>

<body style="margin: 0;">

<div id="p1" style="overflow: hidden; position: relative; background-color: white; width: 1210px; height: 825px;">

    <!-- Begin shared CSS values -->
    <style class="shared-css" type="text/css" >
        .t {
            transform-origin: bottom left;
            z-index: 2;
            position: absolute;
            white-space: pre;
            overflow: visible;
            line-height: 1.5;
        }
        .text-container {
            white-space: pre;
        }
        @supports (-webkit-touch-callout: none) {
            .text-container {
                white-space: normal;
            }
        }
    </style>
    <!-- End shared CSS values -->

    <!-- Begin inline CSS -->
    <style type="text/css" >
        #t1_1{left:18px;bottom:804px;letter-spacing:0.14px;}
        #t2_1{left:128px;bottom:804px;}
        #t3_1{left:165px;bottom:804px;letter-spacing:0.15px;}
    </style>
    <!-- End inline CSS -->

    <!-- Begin text -->
    <div id="t1_1" class="t">Beispieltext 1</div>
    <div id="t2_1" class="t">Beispieltext 2</div>
    <div id="t3_1" class="t">Beispieltext 3</div>
    <!-- End text -->

</div>
</body>
</html>"""
    
    # Save the original HTML
    original_path = save_original_html(example_html)
    
    # Convert bottom to top
    converted_html = convert_bottom_to_top(example_html)
    
    # Save the converted HTML
    converted_path = save_html_with_timestamp(converted_html)
    
    # Convert with offsets
    converted_with_offset = convert_bottom_to_top(example_html, offset_x=3, offset_y=-5)
    
    # Save the converted HTML with offsets
    offset_path = save_html_with_timestamp(converted_with_offset, "convert_bottom_to_top_with_offset")
    
    print("\nConversion completed successfully!")