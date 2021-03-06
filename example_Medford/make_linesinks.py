
# coding: utf-8

# In[1]:

import sys
sys.path.insert(0, '../linesinkmaker')
import lsmaker
'''
try:
    input_file = sys.argv[1]
except IndexError:
    print("\nusage is: python make_linesinks.py <input_xml_file>\n")
    quit()
'''
input_file = 'Medford_lines.xml'
ls = lsmaker.linesinks(input_file)

ls.preprocess(save=True)

ls.makeLineSinks(shp='preprocessed/lines.shp')
