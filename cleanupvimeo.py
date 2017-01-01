import markdown_file_processing as mfp
import link_processing as lp


def main():

    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    mfp.translate_files_from_html_to_markdown(input_path, '.txt')
    links = mfp.process_files_into_list_of_links(input_path)

    known_urls = mfp.get_known_urls(existing_path)

    new_links = lp.find_new_links(links, known_urls)

    for s in new_links:
        print('- ', s)

if __name__ == "__main__":
    main()
