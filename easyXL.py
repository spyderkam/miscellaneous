#!/usr/bin/env python3.12

__author__ = "spyderkam"

import pandas as pd
import xlsxwriter


class Table:
    """Class of football league tables."""
    
    def __init__(self, path, sheet_name=0, excel=False):
        self.path = path            # Path will just be the filename if it is in the same directory as this script.
        self.sheet_name = sheet_name
        self.excel = excel
        if excel is True:
            self.df = pd.read_excel(path, sheet_name=sheet_name)
        elif excel is False:
            self.df = pd.read_csv(path)
        (self.df).index += 1        
        
    def cell_value(self, club, header, value):
        """Give info..."""
        row_number = (self.df).loc[(self.df)["Club"] == club, header].index[0] - 1     # Subtract 1 for index shift.
        column_number = (self.df).columns.get_loc(header)
        column_letter = xlsxwriter.utility.xl_col_to_name(column_number)
        (self.df).iloc[row_number, column_number] = value
        
    def change_clubData(self, club, clubData):
        """Change the row data with respect to the club.
        Club is the club name and clubData is a list of its data.
        Do not include the club itself in clubData."""
        for i, column in enumerate((self.df).columns[1::]):
            (self.df).loc[(self.df)["Club"] == club, column] = clubData[i]
    
    def save(self):
        """Save the spreadsheet to the same format it already is."""
        if self.excel is True:
            (self.df).to_excel(self.path, sheet_name=self.sheet_name, index=False)
        elif self.excel is False:
            (self.df).to_csv(self.path, index=False)
        
    def reorder(self):
        """Reset the table order based on points, etc."""
        SORT_ORDER = ["Points", "GD", "GF", "W", "D", "Club"]
        (self.df).sort_values(by=SORT_ORDER, ascending=False, inplace=True, ignore_index=True)
        (self.df).index += 1 

    def getValue(self, club, header):
        """Get the value of a cell."""
        return ((self.df)[(self.df)["Club"] == club][header]).values[0]       



if __name__ == "__main__":
    eplt = Table("epl_2425.csv", sheet_name="Table")
    #eplt.cell_value("Wolverhampton Wanderers", "Points", "50")
    eplt.reorder()
    print(eplt.df)
    eplt.save()
    #eplt.change_clubData("Liverpool", [12, 10, 1, 1, 24, 8, 16, -10, "LLLLL"])
    
