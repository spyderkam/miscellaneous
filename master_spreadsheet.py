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


    def addColumn(self, header: str, newCol: list, position: int=None):
        """Add new column to Master Spreadsheet."""
        if position is not None:
            (self.df).insert(position, header, newCol)
            (self.headers).insert(position, header)
        else:
            (self.df).insert(len(self.headers), header, newCol)
            #(self.df)[header] = newCol     # Do not use this method, no dupilcate support.
            (self.headers).append(header)


    def addRow(self, newRow: list, position: int=None):
        """Add new row to Master Spreadsheet."""

        m, n = (ms.df).shape[0], (ms.df).shape[1]     # df is an m x n matrix
        # [newRow manipulation for rows with pd.isna values]

        if position is None:     # Create the new row at the end.
            (ms.df).loc[m] = newRow
        else:                    # Insert the new row before the end.
            (ms.df).loc[position - 0.5] = newRow     # The 0.5 can be any number such that 0 < n < 1.
            (ms.df) = (ms.df).sort_index()
            (ms.df).reset_index(drop=True, inplace=True)
                        


if __name__ == "__main__":
    # You have to subtract (2 + skiprows) from the row number in Excel.
    # https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different

    from storage import *

    ms = MasterSpreadsheet("Master_Spreadsheet.xlsx")

    #arr1 = [i for i in range(len(ms.df))]
    #ms.addColumn("NEW_COLUMN", arr1, 1)
    #print(ms.headers[1])

    m, n = ms.df.shape[0], ms.df.shape[1]
    arr2 = np.zeros(n)
    ms.addRow(arr2, 0)
