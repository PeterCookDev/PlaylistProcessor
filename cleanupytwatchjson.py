import os
import json
import codecs

import link_processing as lp
import markdown_file_processing as mfp



def process_json_file_to_dictionary(fullpath, known_urls):
    links = []
    with codecs.open(fullpath, "r", encoding='ascii', errors='ignore') as data_file:
        data = json.load(data_file)
        for data_item in data:
            title = data_item['snippet']['title'].strip()
            snippet_id = 'https://www.youtube.com/watch?v=' + data_item['contentDetails']['videoId']
            current_line = '[' + title + '](' + snippet_id + ')'
            links.append(current_line)
    return links

def find_duplicates(to_watch, enjoyed):
    for s in to_watch:
        if s in enjoyed:
            print('-', s)

def processjson(inputpath):
    known_urls = []
    # go get json files in the path
    all_files = os.listdir(inputpath)
    for filename in all_files:
        if filename.endswith(".json"):
            full_path = inputpath + "\\" + filename
            known_urls = process_json_file_to_dictionary(full_path, known_urls)

    return known_urls


def main():

    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    links = processjson(input_path)

    known_urls = mfp.get_known_urls(existing_path)

    new_links = lp.find_new_links(links, known_urls)

    for s in new_links:
        print('- ', s)

    print(len(new_links))

if __name__ == "__main__":
    main()