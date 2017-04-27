import html_to_markdown
import link_processing 

from markdown_file_processor import MarkdownFileProcessor

def main():

    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    html_to_markdown.translate_files_from_html_to_markdown(input_path, '.txt')
    links = html_to_markdown.process_files_into_list_of_links(input_path)

    markdown_file_processor = MarkdownFileProcessor(existing_path)
    known_urls = markdown_file_processor.process_files()

    new_links = link_processing.find_new_links(links, known_urls)

    for link in new_links:
        print('- ', link)

if __name__ == "__main__":
    main()
