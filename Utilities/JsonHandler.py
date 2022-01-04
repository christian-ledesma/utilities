import json

class JsonHandler:

    def read(file, pretty=False):
        """
        params: set 'pretty' to True if you need Json indentation
        """
        data = None
        with open(file) as json_file:
            data = json.load(json_file)
            if pretty:
                data = json.dumps(data, indent = 4, sort_keys=True)
        return data
