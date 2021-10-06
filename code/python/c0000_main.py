import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0100_search_resources import search_resources
from c0200_html_build import html_build

def main():
    """
    Map the publications by author affiliation and impact

    Tasks to complete:
    1. Search for relevant publications
    2. Build html

    """

    print("running main")

    # Review the note above
    # Identify which tasks need to be run
    # List the task numbers that need to be run below
    tasks = [2]

    if 1 in tasks: search_resources()
    if 2 in tasks: html_build()



    print("completed main")

if __name__ == "__main__":
    main()
