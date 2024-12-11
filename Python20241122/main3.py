import os
from fileinput import filename
from os import write


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        do(self, filename)

    def do(self, filename):
        file = open(filename, "w")
        os.write(file, "SHUIDS")
