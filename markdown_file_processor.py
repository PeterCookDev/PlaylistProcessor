import codecs
import stringprocessing as sp
import os
import re

from file_processor import FileProcessor


class MarkdownFileProcessor(FileProcessor):

    def __init__(self, input_path):
        super().__init__(input_path)

    def process_markdown_list_into_dictionary(self, path, current_dictionary):

        with codecs.open(path, "r", encoding='ascii', errors='ignore') as f:
            for line in f:
                if line.startswith('- ['):
                    url = sp.get_url_from_line(line)
                    if url not in current_dictionary:
                        current_dictionary.append(url)
            f.close()

        return current_dictionary


    def get_known_urls(self, existing_path):

        known_urls = []
        all_files = os.listdir(existing_path)

        for filename in all_files:
            if filename.endswith(".md"):
                full_path = existing_path + "\\" + filename
                known_urls = self.process_markdown_list_into_dictionary(full_path, known_urls)

        return known_urls


    def process_files(self):
        return self.get_known_urls(self.input_path)