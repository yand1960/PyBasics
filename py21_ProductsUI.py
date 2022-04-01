from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit
from py20_DataLayer import Repository

class ProductWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 400)
        self.setWindowTitle("Products")

        self.txtFilter = QLineEdit(self)
        self.txtFilter.setGeometry(10,10, 280, 20)
        self.txtFilter.textChanged.connect(self.showProducts)

        self.txtDisplay = QTextEdit(self)
        self.txtDisplay.setGeometry(10, 40, 280, 350)

        self.show()

    def showProducts(self):
        repository = Repository()
        products = repository.getFilteredProducts(self.txtFilter.text())
        out = ""
        for p in products:
            # print(p['name'])
            out += f"{p['name']:35}\t{p['price']}\n"
        self.txtDisplay.setText(out)

if __name__ == "__main__":
    app = QApplication([])
    window = ProductWindow()
    app.exec()