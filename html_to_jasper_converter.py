"""
HTML to JasperReport Converter

This module provides functions to convert HTML elements to JasperReport XML elements.
It supports both bottom-based and top-based positioning, and can apply scaling factors and offsets.
"""

import re
from bs4 import BeautifulSoup
from shared.constants import (
    HTML_HEIGHT, HTML_WIDTH,
    JASPER_PAGE_WIDTH, JASPER_PAGE_HEIGHT,
    JASPER_MARGIN_TOP, JASPER_MARGIN_RIGHT, JASPER_MARGIN_BOTTOM, JASPER_MARGIN_LEFT,
    SCALE_FACTOR_X, SCALE_FACTOR_Y
)
from shared.html_utils import (
    parse_html, extract_css_styles, extract_elements,
    convert_bottom_to_top, apply_offset, load_html_from_file
)

def generate_jasper_textfields_from_html(
    html_string=None, 
    file_path=None,
    offset_x=0, 
    offset_y=0,
    scale_factor_x=None,
    scale_factor_y=None,
    detect_positioning="auto"
):
    """
    Convert HTML <span> elements to JasperReport <textField> elements.
    
    This function can handle both bottom-based and top-based positioning,
    and can apply scaling factors and offsets.
    
    Args:
        html_string (str, optional): The HTML string to convert. If None, file_path must be provided.
        file_path (str, optional): The path to the HTML file to convert. If None, html_string must be provided.
        offset_x (int, optional): Horizontal offset to apply to left values (positive = right, negative = left). Defaults to 0.
        offset_y (int, optional): Vertical offset to apply to top values (positive = down, negative = up). Defaults to 0.
        scale_factor_x (float, optional): Scaling factor for the X-axis. If None, uses the default from constants.
        scale_factor_y (float, optional): Scaling factor for the Y-axis. If None, uses the default from constants.
        detect_positioning (str, optional): How to detect the positioning system. 
                                          "auto" (default): Automatically detect based on CSS properties.
                                          "bottom": Force bottom-based positioning.
                                          "top": Force top-based positioning.
    
    Returns:
        str: The JasperReport XML for the text fields.
    """
    # Validate input
    if html_string is None and file_path is None:
        raise ValueError("Either html_string or file_path must be provided")
    
    # Load HTML from file if needed
    if html_string is None:
        html_string = load_html_from_file(file_path)
    
    # Use default scale factors if not provided
    if scale_factor_x is None:
        scale_factor_x = SCALE_FACTOR_X
    if scale_factor_y is None:
        scale_factor_y = SCALE_FACTOR_Y
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_string, 'html.parser')
    
    # Extract all styles from all style tags
    styles = {}
    for style_content in soup.select('style'):
        if style_content.string:  # Check if style content is not None
            for style_definition in style_content.string.split('}'):
                if '{' in style_definition:
                    parts = style_definition.split('{')
                    if len(parts) == 2:
                        selector, properties = parts
                        selector = selector.strip()
                        properties = properties.strip()
                        styles[selector] = properties
    
    # Detect positioning system if auto
    if detect_positioning == "auto":
        # Check if any style contains 'bottom' property
        has_bottom = any('bottom:' in prop for prop in styles.values())
        # Check if any style contains 'top' property
        has_top = any('top:' in prop for prop in styles.values())
        
        if has_bottom and not has_top:
            detect_positioning = "bottom"
        else:
            detect_positioning = "top"
    
    # Convert bottom-based positioning to top-based if needed
    if detect_positioning == "bottom":
        # Create a new HTML string with converted positions
        html_string = convert_bottom_to_top(html_string, offset_x, offset_y)
        # Re-parse the HTML with converted positions
        soup = BeautifulSoup(html_string, 'html.parser')
        # Re-extract styles
        styles = {}
        for style_content in soup.select('style'):
            if style_content.string:
                for style_definition in style_content.string.split('}'):
                    if '{' in style_definition:
                        parts = style_definition.split('{')
                        if len(parts) == 2:
                            selector, properties = parts
                            selector = selector.strip()
                            properties = properties.strip()
                            styles[selector] = properties
    elif detect_positioning == "top" and (offset_x != 0 or offset_y != 0):
        # Apply offsets to top-based positioning
        html_string = apply_offset(html_string, offset_x, offset_y)
        # Re-parse the HTML with applied offsets
        soup = BeautifulSoup(html_string, 'html.parser')
        # Re-extract styles
        styles = {}
        for style_content in soup.select('style'):
            if style_content.string:
                for style_definition in style_content.string.split('}'):
                    if '{' in style_definition:
                        parts = style_definition.split('{')
                        if len(parts) == 2:
                            selector, properties = parts
                            selector = selector.strip()
                            properties = properties.strip()
                            styles[selector] = properties
    
    # Process each span to extract the text and associated styles
    jasper_textfields = ""
    for span in soup.select('span.t'):
        span_id = span.attrs.get('id', '')
        span_text = span.string if span.string else ""
        span_class = " ".join(span.attrs.get('class', []))
        
        # Extract style associated with this span using its id
        style_definition = styles.get(f"#{span_id}", '')
        
        # Extract position information
        x_match = re.search(r'left:(\d+\.?\d*)px', style_definition)
        y_match = re.search(r'top:(\d+\.?\d*)px', style_definition)
        
        # Skip if position information is missing
        if not x_match or not y_match:
            continue
        
        # Extract and scale positions
        x_pos = float(x_match.group(1)) * scale_factor_x
        y_pos = float(y_match.group(1)) * scale_factor_y
        
        # Calculate width based on text length (with a minimum width)
        width = max(10 * len(span_text), 30) * scale_factor_x
        
        # Generate the JasperReport XML for this text span
        jasper_textfields += f"""
            <textField>
                <reportElement style="{span_class}" x="{int(x_pos)}" y="{int(y_pos)}" width="{int(width)}" height="30" />
                <textFieldExpression><![CDATA["{span_text}"]]></textFieldExpression>
            </textField>
        """
    
    return jasper_textfields