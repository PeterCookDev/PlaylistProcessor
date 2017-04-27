import os
import json
import codecs

from file_processor import FileProcessor


class VimeoResponseProcessor(FileProcessor):

    def __init__(self, input_path):
        super().__init__(input_path)

    def process_json_file_to_dictionary(self, data_file):
        links = []
        data = json.loads(data_file)
        for data_item in data['body']['data']:
            title = data_item['name'].strip()
            snippet_id = data_item['link']
            current_line = '[' + title + '](' + snippet_id + ')'
            links.append(current_line)

        return links


    def clean_up_vimeo_api(self, response_body):
        body = response_body.replace("   ", "")
        body = body.replace('\\\\\\"', "\\")
        body = body.replace('\\n', '')
        body = body.replace('"https:\\\/\\\/vimeo.com', "'https:\/\/vimeo.com")
        body = body.replace("\\", "")
        body = body.replace('"{', "{")
        body = body.replace('}"', "}")
        return body


    def preprocess_json(self, fullpath):
        with codecs.open(fullpath, "r", encoding='ascii', errors='ignore') as data_file:
            data = data_file.read()
            data_file.close()

        new_filename = fullpath + ".new"
        body = self.clean_up_vimeo_api(data)
        return body

    def process_json(self, inputpath):
        known_urls = []
        all_files = os.listdir(inputpath)
        for filename in all_files:
            if filename.endswith(".response"):
                full_path = inputpath + "\\" + filename
                body = self.preprocess_json(full_path)
                known_urls.extend(self.process_json_file_to_dictionary(body))

        return known_urls

    def process_files(self):
        return self.process_json(self.input_path)