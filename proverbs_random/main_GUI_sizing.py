import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, 
                             QHBoxLayout, QSizePolicy, QSpacerItem)
from PyQt5.QtGui import QFont

class App(QWidget):
    def __init__(self, filename):
        super().__init__()
        self.data = self.load_key_value_pairs(filename)
        self.keys = list(self.data.keys())
        self.current_index = random.randint(0, len(self.keys) - 1)
        self.init_ui()

    def init_ui(self):
        self.resize(100, 200)

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        font = QFont()
        font.setPointSize(14)

        self.verse_label = QLabel("", self)
        self.verse_label.setFont(font)
        self.verse_label.setWordWrap(True)
        layout.addWidget(self.verse_label)

        layout.addStretch(1)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)  

        btn = QPushButton("Get Random Verse", self)
        btn.setFont(font)
        btn.clicked.connect(self.display_random_verse)
        btn.setFixedSize(300, 40)
        btn_layout.addWidget(btn)

        btn_layout.addStretch(1)

        layout.addLayout(btn_layout)  

        layout.addStretch(0)

        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(0)
        nav_layout.setContentsMargins(0, 0, 0, 0)

        prev_btn = QPushButton("Previous", self)
        prev_btn.setFont(font)
        prev_btn.clicked.connect(self.display_previous_verse)
        prev_btn.setFixedSize(150, 40)
        nav_layout.addWidget(prev_btn)

        next_btn = QPushButton("Next", self)
        next_btn.setFont(font)
        next_btn.clicked.connect(self.display_next_verse)
        next_btn.setFixedSize(150, 40)
        nav_layout.addWidget(next_btn)

        layout.addLayout(nav_layout)

        self.setLayout(layout)
        self.setWindowTitle('Random Proverb')
        self.show()




    def load_key_value_pairs(self, filename):
        data = {}
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                data[key] = value

        return data

    def display_next_verse(self):
        self.current_index = (self.current_index + 1) % len(self.keys)
        key = self.keys[self.current_index]
        self.verse_label.setText(self.data[key])

    def display_previous_verse(self):
        self.current_index = (self.current_index - 1) % len(self.keys)
        key = self.keys[self.current_index]
        self.verse_label.setText(self.data[key])

    def display_random_verse(self):
        self.current_index = random.randint(0, len(self.keys) - 1)
        key = self.keys[self.current_index]
        self.verse_label.setText(self.data[key])

def main():
    app = QApplication(sys.argv)
    ex = App("verses.txt")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
