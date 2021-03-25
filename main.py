##################################################
## This is a simple Python script to select columns
## in a file and save them as a subset of the parent file.
##################################################
## {License_info}
##################################################
## Author: Wagner de O. da Rosa
## Copyright: Copyright 2020
## Credits: ["Wagner de O. da Rosa"]
## License: GPL 3.0
## Version: 1.0.0
## Maintainer: Wagner de O. da Rosa
## Email: wagner.deoliveira@perkinelmer.com
## Status: Deploy
##################################################
import pandas as pd
from os import chdir

path = 'YOUR PATH TO FILE'
chdir(path)


def remove_columns(dataframe, sep='\t'):
    df = pd.read_csv(dataframe, sep=sep)
    # Substitute Col1 and others with the name of the column in your dataframe
    # Add as many columns you want
    # new_df = df[['Col1', 'Col2', 'Col3']]

    # If you want to drop some few columns you can also use this from
    new_df = df.drop(['Factor - Strata'], axis='columns')
    new_df.to_csv(r'pki.app.categorical.survival.analysis.results.txt', index=None, sep=sep, mode='a')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = 'pki.app.categorical.survival.id245.analysis.results.txt'
    remove_columns(file)
