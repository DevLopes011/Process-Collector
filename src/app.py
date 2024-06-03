from Collector.Extract import Extract
from Collector.read_data import ReadData
from DataFrames.excel_exporter import ExcelExporter
from DataFrames.data_frame_creator import DataFrameCreator

class App:
    def __init__(self):
        pass
    
    def run(self):
        read_data = ReadData()
        extract = Extract()
        excel_exporter = ExcelExporter()
        dataFrameCreator = DataFrameCreator()

        data = read_data.read_file('../Inputs/input_text.txt')
        df_cnj = extract.extractor_cnj(data)
        data_frame = dataFrameCreator.add_line(df_cnj)
        excel_exporter.export_to_excel(data_frame, '../Outputs', 'df_process_to_excel.xlsx')

app = App()
app.run()
