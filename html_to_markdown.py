import codecs
import stringprocessing as sp
import os
import re
import html2text

def process_files_into_list_of_links(path):

    links = []

    in_link = False
    current_line = ""

    all_files = os.listdir(path)
    for filename in all_files:
        if filename.endswith(".new"):

            full_path = path + "\\" + filename

            with codecs.open(full_path, "r", encoding='ascii', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    dataline = sp.strip_constant_tokens(line).strip('')

                    if not sp.only_whitespace(dataline):
                        # if not in a commentedout block look for the beginning of a commentedout block
                        if not in_link:
                            if dataline.startswith('[ ![]'):
                                in_link = False
                            elif dataline.startswith('['):
                                in_link = True

                        if in_link and re.match("\[\d+:", dataline):
                            current_line = current_line + " " + dataline
                        elif in_link:
                            current_line = current_line + dataline

                        # if in a commentedout block look for the ending
                        if in_link and re.match("\[\d+:", dataline):
                            in_link = False
                            if sp.is_vimeo_link(current_line) :
                                current_line = current_line.replace('(/', '(https://vimeo.com/')

                            links.append(current_line)
                            current_line = ""

    return links


def translate_files_from_html_to_markdown(path, filetype):

    all_files = os.listdir(path)

    for filename in all_files:
        if filename.endswith(filetype):
            full_path = path + "\\" + filename

            with codecs.open(full_path, "r", encoding='ascii', errors='ignore') as f:
                h = html2text.HTML2Text()
                data = f.read()
                body = h.handle(data)

                with codecs.open(full_path.replace(filetype, '.new'), 'w', encoding='ascii', errors='ignore') as w:
                    w.write(body)
                    w.close()
                    f.close()
