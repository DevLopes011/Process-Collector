import re

class Extract:
    def __init__(self):
        pass

    def extractor_cnj (self, data):
        results = re.findall( r'\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b', data)
        return results


