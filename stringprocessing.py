import re


def only_whitespace(line):
    """Return true if the line does only consist of whitespace characters."""
    for c in line:
        if c is not ' ' and c is not '  ':
            return c is ' '
    return line


def is_known_fixed_token(line):

    fixed_tokens = ['[ ![]', '[\+ More details]', '[Watch Later]', '[Upload]', '[Date]', '[Alphabetical]',
                   '[Alphabetical]', '[Plays]', '[Likes]', '[Comments]', '[Customize]', '[s]', '[Duration]']

    for s in fixed_tokens:
        if s in line:
            return True

    return False

def is_known_regular_expression_match(line):

    regex_list = ["\\* Play next", "\\* Play now", "\\* Move to top", "\\* Move to bottom", "\\* Add / edit notes",
                  "\\* Set as playlist thumbnail", "More", "\\*."]

    for s in regex_list:
        if re.match(s, line):
            return True

    return False


def strip_constant_tokens(line):

    if is_known_fixed_token(line):
        return ""

    if is_known_regular_expression_match(line):
        return ""

    if re.match("\d+:\d\d:\d\d", line) or re.match("\d\d:\d\d", line):
        return "[" + line.rstrip() + "]"

    if '/watch' in line:
        newvalue = line.replace('/watch', 'https://www.youtube.com/watch')
        newvalue = newvalue.replace('&list=WL', '')

        newvalue = scrub_youtube_slug(newvalue, 'list')
        newvalue = scrub_youtube_slug(newvalue, 'index')

        return newvalue

    if line.startswith('#'):
        return ""

    if line.startswith('[ ](//vimeo.com)'):
        return ""

    if line.startswith('by '):
        return ""

    return line


def scrub_youtube_slug(line, slug):
    full_slug = '&' + slug + '='

    if full_slug in line:
        index = line.index(full_slug)
        line = line[:index] + ')'
    return line


def is_vimeo_link(line):
    url = get_url_from_line(line)
    return url.startswith('/')


def get_url_from_line(line):
    if '(' in line and ')' in line:
        opening = line.index('(')
        closing = line.index(')')
        url = line[opening + 1:closing]
        return url

    return line