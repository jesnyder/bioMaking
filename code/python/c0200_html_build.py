import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shutil, os

from c0101_search_patent import search_patent
from c0102_search_clinic import search_clinic
from c0103_search_pubs import search_pubs

from c0002_html_table import html_table

def html_build():
    """
    """

    print("running html_build")

    html_table()

    html_path = os.path.join('code', 'html')
    html_file = os.path.join(html_path, 'table_' + 'patents' + '.html')

    old_file = html_file
    new_file = 'index.html'
    shutil.copy(old_file, new_file)



    print("completed search_resources")
