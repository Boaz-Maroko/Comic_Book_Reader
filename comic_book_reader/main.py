import sys
import os
import zipfile
import rarfile
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ComicBookReader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Comic Book Reader")
        self.setGeometry(100, 100, 800, 600)

        # UI components
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(scene=self.scene)
        self.open_button = QPushButton("Open Comic")
        self.next_button = QPushButton("Next Page")
        self.previous_button = QPushButton("Prev Page")

        # Layout Components
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.open_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.previous_button)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Variables
        self.images = []
        self.current_page = 0

        # Button Signals
        self.open_button.clicked.connect(self.open_file_dialog) 
        self.next_button.clicked.connect(self.next_page)
        self.previous_button.clicked.connect(self.prev_page)

    def open_file_dialog(self):
        # Open file dialog to select a CBZ or CBR file
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Comic Book", "", "Comic Files (*.cbz *.cbr);;All Files (*)"
        )
        if file_path:
            try:
                self.open_comic(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open comic: {e}")

    def open_comic(self, file_path: str) -> None:
        if file_path.endswith(".cbz"):
            self.image_files = self.extract_cbz(file_path)
        elif file_path.endswith(".cbr"):
            self.image_files = self.extract_cbr(file_path)

        self.current_page = 0
        self.display_page()

    def extract_cbz(self, file_path: str) -> list:
        extracted_files = []
        temp_dir = "temp_comic"
        os.makedirs(temp_dir, exist_ok=True)

        with zipfile.ZipFile(file_path, 'r') as archive:
            archive.extractall(temp_dir)
            extracted_files = sorted([os.path.join(temp_dir, image_file) for image_file in archive.namelist() if image_file.lower().endswith(('png', 'jpeg', 'jpg'))])
        
        return extracted_files
    
    def extract_cbr(self, file_path: str) -> list[str]:
        extracted_files = []
        temp_dir = "temp_comic"
        os.makedirs(temp_dir, exist_ok=True)

        with rarfile.RarFile(file_path, "r") as archive:
            archive.extractall(temp_dir)
            extracted_files = sorted(
                [os.path.join(temp_dir, f) for f in archive.namelist() if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            )
        return extracted_files
    
    def display_page(self):
        if 0 <= self.current_page < len(self.image_files):
            image_path = self.image_files[self.current_page]
            pixmap = QPixmap(image_path)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.view.setScene(self.scene)
            self.view.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)

    def next_page(self):
        if self.current_page < len(self.image_files) - 1:
            self.current_page += 1
            self.display_page()

                                     
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reader = ComicBookReader()
    reader.show()
    sys.exit(app.exec())