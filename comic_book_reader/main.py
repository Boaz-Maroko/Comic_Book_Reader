import os
from tkinter import Label, filedialog, Button, Tk
from PIL import Image, ImageTk
from utils import Extraction

APP_PATH = '/home/boaz/code/projects/Comic_Reader/comic_book_reader'


class ComicReader:

    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Comic Reader")
        self.page_index = 0
        self.images = []

        self.image_label = Label(root)
        self.image_label.pack()

        Button(root, text="Open Comic", command=self.open_comic).pack()
        Button(root, text="Previous", command=self.prev_page).pack()
        Button(root, text="Next", command=self.next_page).pack()

    def open_comic(self):
        """Opens the comic book archive and reads the extension
        if it is .cbz file it calls the load_comic method approprietly
        """
        file_path = filedialog.askopenfilename(filetypes=[("CBZ Files", "*.cbz"), ("CBR Files", "*.cbr"), ("All Files", "*.*")])
        if file_path.endswith(".cbz"):
            self.load_comic(file_path, is_cbz=True)
        elif file_path.endswith(".cbr"):
            self.load_comic(file_path, is_cbz=False)

    
    def load_comic(self, file_path, is_cbz):
        extract_to = "temp_comic"
        os.makedirs(extract_to, exist_ok=True)

        if is_cbz:
            sub_folder = Extraction(file_path, extract_to).extract_cbz()
        else:
            Extraction(file_path, extract_to).extract_cbr()

        self.images = sorted([os.path.join(f"{extract_to}/{sub_folder}", f) for f in os.listdir(f"{extract_to}/{sub_folder}")])
        print(f"Indentified: {self.images}")
        self.page_index = 0
        self.display_page()

    def display_page(self):
        if 0 <= self.page_index < len(self.images):
            image_path = self.images[self.page_index]
            img = Image.open(image_path)
            img.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(img)

            self.image_label.config(image=photo)
            self.image_label.image = photo

    def next_page(self):
        if self.page_index < len(self.images) -1:
            self.page_index += 1
            self.display_page()


    def prev_page(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.display_page()
        
if __name__== "__main__":
    root = Tk()
    app = ComicReader(root)
    root.mainloop()

                
