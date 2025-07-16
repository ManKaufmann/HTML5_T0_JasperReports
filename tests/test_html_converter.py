"""
Tests for HTML converter functionality.

This module contains tests for the HTML to JasperReport conversion functions.
"""

import re
import os
import sys
import unittest

# Add parent directory to path to import shared modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.html_utils import convert_bottom_to_top, load_html_from_file, save_html_to_file
from shared.constants import HTML_HEIGHT
import tempfile
import shutil


class TestHtmlConverter(unittest.TestCase):
    """Test cases for HTML converter functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Example HTML for testing
        self.example_html = """<!DOCTYPE html>
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
        #t4_1{left:266px;bottom:804px;letter-spacing:0.15px;}
        #t5_1{left:394px;bottom:804px;letter-spacing:0.17px;}
        #t6_1{left:18px;bottom:804px;letter-spacing:0.14px;}
        #t7_1{left:128px;bottom:804px;}
        #t8_1{left:165px;bottom:804px;letter-spacing:0.15px;}
        #t9_1{left:266px;bottom:804px;letter-spacing:0.15px;}
        #ta_1{left:394px;bottom:804px;letter-spacing:0.16px;}
        #tb_1{left:110px;bottom:804px;}
        #tc_1{left:156px;bottom:804px;}
        #td_1{left:101px;bottom:777px;}
        #te_1{left:697px;bottom:777px;letter-spacing:0.17px;}
        #tf_1{left:18px;bottom:777px;letter-spacing:0.17px;}
        #tg_1{left:119px;bottom:777px;letter-spacing:0.17px;}
        #th_1{left:770px;bottom:777px;letter-spacing:0.17px;}
        #ti_1{left:770px;bottom:777px;letter-spacing:0.17px;}
        #tj_1{left:862px;bottom:777px;}
        #tk_1{left:862px;bottom:777px;letter-spacing:9.39px;word-spacing:-9.17px;}
        #tl_1{left:889px;bottom:777px;}
        #tm_1{left:953px;bottom:777px;letter-spacing:0.17px;}
        #tn_1{left:953px;bottom:777px;letter-spacing:0.17px;}
        #to_1{left:990px;bottom:777px;letter-spacing:0.17px;}
        #tp_1{left:770px;bottom:763px;letter-spacing:0.16px;}
        #tq_1{left:953px;bottom:763px;letter-spacing:0.11px;}
        #tr_1{left:990px;bottom:763px;letter-spacing:0.17px;}
        #ts_1{left:266px;bottom:749px;letter-spacing:0.17px;}
        #tt_1{left:266px;bottom:749px;letter-spacing:0.17px;}
        #tu_1{left:266px;bottom:749px;letter-spacing:0.17px;}
        #tv_1{left:358px;bottom:749px;letter-spacing:0.17px;}
        #tw_1{left:358px;bottom:749px;letter-spacing:0.17px;}
        #tx_1{left:431px;bottom:749px;letter-spacing:0.17px;}
        #ty_1{left:431px;bottom:749px;letter-spacing:3.26px;word-spacing:-3.06px;}
        #tz_1{left:468px;bottom:749px;letter-spacing:0.17px;}
        #t10_1{left:477px;bottom:749px;}
        #t11_1{left:422px;bottom:749px;}
        #t12_1{left:422px;bottom:749px;}
        #t13_1{left:422px;bottom:749px;}
        #t14_1{left:788px;bottom:708px;letter-spacing:0.17px;}
        #t15_1{left:18px;bottom:694px;letter-spacing:0.15px;}
        #t16_1{left:413px;bottom:694px;letter-spacing:0.17px;}
        #t17_1{left:165px;bottom:694px;letter-spacing:0.17px;}
        #t18_1{left:165px;bottom:694px;letter-spacing:0.15px;}
        #t19_1{left:413px;bottom:681px;letter-spacing:0.17px;}
        #t1a_1{left:18px;bottom:681px;letter-spacing:0.17px;}
        #t1b_1{left:541px;bottom:681px;letter-spacing:0.17px;}
        #t1c_1{left:413px;bottom:667px;letter-spacing:0.14px;}
        #t1d_1{left:523px;bottom:667px;}
        #t1e_1{left:18px;bottom:667px;}
        #t1f_1{left:541px;bottom:667px;letter-spacing:0.17px;}
        #t1g_1{left:413px;bottom:653px;letter-spacing:0.14px;}
        #t1h_1{left:523px;bottom:653px;}
        #t1i_1{left:18px;bottom:653px;letter-spacing:0.17px;}
        #t1j_1{left:541px;bottom:653px;letter-spacing:0.17px;}
        #t1k_1{left:413px;bottom:639px;letter-spacing:0.15px;}
        #t1l_1{left:523px;bottom:639px;}
        #t1m_1{left:413px;bottom:626px;letter-spacing:0.17px;}
        #t1n_1{left:18px;bottom:626px;letter-spacing:0.17px;}
        #t1o_1{left:18px;bottom:626px;letter-spacing:0.16px;}
        #t1p_1{left:541px;bottom:626px;letter-spacing:0.17px;}
        #t1q_1{left:18px;bottom:612px;letter-spacing:0.17px;}
        #t1r_1{left:165px;bottom:612px;letter-spacing:0.14px;}
        #t1s_1{left:18px;bottom:598px;letter-spacing:0.17px;}
        #t1t_1{left:110px;bottom:598px;letter-spacing:0.17px;}
        #t1u_1{left:147px;bottom:598px;letter-spacing:0.17px;}
        #t1v_1{left:202px;bottom:598px;letter-spacing:0.16px;}
        #t1w_1{left:633px;bottom:584px;letter-spacing:0.17px;}
        #t1x_1{left:18px;bottom:584px;letter-spacing:0.17px;}
        #t1y_1{left:770px;bottom:584px;letter-spacing:0.17px;}
        #t1z_1{left:770px;bottom:584px;letter-spacing:0.17px;}
        #t20_1{left:18px;bottom:571px;letter-spacing:0.15px;}
        #t21_1{left:633px;bottom:571px;letter-spacing:0.17px;}
        #t22_1{left:147px;bottom:571px;letter-spacing:0.17px;}
        #t23_1{left:147px;bottom:571px;letter-spacing:0.17px;}
        #t24_1{left:770px;bottom:571px;letter-spacing:0.17px;}
        #t25_1{left:18px;bottom:557px;letter-spacing:0.15px;}
        #t26_1{left:128px;bottom:557px;}
        #t27_1{left:633px;bottom:557px;letter-spacing:0.17px;}
        #t28_1{left:147px;bottom:557px;letter-spacing:0.17px;}
        #t29_1{left:770px;bottom:557px;letter-spacing:0.17px;}
        #t2a_1{left:18px;bottom:543px;letter-spacing:0.15px;}
        #t2b_1{left:633px;bottom:543px;letter-spacing:0.17px;}
        #t2c_1{left:193px;bottom:543px;letter-spacing:0.17px;}
        #t2d_1{left:770px;bottom:543px;letter-spacing:0.17px;}
        #t2e_1{left:9px;bottom:502px;letter-spacing:0.17px;}
        #t2f_1{left:9px;bottom:502px;letter-spacing:0.17px;}
        #t2g_1{left:9px;bottom:488px;}
        #t2h_1{left:183px;bottom:488px;letter-spacing:1.93px;word-spacing:-1.74px;}
        #t2i_1{left:9px;bottom:474px;}
        #t2j_1{left:183px;bottom:474px;letter-spacing:1.72px;word-spacing:-1.53px;}
        #t2k_1{left:9px;bottom:461px;letter-spacing:0.17px;}
        #t2l_1{left:9px;bottom:461px;letter-spacing:0.17px;}
        #t2m_1{left:9px;bottom:419px;letter-spacing:0.17px;}
        #t2n_1{left:275px;bottom:419px;}
        #t2o_1{left:339px;bottom:419px;}
        #t2p_1{left:403px;bottom:419px;}
        #t2q_1{left:468px;bottom:419px;}
        #t2r_1{left:532px;bottom:419px;}
        #t2s_1{left:596px;bottom:419px;}
        #t2t_1{left:660px;bottom:419px;}
        #t2u_1{left:724px;bottom:419px;}
        #t2v_1{left:788px;bottom:419px;}
        #t2w_1{left:853px;bottom:419px;}
        #t2x_1{left:917px;bottom:419px;}
        #t2y_1{left:981px;bottom:419px;}
        #t2z_1{left:1045px;bottom:419px;}
        #t30_1{left:1109px;bottom:419px;}
        #t31_1{left:1173px;bottom:419px;}
        #t32_1{left:28px;bottom:406px;letter-spacing:0.17px;}
        #t33_1{left:238px;bottom:406px;letter-spacing:0.17px;}
        #t34_1{left:9px;bottom:392px;letter-spacing:0.17px;}
        #t35_1{left:211px;bottom:392px;}
        #t36_1{left:275px;bottom:392px;}
        #t37_1{left:339px;bottom:392px;}
        #t38_1{left:403px;bottom:392px;}
        #t39_1{left:28px;bottom:378px;letter-spacing:0.17px;}
        #t3a_1{left:174px;bottom:378px;letter-spacing:0.17px;}
        #t3b_1{left:816px;bottom:364px;letter-spacing:0.17px;}
        #t3c_1{left:1027px;bottom:364px;letter-spacing:0.17px;}
        #t3d_1{left:1027px;bottom:364px;letter-spacing:0.19px;word-spacing:9.17px;}

        .s0{font-size:15px;font-family:Courier;color:#000;}
    </style>
    <!-- End inline CSS -->

    <!-- Begin page background -->
    <div id="pg1Overlay" style="width:100%; height:100%; position:absolute; z-index:1; background-color:rgba(0,0,0,0); -webkit-user-select: none;"></div>
    <div id="pg1" style="-webkit-user-select: none;"><object width="1210" height="825" data="1/1.svg" type="image/svg+xml" id="pdf1" style="width:1210px; height:825px; -moz-transform:scale(1); z-index: 0;"></object></div>
    <!-- End page background -->


    <!-- Begin text definitions (Positioned/styled in CSS) -->
    <div class="text-container"><span id="t1_1" class="t s0">Seite: </span><span id="t2_1" class="t s0">( </span><span id="t3_1" class="t s0">) *Kopie* </span><span id="t4_1" class="t s0">LIEFERSCHEIN </span><span id="t5_1" class="t s0">Katag AG - Stralsunder Str.5 - 33605 Bielefeld </span><span id="t6_1" class="t s0">Seite: </span><span id="t7_1" class="t s0">( </span><span id="t8_1" class="t s0">) *Kopie* </span><span id="t9_1" class="t s0">LIEFERSCHEIN </span><span id="ta_1" class="t s0">Katag AG - Stralsunder Str.5 - 33605 Bielefeld </span><span id="tb_1" class="t s0">1 </span><span id="tc_1" class="t s0">1 </span>
        <span id="td_1" class="t s0">/ </span><span id="te_1" class="t s0">Nummer: </span><span id="tf_1" class="t s0">28.09.23 </span><span id="tg_1" class="t s0">15:22 </span><span id="th_1" class="t s0">3034948 </span><span id="ti_1" class="t s0">3034948 </span><span id="tj_1" class="t s0">1 </span><span id="tk_1" class="t s0">1 1 </span><span id="tl_1" class="t s0">1 </span><span id="tm_1" class="t s0">120 </span><span id="tn_1" class="t s0">120 31 </span><span id="to_1" class="t s0">31 </span>
        <span id="tp_1" class="t s0">Auftrag Ind SF </span><span id="tq_1" class="t s0">LO </span><span id="tr_1" class="t s0">Bt </span>
        <span id="ts_1" class="t s0">Liefernr. </span><span id="tt_1" class="t s0">_________ </span><span id="tu_1" class="t s0">Liefernr. 3034948 </span><span id="tv_1" class="t s0">_______ </span><span id="tw_1" class="t s0">3034948 001 </span><span id="tx_1" class="t s0">___ </span><span id="ty_1" class="t s0">001 1 </span><span id="tz_1" class="t s0">__ </span><span id="t10_1" class="t s0">1 </span><span id="t11_1" class="t s0">/ </span><span id="t12_1" class="t s0">_ </span><span id="t13_1" class="t s0">/ </span>
        <span id="t14_1" class="t s0">30349480010112031 </span>
        <span id="t15_1" class="t s0">Kundennummer: </span><span id="t16_1" class="t s0">Streutermin : </span><span id="t17_1" class="t s0">28260001 </span><span id="t18_1" class="t s0">28260001 </span>
        <span id="t19_1" class="t s0">Auftragsdat.: </span><span id="t1a_1" class="t s0">Young Fashion Behrendt </span><span id="t1b_1" class="t s0">28.09.23 </span>
        <span id="t1c_1" class="t s0">Marke </span><span id="t1d_1" class="t s0">: </span><span id="t1e_1" class="t s0">. </span><span id="t1f_1" class="t s0">50 ***Mc Percy </span>
        <span id="t1g_1" class="t s0">Thema </span><span id="t1h_1" class="t s0">: </span><span id="t1i_1" class="t s0">Holmpassage, Holm 39 </span><span id="t1j_1" class="t s0">KATAGABRUF Katag Abrufe </span>
        <span id="t1k_1" class="t s0">Prospekt </span><span id="t1l_1" class="t s0">: </span>
        <span id="t1m_1" class="t s0">Auftragstyp : </span><span id="t1n_1" class="t s0">D-24937 Flensburg </span><span id="t1o_1" class="t s0">D-24937 Flensburg </span><span id="t1p_1" class="t s0">291 Katag Lagerauftrag Anschlusshaus </span>
        <span id="t1q_1" class="t s0">Verdichtung...: VERSA </span><span id="t1r_1" class="t s0">VERSA </span>
        <span id="t1s_1" class="t s0">Versandart</span><span id="t1t_1" class="t s0">....</span><span id="t1u_1" class="t s0">: 200 Hängend: DKS / Liegend: DPD-unfr. </span><span id="t1v_1" class="t s0">Hängend: DKS / Liegend: DPD-unfr. </span>
        <span id="t1w_1" class="t s0">Kundentermin : </span><span id="t1x_1" class="t s0">Denim Jeans </span><span id="t1y_1" class="t s0">28.09.23 </span><span id="t1z_1" class="t s0">28.09.23 </span>
        <span id="t20_1" class="t s0">Modellnummer: </span><span id="t21_1" class="t s0">Kundenauftrag: </span><span id="t22_1" class="t s0">210000943 </span><span id="t23_1" class="t s0">210000943 </span><span id="t24_1" class="t s0">3034948 </span>
        <span id="t25_1" class="t s0">Lagerplatz </span><span id="t26_1" class="t s0">: </span><span id="t27_1" class="t s0">Art.Nr. Lief.: </span><span id="t28_1" class="t s0">P10 </span><span id="t29_1" class="t s0">700 NOS </span>
        <span id="t2a_1" class="t s0">Bereich: </span><span id="t2b_1" class="t s0">Art.Bez.Lief.: </span><span id="t2c_1" class="t s0">2100 Katag, HAKA I / Hosen </span><span id="t2d_1" class="t s0">605 5 P. Regular </span>
        <span id="t2e_1" class="t s0">================================================================================================================================== </span><span id="t2f_1" class="t s0">================================================================================================================================== </span>
        <span id="t2g_1" class="t s0">A </span><span id="t2h_1" class="t s0">31/30 32/30 33/30 34/30 36/30 38/30 40/30 31/32 32/32 33/32 34/32 36/32 38/32 40/32 31/34 32/34 </span>
        <span id="t2i_1" class="t s0">B </span><span id="t2j_1" class="t s0">33/34 34/34 36/34 38/34 40/34 </span>
        <span id="t2k_1" class="t s0">================================================================================================================================== </span><span id="t2l_1" class="t s0">================================================================================================================================== </span>
        <span id="t2m_1" class="t s0">A BLUE STONE </span><span id="t2n_1" class="t s0">1 </span><span id="t2o_1" class="t s0">1 </span><span id="t2p_1" class="t s0">1 </span><span id="t2q_1" class="t s0">1 </span><span id="t2r_1" class="t s0">1 </span><span id="t2s_1" class="t s0">1 </span><span id="t2t_1" class="t s0">1 </span><span id="t2u_1" class="t s0">1 </span><span id="t2v_1" class="t s0">1 </span><span id="t2w_1" class="t s0">1 </span><span id="t2x_1" class="t s0">1 </span><span id="t2y_1" class="t s0">1 </span><span id="t2z_1" class="t s0">1 </span><span id="t30_1" class="t s0">1 </span><span id="t31_1" class="t s0">1 </span>
        <span id="t32_1" class="t s0">600 </span><span id="t33_1" class="t s0">______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ </span>
        <span id="t34_1" class="t s0">B BLUE STONE </span><span id="t35_1" class="t s0">1 </span><span id="t36_1" class="t s0">1 </span><span id="t37_1" class="t s0">1 </span><span id="t38_1" class="t s0">1 </span>
        <span id="t39_1" class="t s0">600 </span><span id="t3a_1" class="t s0">______ ______ ______ ______ </span>
        <span id="t3b_1" class="t s0">Stück gesamt : </span><span id="t3c_1" class="t s0">19 </span><span id="t3d_1" class="t s0">19 STK </span></div>
    <!-- End text definitions -->


</div>
</body>
</html>
"""

    def test_convert_bottom_to_top_no_offset(self):
        """Test conversion from bottom to top positioning without offset using example HTML.
        
        This test verifies that:
        1. The function can convert example HTML
        2. The conversion is correct
        3. The converted HTML is saved to a file
        4. The saved file contains the correctly converted HTML
        """
        # Create a temporary directory for test files
        temp_dir = tempfile.mkdtemp()
        try:
            # Convert HTML
            converted_html = convert_bottom_to_top(self.example_html)
            
            # Save the converted HTML to a file
            timestamp = "test_timestamp"
            output_path = save_html_to_file(converted_html, "test_convert_bottom_to_top_no_offset", timestamp)
            
            # Verify that the output file exists
            self.assertTrue(os.path.exists(output_path), f"Output file {output_path} should exist")
            
            # Load the saved HTML file
            saved_html = load_html_from_file(output_path)
            self.assertTrue(saved_html, "Saved HTML file should not be empty")
            
            # Verify that the saved HTML is the same as the converted HTML
            self.assertEqual(saved_html, converted_html, "Saved HTML should match converted HTML")
            
            # Extract all CSS rules with bottom from the original
            bottom_pattern = re.compile(r'([^{]+){([^}]*bottom:[^}]*)}')
            original_bottom_rules = bottom_pattern.findall(self.example_html)
            
            # Extract all CSS rules with top from the saved HTML
            top_pattern = re.compile(r'([^{]+){([^}]*top:[^}]*)}')
            saved_top_rules = top_pattern.findall(saved_html)
            
            # Check if the number of rules matches
            self.assertEqual(len(original_bottom_rules), len(saved_top_rules),
                            "Number of positioning rules should match")
            
            # Check if bottom values are correctly converted to top values in the saved file
            for i, (selector, rule) in enumerate(original_bottom_rules):
                # Extract bottom value
                bottom_match = re.search(r'bottom:(\d+)px', rule)
                self.assertIsNotNone(bottom_match, f"Bottom value not found in rule: {rule}")
                
                bottom_value = int(bottom_match.group(1))
                
                # Extract top value from saved rule
                top_match = re.search(r'top:(\d+)px', saved_top_rules[i][1])
                self.assertIsNotNone(top_match, f"Top value not found in saved rule: {saved_top_rules[i][1]}")
                
                top_value = int(top_match.group(1))
                
                # Check if the conversion is correct
                expected_top = HTML_HEIGHT - bottom_value
                self.assertEqual(top_value, expected_top,
                                f"Top value should be {expected_top}, got {top_value}")
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_dir)

    def test_convert_bottom_to_top_with_offset(self):
        """Test conversion from bottom to top positioning with offset using example HTML.
        
        This test verifies that:
        1. The function can convert example HTML with offset values
        2. The conversion is correct with both vertical and horizontal offsets
        3. The converted HTML is saved to a file
        4. The saved file contains the correctly converted HTML
        """
        # Create a temporary directory for test files
        temp_dir = tempfile.mkdtemp()
        try:
            # Set offset values
            offset_x = 10
            offset_y = 5
            
            # Convert HTML with offset
            converted_html = convert_bottom_to_top(self.example_html, offset_x, offset_y)
            
            # Save the converted HTML to a file
            timestamp = "test_timestamp"
            output_path = save_html_to_file(converted_html, "test_convert_bottom_to_top_with_offset", timestamp)
            
            # Verify that the output file exists
            self.assertTrue(os.path.exists(output_path), f"Output file {output_path} should exist")
            
            # Load the saved HTML file
            saved_html = load_html_from_file(output_path)
            self.assertTrue(saved_html, "Saved HTML file should not be empty")
            
            # Verify that the saved HTML is the same as the converted HTML
            self.assertEqual(saved_html, converted_html, "Saved HTML should match converted HTML")
            
            # Extract all CSS rules with bottom from the original
            bottom_pattern = re.compile(r'([^{]+){([^}]*bottom:[^}]*)}')
            original_bottom_rules = bottom_pattern.findall(self.example_html)
            
            # Extract all CSS rules with top from the saved HTML
            top_pattern = re.compile(r'([^{]+){([^}]*top:[^}]*)}')
            saved_top_rules = top_pattern.findall(saved_html)
            
            # Check if the number of rules matches
            self.assertEqual(len(original_bottom_rules), len(saved_top_rules),
                            "Number of positioning rules should match")
            
            # Check if bottom values are correctly converted to top values with offset in the saved file
            for i, (selector, rule) in enumerate(original_bottom_rules):
                # Extract bottom value
                bottom_match = re.search(r'bottom:(\d+)px', rule)
                self.assertIsNotNone(bottom_match, f"Bottom value not found in rule: {rule}")
                
                bottom_value = int(bottom_match.group(1))
                
                # Extract top value from saved rule
                top_match = re.search(r'top:(\d+)px', saved_top_rules[i][1])
                self.assertIsNotNone(top_match, f"Top value not found in saved rule: {saved_top_rules[i][1]}")
                
                top_value = int(top_match.group(1))
                
                # Check if the conversion is correct with offset
                expected_top = HTML_HEIGHT - bottom_value + offset_y
                self.assertEqual(top_value, expected_top,
                                f"Top value should be {expected_top}, got {top_value}")
                
                # Extract left value from original rule
                left_match = re.search(r'left:(\d+)px', rule)
                if left_match:
                    left_value = int(left_match.group(1))
                    
                    # Extract left value from saved rule
                    saved_left_match = re.search(r'left:(\d+)px', saved_top_rules[i][1])
                    self.assertIsNotNone(saved_left_match, 
                                        f"Left value not found in saved rule: {saved_top_rules[i][1]}")
                    
                    saved_left_value = int(saved_left_match.group(1))
                    
                    # Check if the left offset is applied correctly
                    expected_left = left_value + offset_x
                    self.assertEqual(saved_left_value, expected_left,
                                    f"Left value should be {expected_left}, got {saved_left_value}")
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_dir)

    def test_convert_bottom_to_top_with_file(self):
        """Test conversion from bottom to top positioning with a file input and output.
        
        This test verifies that:
        1. The function can load HTML from a file
        2. The conversion is correct
        3. The converted HTML is saved to a file
        4. The saved file contains the correctly converted HTML
        """
        # Create a temporary directory for test files
        temp_dir = tempfile.mkdtemp()
        try:
            # Check if the test file exists
            test_file_path = os.path.join('data', 'original', 'original_2025-07-16_104156.html')
            if not os.path.exists(test_file_path):
                # Create a temporary test file with example HTML instead of skipping the test
                os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
                with open(test_file_path, 'w', encoding='utf-8') as f:
                    f.write(self.example_html)
                print(f"Created test file {test_file_path} with example HTML")
            
            # Load HTML from file
            html_string = load_html_from_file(test_file_path)
            self.assertTrue(html_string, "HTML file should not be empty")
            
            # Convert HTML
            offset_x = 0
            offset_y = 0
            converted_html = convert_bottom_to_top(html_string, offset_x, offset_y)
            
            # Save the converted HTML to a file
            timestamp = "test_timestamp"
            output_path = save_html_to_file(converted_html, "test_convert_bottom_to_top_with_file", timestamp)
            
            # Verify that the output file exists
            self.assertTrue(os.path.exists(output_path), f"Output file {output_path} should exist")
            
            # Load the saved HTML file
            saved_html = load_html_from_file(output_path)
            self.assertTrue(saved_html, "Saved HTML file should not be empty")
            
            # Verify that the saved HTML is the same as the converted HTML
            self.assertEqual(saved_html, converted_html, "Saved HTML should match converted HTML")
            
            # Extract all CSS rules with bottom from the original
            bottom_pattern = re.compile(r'([^{]+){([^}]*bottom:[^}]*)}')
            original_bottom_rules = bottom_pattern.findall(html_string)
            
            # Extract all CSS rules with top from the saved HTML
            top_pattern = re.compile(r'([^{]+){([^}]*top:[^}]*)}')
            saved_top_rules = top_pattern.findall(saved_html)
            
            # Check if the number of rules matches
            self.assertEqual(len(original_bottom_rules), len(saved_top_rules),
                            "Number of positioning rules should match")
            
            # Check if bottom values are correctly converted to top values in the saved file
            correct_conversions = 0
            total_conversions = 0
            
            for i, (selector, rule) in enumerate(original_bottom_rules):
                if i < len(saved_top_rules):
                    # Extract bottom value
                    bottom_match = re.search(r'bottom:(\d+)px', rule)
                    if bottom_match:
                        bottom_value = int(bottom_match.group(1))
                        
                        # Extract top value from saved rule
                        top_match = re.search(r'top:(\d+)px', saved_top_rules[i][1])
                        if top_match:
                            top_value = int(top_match.group(1))
                            
                            # Check if the conversion is correct
                            expected_top = HTML_HEIGHT - bottom_value + offset_y
                            if top_value == expected_top:
                                correct_conversions += 1
                            
                            total_conversions += 1
            
            # Check if all conversions are correct
            self.assertEqual(correct_conversions, total_conversions,
                            f"{correct_conversions} of {total_conversions} conversions are correct")
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    unittest.main()