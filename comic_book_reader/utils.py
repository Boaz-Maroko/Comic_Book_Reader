import zipfile
import os
from pyunpack import Archive


class Extraction:
    """An Object that extracts the comic book files and images"""

    def __init__(self, comic_file, extract_to) -> None:
        self.comic_file = comic_file
        self.extract_to = extract_to
        
    def __str__(self) -> str:
        return "Extraction"

    def extract_cbz(self):
        with zipfile.ZipFile(self.comic_file, 'r') as zip_ref:
            # Loop through each file in the zip and extract to the target folder
            for file_name in zip_ref.namelist():
                # Construct full path for extraction
                extracted_path = os.path.join(self.extract_to, os.path.basename(file_name))
                zip_ref.extract(file_name, self.extract_to)
                
        name = os.path.basename(self.comic_file)
        name_without_extension = os.path.splitext(name)[0]

        return name_without_extension.strip()


    def extract_cbr(self):
        """Extracts cbr type comics"""
        Archive(self.comic_file).extractall(self.extract_to)


