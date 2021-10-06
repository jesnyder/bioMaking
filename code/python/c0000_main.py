import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0100_search_resources import search_resources

def main():
    """
    Map the publications by author affiliation and impact

    Tasks to complete:
    1. Search for relevant publications
    2. Find the latitude and longitude of author affiliations
    3. Aggregate information
    4. Make plot as .png
    5. Make .gif
    6. Make .mp4
    7. Summarize aggregated information

    """

    print("running main")

    # Review the note above
    # Identify which tasks need to be run
    # List the task numbers that need to be run below
    tasks = [1]

    if 1 in tasks: search_resources()
    
    print("completed main")

if __name__ == "__main__":
    main()
