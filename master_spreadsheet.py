#!/usr/bin/env python3.12

from xlsxwriter.utility import xl_col_to_name
import pandas as pd


class MasterSpreadsheet:
    """Some description..."""

    def __init__(self, file: str, sheet_name: str=0, skiprows: int=0):
        """Initialize and create the pandas DataFrame."""
        self.file = file
        self.sheet_name = sheet_name  # Can be int but str is preferred, avoid list.
        self.skiprows = skiprows

        df = pd.read_excel(self.file, sheet_name=sheet_name, skiprows=skiprows)
        headers = [header.replace("\n", " ") for header in df.columns.values]
        for i in range(len(df.columns.values)):
            df.columns.values[i] = headers[i]

        self.headers = headers     # List of Master Spreadsheet headers.
        self.df = df               # Pandas DataFrame of Master Spreadsheet.


    def getColumn(self, header: str) -> int:
        """Outputs column label of the input header."""
        return xl_col_to_name(self.headers.index(header))


    def addColumn(self, header: str, values: list, position: int=None):
        """Add new column to Master Spreadsheet."""
        if position is not None:
            (self.df).insert(position, header, values)
            (self.headers).insert(position, header)
        else:
            #(self.df).insert(len(self.headers), header, values)
            (self.df)[header] = values     # Better version of above line.
            (self.headers).append(header)
            


if __name__ == "__main__":
    # You have to subtract (2 + skiprows) from the row number in Excel.
    # https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different

    import numpy as np

    ms = MasterSpreadsheet("Master_Spreadsheet.xlsx")

    arr = np.zeros(len(ms.df))
    ms.addColumn("NEW_COLUMN", arr, 1)
    print(ms.headers[1])
    
