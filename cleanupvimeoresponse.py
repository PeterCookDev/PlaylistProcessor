import os
import json
import codecs

import markdown_file_processing as mfp
import link_processing as lp


def process_json_file_to_dictionary(fullpath, known_urls):
    links = []
    with codecs.open(fullpath, "r", encoding='ascii', errors='ignore') as data_file:
        data = json.load(data_file)
        for data_item in data['body']['data']:
            title = data_item['name'].strip()
            snippet_id = data_item['link']
            current_line = '[' + title + '](' + snippet_id + ')'
            links.append(current_line)

    return links

def preprocess_json(fullpath):
    with codecs.open(fullpath, "r", encoding='ascii', errors='ignore') as data_file:
        #data = json.load(data_file)
        data = data_file.read()

    new_filename = fullpath + ".new"
    body = data.replace("   ", "")
    body = body.replace('\\\\\\"', "\\")
    body = body.replace('\\n', '')
    body = body.replace('"https:\\\/\\\/vimeo.com', "'https:\/\/vimeo.com")
    body = body.replace("\\", "")
    body = body.replace('"{', "{")
    body = body.replace('}"', "}")
 
    with codecs.open(new_filename, 'w', encoding='ascii', errors='ignore') as w:
        w.write(body)
        w.close()

    return new_filename

def processjson(inputpath):
    known_urls = []
    all_files = os.listdir(inputpath)
    for filename in all_files:
        if filename.endswith(".response"):
            full_path = inputpath + "\\" + filename
            new_filename = preprocess_json(full_path)
            known_urls.extend(process_json_file_to_dictionary(new_filename, known_urls))

    return known_urls

def main():

    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    links = processjson(input_path)

    known_urls = mfp.get_known_urls(existing_path)

    new_links = lp.find_new_links(links, known_urls)

    for new_link in new_links:
        print('- ', new_link)

    print(len(new_links))

if __name__ == "__main__":
    main()