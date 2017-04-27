class LinkCleaner:

    def __init__(self):
        tokens = [', LSC14', 'RailsConf 2016 - ', '33rd Degree 2014 - ', ' - PyCon 2016', 'Ruby On Ales 2016: ']
        tokens.extend(['DevOpsDays Seattle 2016 - ', 'GORUCO 2016 - ', 'Full Stack Fest 2015: '])
        tokens.extend([' - PyCon 2015', 'ArrrrCamp 2015 - ', 'RubyConf 2015 - ', 'GOTO 2015  ', 'e4e Developer Conf 2015 - '])
        tokens.extend(['Ruby On Ales 2015 - ', 'Cascadia Ruby 2014- ', 'Rails Pacific 2016 - ', 'GOTO 2016  ','Rocky Mountain Ruby 2016 -'])
        tokens.extend(['GeeCON 2016: ','u00d8redev 2016 - ','GeeCON 2014: ','GeeCON TDD 2015: ','GeeCON 2013: - ','YOW! 2015 - ','OSFeels 2016 - '])
        tokens.extend(['PyDX 2015: ','PyDX 2016: ','CodeDaze 2016 - ','Keep Ruby Weird 2016 - ','RubyConf 2016 -','YOW! CTO Summit 2016 ','DevTernity 2016: ','YOW! 2016 '])

        self.tokens = tokens


    def clean_link(self, to_replace):
        for token in self.tokens:
            to_replace = to_replace.replace(token, "")

        to_replace = to_replace.replace(' | ',' - ')

        return to_replace


    def clean_links(self, links):
        new_links = []

        for link in links:
            new_links.append(self.clean_link(link))

        return new_links


