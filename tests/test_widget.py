from tw2.core.testbase import WidgetTest
from tw2.wysihtml5 import *

class TestWysihtml5(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Wysihtml5
    # Initilization args. go here 
    attrs = {'id':'wysihtml5-test'}
    params = {}
    expected = """<div id="wysihtml5-test"></div>"""
