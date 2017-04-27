import os
import json
import codecs

from file_processor import FileProcessor


class YoutubeToWatchListProcessor(FileProcessor):

    def __init__(self, input_path):
        super().__init__(input_path)

    def process_json_into_links(self, data):
        links = []
        for data_item in data:
            title = data_item['snippet']['title'].strip()
            snippet_id = 'https://www.youtube.com/watch?v=' + data_item['contentDetails']['videoId']
            current_line = '[' + title + '](' + snippet_id + ')'
            links.append(current_line)

        return links

    def process_json_file_to_dictionary(self, fullpath, known_urls):
        with codecs.open(fullpath, "r", encoding='ascii', errors='ignore') as data_file:
            data = json.load(data_file)

        return self.process_json_into_links(data)

    def process_json(self, inputpath):
        known_urls = []

        all_files = os.listdir(inputpath)

        for filename in all_files:
            if filename.endswith(".json"):
                full_path = inputpath + "\\" + filename
                known_urls = self.process_json_file_to_dictionary(full_path, known_urls)

        return known_urls

    def process_files(self):
        return self.process_json(self.input_path)
