import sys
from datetime import datetime
from PySide6.QtCore import Slot 
from PySide6.QtWidgets import QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent=parent)

        self.edit = QLineEdit("Hellow World")
        self.button = QPushButton("Click")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.btn_hello)

    @Slot()
    def btn_hello(self):
        print("압력 날짜: ", datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
        print("현재 입력한 값: ", self.edit.text().strip())

try:
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        
        form = Form()
        form.show()

        sys.exit(app.exec())
except Exception as err:
    print("에러 발생: ", err)



