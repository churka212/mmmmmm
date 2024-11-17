import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class UserInfoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Форма')
        layout = QVBoxLayout(self)
        self.number_input, self.name_input = QLineEdit(), QLineEdit()
        layout.addWidget(self.number_input)
        layout.addWidget(self.name_input)
        submit_button = QPushButton('Підтвердити', self)
        result_label = QLabel(self)
        layout.addWidget(submit_button)
        layout.addWidget(result_label)

        submit_button.clicked.connect(lambda: result_label.setText(f'Число: {self.number_input.text()}\nІм\'я: {self.name_input.text()}') 
                                      if self.number_input.text().isdigit() and len(self.number_input.text()) == 14 else result_label.setText('Помилка!'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = UserInfoForm()
    form.show()
    sys.exit(app.exec_())