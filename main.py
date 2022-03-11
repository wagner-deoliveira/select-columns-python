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

path = 'C:/Users/DeOliW20137/Downloads/STL-896/STL-896/Comparison1'
chdir(path)


def remove_columns(dataframe, column_list, output_file, sep='\t'):
    df = pd.read_csv(dataframe, sep=sep)
    # Substitute Col1 and others with the name of the column in your dataframe

    # If you want to drop some few columns you can also use this from
    new_df = df.drop(column_list, axis='columns')
    new_df.to_csv(output_file, index=None, sep=sep, mode='a')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = 'compounds.txt'
    columns_to_remove = ['Comments']
    remove_columns(file, columns_to_remove, file)
