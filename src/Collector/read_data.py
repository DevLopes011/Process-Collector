class ReadData:
    def __init__(self):
        pass
    
    def read_file(self, text):
        with open(text, "r") as file:
            data = file.read()
            return data
        
    def read_json(self):
        pass