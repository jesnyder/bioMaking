
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from  prettytable import PrettyTable

def html_table():

    patent_path = os.path.join('searchResults', 'patents')
    patent_files = os.listdir(patent_path)

    for file in patent_files:

        if file == patent_files[-1]:

            patent_file = os.path.join(patent_path, file)
            print(patent_file)
            df = pd.read_csv(patent_file)
            del df['Unnamed: 0']
            del df['description']
            del df['claims']
            del df['abstract']
            del df['inventors']
            # del df['url']

            html_code = df.to_html(render_links=True)


            """

            x = PrettyTable()

            read_file = open(patent_file, 'r')
            for line in read_file:
                line_split = line.split(',')
                # print(line)

                x.add_row([line_split[0], line_split[1], line_split[3]])

            html_code = x.get_html_string()
            """

            html_path = os.path.join('code')
            if not os.path.isdir(html_path): os.mkdir(html_path)
            html_path = os.path.join('code', 'html')
            if not os.path.isdir(html_path): os.mkdir(html_path)
            html_file = os.path.join(html_path, 'table_' + 'patents' + '.html')



            with open(html_file, 'w') as myFile:
                myFile.write('<html>')
                myFile.write('<body>')
                myFile.write('<table>')

                for line in html_code:
                    myFile.write(line)
                    # myFile.write('/n')

                myFile.write('</tr>')
                myFile.write('</table>')
                myFile.write('</body>')
                myFile.write('</html>')

            myFile.close()








    """
    df.to_csv(patent_file)
    print('patentsRetrieved saved: ' + patent_file)

    ref_path = os.path.join( 'metadata')
    ref_file = os.path.join(ref_path, 'ref.csv')
    df = pd.read_csv(ref_file)

    variableNames = list(df['name'])
    variableValues = list(df['value'])

    value = 0
    for i in range(len(variableNames)):
        if variableName == variableNames[i]:
            value = variableValues[i]
            break

    # print('value = ' + str(value))
    return value
    """
