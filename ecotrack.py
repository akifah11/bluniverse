import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QDateEdit, QComboBox, QLineEdit, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import QDate

class SampahEntry:
    def __init__(self, tanggal, jenis, berat):
        self.tanggal = tanggal
        self.jenis = jenis
        self.berat = berat

class SampahManager:
    def __init__(self):
        self.entries = []

    def tambah_entry(self, entry):
        self.entries.append(entry)

    def hapus_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]

    def total_hari_ini(self, tanggal):
        return sum(entry.berat for entry in self.entries if entry.tanggal == tanggal)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EcoTrack - Pengelola Sampah Rumah Tangga")
        self.manager = SampahManager()
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()

        # Input section
        input_layout = QHBoxLayout()
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())

        self.combo_jenis = QComboBox()
        self.combo_jenis.addItems(["Organik", "Anorganik", "B3 (Berbahaya)"])

        self.lineedit_berat = QLineEdit()
        self.lineedit_berat.setPlaceholderText("Berat (kg)")

        self.btn_tambah = QPushButton("Tambah Data")
        self.btn_tambah.clicked.connect(self.tambah_data)

        input_layout.addWidget(self.date_edit)
        input_layout.addWidget(self.combo_jenis)
        input_layout.addWidget(self.lineedit_berat)
        input_layout.addWidget(self.btn_tambah)

        # Table section
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Tanggal", "Jenis", "Berat (kg)", "Aksi"])

        # Statistik & Tips
        self.label_statistik = QLabel("Total berat hari ini: 0.0 kg")
        self.label_tips = QLabel("Tips: Pisahkan sampah organik untuk kompos!")

        layout.addLayout(input_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.label_statistik)
        layout.addWidget(self.label_tips)

        main_widget.setLayout(layout)

    def tambah_data(self):
        try:
            tanggal = self.date_edit.date().toString("yyyy-MM-dd")
            jenis = self.combo_jenis.currentText()
            berat = float(self.lineedit_berat.text())

            if berat <= 0:
                raise ValueError("Berat harus lebih dari 0")

            entry = SampahEntry(tanggal, jenis, berat)
            self.manager.tambah_entry(entry)
            self.populate_table()
            self.update_statistik()
            self.lineedit_berat.clear()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def populate_table(self):
        self.table.setRowCount(len(self.manager.entries))
        for i, entry in enumerate(self.manager.entries):
            self.table.setItem(i, 0, QTableWidgetItem(entry.tanggal))
            self.table.setItem(i, 1, QTableWidgetItem(entry.jenis))
            self.table.setItem(i, 2, QTableWidgetItem(f"{entry.berat:.2f}"))

            btn_hapus = QPushButton("Hapus")
            btn_hapus.clicked.connect(lambda _, row=i: self.hapus_data(row))
            self.table.setCellWidget(i, 3, btn_hapus)

    def hapus_data(self, row):
        self.manager.hapus_entry(row)
        self.populate_table()
        self.update_statistik()

    def update_statistik(self):
        today = QDate.currentDate().toString("yyyy-MM-dd")
        total = self.manager.total_hari_ini(today)
        self.label_statistik.setText(f"Total berat hari ini: {total:.2f} kg")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(700, 400)
    window.show()
    sys.exit(app.exec_())
