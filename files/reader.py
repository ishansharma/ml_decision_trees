from os.path import isfile

import pandas as pd


# do a quick check if the CSV path exists. If it doesn't, exit.
# if the file exists, read it using Pandas and return resulting dataframe
def read_csv(filepath=''):
    if not _does_file_exist(filepath):
        print("The file " + filepath + " does not exist")
        exit(-2)

    data = pd.read_csv(filepath)
    return data


# check if a file exists on a given path
def _does_file_exist(filepath=''):
    if filepath == '':
        return False

    return isfile(filepath)
