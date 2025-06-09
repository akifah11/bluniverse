import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QMessageBox
)
from PyQt6.QtCore import Qt

class SimpleBookTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daftar Buku Yang Akan Dibaca")
        self.setGeometry(200, 200, 450, 350) 

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        main_layout.addWidget(QLabel("Judul Buku:"))
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Masukkan judul buku di sini")
        main_layout.addWidget(self.title_input)

        self.add_button = QPushButton("Tambah Buku")
        self.add_button.clicked.connect(self.add_book)
        main_layout.addWidget(self.add_button)

        main_layout.addWidget(QLabel("Daftar Buku yang Telah Dibaca:"))
        self.book_list_widget = QListWidget()
        self.book_list_widget.itemChanged.connect(self.update_book_status)
        main_layout.addWidget(self.book_list_widget)

        self.load_sample_books()

    def add_book(self):
        """Menambah buku ke daftar ketika tombol 'Tambah Buku' diklik."""
        title = self.title_input.text().strip()

        if not title:
            QMessageBox.warning(self, "Peringatan", "Judul buku tidak boleh kosong!")
            return

        item = QListWidgetItem(title)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setCheckState(Qt.CheckState.Unchecked) 
        item.setForeground(Qt.GlobalColor.black) 

        self.book_list_widget.addItem(item)
        self.title_input.clear() 
        QMessageBox.information(self, "Sukses", f"Buku '{title}' berhasil ditambahkan!")

    def update_book_status(self, item):
        """Mengubah warna teks item berdasarkan status centang (dibaca/belum dibaca)."""
        if item.checkState() == Qt.CheckState.Checked:
            item.setForeground(Qt.GlobalColor.gray) 
        else:
            item.setForeground(Qt.GlobalColor.black) 

    def load_sample_books(self):
        """Memuat beberapa buku contoh ke dalam daftar."""
        sample_titles = ["Laskar Pelangi", "Bumi Manusia", "Negeri 5 Menara"]
        for title in sample_titles:
            item = QListWidgetItem(title)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked) 
            item.setForeground(Qt.GlobalColor.black)
            self.book_list_widget.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBookTracker()
    window.show()
    sys.exit(app.exec())