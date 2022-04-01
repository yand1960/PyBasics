from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class HelloWindow(QWidget):

    def __init__(self):
        # super() - это отсылка к предку
        # Так что это вызов конструктора предка (QWidget'а)
        super().__init__()

        self.setFixedHeight(200)
        self.setFixedWidth(300)
        self.setWindowTitle("Hello")

        self.txt = QLineEdit(self)
        self.txt.setGeometry(10, 50, 280, 20)

        # Self - здесь не маркер, в указание родтельского элемента
        self.btn = QPushButton(self)
        self.btn.setGeometry(10,80,280,40)
        self.btn.setText("Click me!")
        self.btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        # print("Hello, world!")
        # self.setWindowTitle("hello, world!")
        user = self.txt.text()
        self.btn.setText(f"Hello, {user}!")

if __name__ == "__main__":
    app = QApplication([])
    window = HelloWindow()
    app.exec()