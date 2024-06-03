import re

class Extract:
    def __init__(self):
        pass

    def extractor_cnj (self, data):
        results = re.findall( r'\d{7}\-\d{2}\.\d{4}.\d{2}.\d{4}', data)
        return results


