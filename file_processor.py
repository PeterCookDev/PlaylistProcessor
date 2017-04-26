from abc import ABCMeta
from abc import abstractmethod

class FileProcessor(metaclass = ABCMeta):

    def __init__(self, input_path):
        self.input_path = input_path


    @abstractmethod
    def process_files(self):
        pass