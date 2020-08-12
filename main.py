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


def remove_columns(dataframe, sep='\t'):
    df = pd.read_csv(dataframe, sep=sep)
    # Substitute Col1 and others with the name of the column in your dataframe
    # Add as many columns you want
    new_df = df[['Col1', 'Col2', 'Col3']]
    new_df.to_csv(r'exported.txt', index=None, sep=sep, mode='a')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = 'file_path'
    remove_columns(file)
