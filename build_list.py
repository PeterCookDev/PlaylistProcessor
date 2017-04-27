from vimeo_response_processor import VimeoResponseProcessor 
from youtube_to_watch_list_processor import YoutubeToWatchListProcessor
from markdown_file_processor import MarkdownFileProcessor
from link_cleaner import LinkCleaner
import stringprocessing as sp


def find_new_links(links, known_links):
    new_links = []

    for link in links:
        url = sp.get_url_from_line(link)
        if url not in known_links:
            new_links.append(link)

    return new_links

def find_duplicate_links(links, known_links):
    duplicate_links = []

    for link in links:
        url = sp.get_url_from_line(link)
        if url not in known_links:
            duplicate_links.append(link)

    return duplicate_links



def print_links(links):
    for link in links:
        print('- ', link)

def main():
    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    vimeo_response_processor = VimeoResponseProcessor(input_path)
    v_links = vimeo_response_processor.process_files()

    youtube_to_watch_list_processor = YoutubeToWatchListProcessor(input_path)
    yt_links = youtube_to_watch_list_processor.process_files()

    links = []
    links.extend(v_links)
    links.extend(yt_links)

    link_cleaner = LinkCleaner()
    cleaned_links = link_cleaner.clean_links(links)

    markdown_file_processor = MarkdownFileProcessor(existing_path)
    known_urls = markdown_file_processor.process_files()


#    dupes = find_duplicate_links(cleaned_links, known_urls)
#    print('Duplicates')
#    print('============================================================================')
#    print_links(dupes)
#    print()
#    print()

    new_links = find_new_links(cleaned_links, known_urls)
    print('New - ', len(new_links), 'links')
    print('============================================================================')
    print_links(new_links)


if __name__ == "__main__":
    main()