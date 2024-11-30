#!/usr/bin/env python3.12

__author__ = "Kamyar Modjtahedzadeh"

import pandas as pd
import xlsxwriter


class Table:
    """Class of soccer league tables."""

    def __init__(self, path, sheet_name=0):
        self.path = path
        self.sheet_name = sheet_name
        (self.df) = pd.read_excel(path, sheet_name=sheet_name)
        (self.df).index += 1

    def cell_value(self, club, header, value):
        """Give info..."""
        row_number = (self.df).loc[(self.df)["Club"] == club, header].index[0] - 1     # Subtract 1 for index shift.
        column_number = (self.df).columns.get_loc(header)
        column_letter = xlsxwriter.utility.xl_col_to_name(column_number)
        (self.df).iloc[row_number, column_number] = value

    def save(self):
        """Save the spreadsheet."""
        
