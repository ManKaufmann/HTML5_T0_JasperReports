"""
Constants for HTML to JasperReport conversion.

This module contains all the technical constants used in the HTML to JasperReport conversion process.
"""

# HTML page dimensions and margins
HTML_WIDTH = 1210
HTML_HEIGHT = 825
HTML_MARGIN_TOP = 0
HTML_MARGIN_RIGHT = 0
HTML_MARGIN_BOTTOM = 0
HTML_MARGIN_LEFT = 0

# JasperReport page dimensions and margins (A4)
JASPER_PAGE_WIDTH = 595
JASPER_PAGE_HEIGHT = 842
JASPER_MARGIN_TOP = 20
JASPER_MARGIN_RIGHT = 20
JASPER_MARGIN_BOTTOM = 20
JASPER_MARGIN_LEFT = 20

# Calculate scale factors for converting between HTML and JasperReport dimensions
SCALE_FACTOR_X = (JASPER_PAGE_WIDTH - JASPER_MARGIN_LEFT - JASPER_MARGIN_RIGHT) / HTML_WIDTH
SCALE_FACTOR_Y = (JASPER_PAGE_HEIGHT - JASPER_MARGIN_TOP - JASPER_MARGIN_BOTTOM) / HTML_HEIGHT