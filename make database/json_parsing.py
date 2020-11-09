import json

def parsing_json(path):
        with open(path) as json_file:
                json_data = json.load(json_file)

        os_type = json_data['type']
        ismalware = json_data['scans']['Kaspersky']['detected']
        if not ismalware:
                malware_type = 'benign'
        else:
                part = json_data['scans']['Kaspersky']['result']
                part = part.split(':')[-1]
                part = part.split('.')
                if len(part) < 3:
                        malware_type = 'unknown'
                else:
                        malware_type = str(part[0]).upper()

        return os_type, ismalware, malware_type

