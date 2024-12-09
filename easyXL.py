#!/usr/bin/env python3.12

__author__ = "spyderkam"

import pandas as pd


class Table:
    """Class of football league tables."""
    
    def __init__(self, path: str, excel: bool = False, sheet_name: str | int = 0) -> None:
        self.path = path
        self.excel = excel
        if excel is True:
            self.sheet_name = sheet_name
            self.df = pd.read_excel(path, sheet_name=sheet_name)
        elif excel is False:
            self.df = pd.read_csv(path)
        (self.df).index += 1        


    def cell_value(self, club: str, header: str, value) -> None:
        """Update a cell value."""
        try:
            row_number = (self.df).loc[(self.df)["Club"] == club, header].index[0]
            (self.df).loc[row_number, header] = value
        except (IndexError, KeyError) as err: 
            print(f"Error: {err}")
        
    def change_clubData(self, club: str, clubData: tuple) -> None:
        """Change the row data with respect to the club.
        Club is the club name and clubData is a tuple of its data.
        Do not include the club itself in clubData."""
        for i, column in enumerate((self.df).columns[1::]):
            (self.df).loc[(self.df)["Club"] == club, column] = clubData[i]
    
    def save(self) -> None:
        """Save the spreadsheet to the same format it already is."""
        if self.excel is True:
            (self.df).to_excel(self.path, sheet_name=self.sheet_name, index=False)
        elif self.excel is False:
            (self.df).to_csv(self.path, index=False)
        
    def reorder(self) -> None:
        """Reset the table order based on points, etc."""
        SORT_ORDER = ["Points", "GD", "GF", "W", "D", "Club"]
        (self.df).sort_values(by=SORT_ORDER, ascending=False, inplace=True, ignore_index=True)
        (self.df).index += 1 
    
    def getValue(self, club: str, header: str):
        """Get the value of a cell."""
        try:
            return self.df[self.df["Club"] == club][header].values[0]
        except (IndexError, KeyError) as error:
            print(f"Error: {error}")
            return None



if __name__ == "__main__":
    eplt = Table("epl_2425.csv", sheet_name="Table")
    eplt.cell_value("Wolverhampton Wanderers", "W", "50")
    print(eplt.df)
    x = eplt.getValue("Wolverhampton Wanderers", "W")
    #eplt.reorder()
    print(x)
    #eplt.save()
    #eplt.change_clubData("Liverpool", [12, 10, 1, 1, 24, 8, 16, -10, "LLLLL"])
    
