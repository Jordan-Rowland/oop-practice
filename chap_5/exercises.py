from urllib.request import urlopen
import time

# Add timeout feature to refresh content from cache
class WebPage:
    def __init__(self, url, timeout=256):
        self.url = url
        self._content = None
        self.cache = 0
        self.timeout = timeout

    @property
    def content(self):
        now = time.time()
        if not self._content or now - self.cache > self.timeout:
            print('Retrieving New Page...')
            self.cache = time.time()
            self._content = urlopen(self.url).read()
        return self._content

    
# Ex.2, change ZipProcessor to use Composition
import shutil
import sys
import zipfile
from pathlib import Path


class ZipProcessor:
    """Modified to use composition"""
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = Path(f'unzipped-{zipname[:-4]}')
        self.processor = processor()

    def process_files(self):
        self.processor.process_files()

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        print(f'making {self.temp_directory}')
        print('files unzipped')

    def zip_files(self):
        print('zipping files')
        print(f'deleted {self.temp_directory}')


class ZipReplace():
    def process_files(self):
        """Perform a search and replace on all files in the temp directory"""
        print('ZipReplace processor')


class ScaleZip():
    def process_files(self):
        """Scale each image in the directory to 640x480"""
        print('ScaleZip processor')


# Ex.3, add error handling to the case study example
class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    @property
    def string(self):
        return ''.join((str(c) for c in self.characters))

    def insert(self, character):
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to the begenning of the file before newline
                break

    def end(self):
        while (
                self.position < len(self.document.characters)
                and self.document.characters[self.position].character != '\n'
            ):
            self.position += 1

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return f'{bold}{italic}{underline}{self.character}'

