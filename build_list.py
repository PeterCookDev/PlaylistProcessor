from vimeo_response_processor import VimeoResponseProcessor 

def main():
    path = "C:\\Projects\\Python\\PlaylistProcessor\\"

    input_path = path + "\\Content"
    existing_path = path + "\\Existing"

    a = VimeoResponseProcessor(input_path)
    links = a.process_files()

    for link in links:
        print(link)

if __name__ == "__main__":
    main()