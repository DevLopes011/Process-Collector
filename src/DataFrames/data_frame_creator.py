import pandas as pd

class DataFrameCreator:
    def __init__(self) -> None:
        self.data_frame = pd.DataFrame(columns=['CNJ'])


    def add_line(self, cnj):
        new_line = pd.DataFrame(cnj, columns=['CNJ'])
        self.data_frame = pd.concat([self.data_frame, new_line], ignore_index=True)
        
        return self.data_frame
    