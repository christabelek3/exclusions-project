import pandas as pd
from pathlib import Path
import os

iopathroot = Path(__file__).resolve().parents[2]

def load_rawdata(filename):
    """
    Load raw data from the specified filename in the raw-data directory.
    Args:
        filename (str): The name of the file to load.
    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    rawfilepath = iopathroot / "data" / "raw-data" / filename
    df = pd.read_spss(rawfilepath, convert_categoricals=False)
    return df

def load_processeddata(filename):
    """
    Load processed data from the specified filename in the processed-data directory.
    Args:
        filename (str): The name of the file to load.
    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """ 
    processedfilepath = iopathroot / "data" / "processed-data" / filename
    df = pd.read_csv(processedfilepath)
    return df

def save_to_csv(df, output_filename):
    """
    Save a pandas DataFrame to a CSV file in the processed-data directory.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_filename (str): The name of the file to save.
    """
    output_filepath = iopathroot / "data" / "processed-data" / output_filename
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    df.to_csv(output_filepath, index=False)


