import stringprocessing as sp


def find_new_links(links, known_links):
    new_links = []

    for s in links:
        url = sp.get_url_from_line(s)
        if url not in known_links:
            new_links.append(token_replacement(s))

    return new_links


def token_replacement(to_replace):
    tokens = [', LSC14', 'RailsConf 2016 - ', '33rd Degree 2014 - ', ' - PyCon 2016', 'Ruby On Ales 2016: ']
    tokens.extend(['DevOpsDays Seattle 2016 - ', 'GORUCO 2016 - ', 'Full Stack Fest 2015: '])
    tokens.extend([' - PyCon 2015', 'ArrrrCamp 2015 - ', 'RubyConf 2015 - ', 'GOTO 2015 ', 'e4e Developer Conf 2015 - '])
    tokens.extend(['Ruby On Ales 2015 - ', 'Cascadia Ruby 2014- ', 'Rails Pacific 2016 - ', 'GOTO 2016 '])

    for token in tokens:
        to_replace = to_replace.replace(token, "")

    return to_replace
