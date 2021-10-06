import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pypatent

def search_patent():
    """
    Find Rooster cumstomers in the patent databases
    Find all operators in the mesenchymal/exosome sector
    Identify operators not citing Rooster
    """

    print("running search_patents")

    # Name searchers
    searchNames = []
    searchNames.append('synthetic biology') #
    searchNames.append('CRISPR') #
    searchNames.append('cyanobacteria') #
    searchNames.append('diatom') #
    searchNames.append('spirulina') #
    # searchNames.append('genetic engineering') #
    searchNames.append('synbio') #

    df = pd.DataFrame()

    for name in searchNames:

        # help on USPTO search terms
        # https://patft.uspto.gov/netahtml/PTO/help/helpflds.htm
        if name == 'synthetic biology': searchTerms = ['synthetic biology', 'gene edit', 'genetic engineering']
        elif name == 'synbio': searchTerms = ['synbio']
        elif name == 'CRISPR': searchTerms = ['CRISPR']
        elif name == 'spirulina': searchTerms = ['spirulina']
        elif name == 'cyanobacteria': searchTerms = ['cyanobacteria']
        elif name == 'diatom': searchTerms = ['diatom']

        df = query_USPTO(name, searchTerms, df)

    print("completed search_patents")


def query_USPTO(searchName, searchTerms, df):
    """
    Query the USPTO with the search terms
    Save as a dataframe
    """

    # Query for patents metadata
    for term in searchTerms:

        df1 = pypatent.Search(term).as_dataframe()
        df1['searchTerm'] = [term] * len(list(df1['title']))
        df = df.append(df1, ignore_index = True)

    # Remove duplicates and sort
    df = df.drop_duplicates(subset ="title")
    df = df.sort_values(by=['patent_date'], ascending = False)
    df = df.reset_index()
    del df['index']

    # Save the dataframe
    patent_path = os.path.join('searchResults')
    if not os.path.isdir(patent_path): os.mkdir(patent_path)
    patent_path = os.path.join('searchResults', 'patents')
    if not os.path.isdir(patent_path): os.mkdir(patent_path)
    patent_file = os.path.join(patent_path, 'patents_' + 'synbio' + '.csv')
    df.to_csv(patent_file)
    print('patentsRetrieved saved: ' + patent_file)

    return(df)
