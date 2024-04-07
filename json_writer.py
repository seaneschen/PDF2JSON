'''
JSONWriter class to handle the conversion of structured text to JSON format and writing it to a file.
'''
import json
class JSONWriter:
    @staticmethod
    def convert_to_json(structured_content):
        # Convert the structured content into a JSON-friendly format
        json_content = {"text": structured_content}
        return json_content
    @staticmethod
    def write_to_file(json_content, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_content, file, indent=4, ensure_ascii=False)