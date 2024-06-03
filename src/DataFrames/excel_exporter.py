import pandas as pd
import os

class ExcelExporter:
    def __init__(self):
        pass

    def export_to_excel(self, data_frame, directory, file_name):
            try:
                file_path = os.path.join(directory, file_name)
                data_frame.to_excel(file_path, index=False)
                print(f"DataFrame exported successfully to {file_path}")
            except Exception as e:
                print(f"An error occurred while exporting the DataFrame to Excel: {e}")
