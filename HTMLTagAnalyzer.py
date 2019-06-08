from PyQt5 import QtWidgets, uic
from bs4 import BeautifulSoup as Bs4
from tld import get_tld
import requests
import sys


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("HTMLTagAnalyzerTable.ui", self)
        self.pushButton.clicked.connect(self.onClick)
        self.tableWidget.setHorizontalHeaderLabels(['HTML Tag ID', 'Occurrences'])

    def onClick(self):
        self.clearTable()
        url = self.lineEdit.text()
        self.parseHTML(url)

    def fillTable(self, tagsAndCounts):
        row = 0
        for key, value in tagsAndCounts.items():
            tag = QtWidgets.QTableWidgetItem(key)
            count = QtWidgets.QTableWidgetItem(str(value))
            self.tableWidget.setItem(row, 0, tag)
            self.tableWidget.setItem(row, 1, count)
            row += 1

    def clearTable(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(''))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(''))

    def validURL(self, url, tagsAndCounts):
        self.fillTable(tagsAndCounts)
        self.lineEdit.clear()
        res = get_tld(url, as_object=True)
        self.label_2.setText(str(res.fld))

    def invalidURL(self):
        self.lineEdit.clear()
        self.label_2.setText('Invalid Entry')

    def parseHTML(self, url):
        if not url.startswith('https://'):
            self.invalidURL()
        else:
            page = requests.get(url)
            if page.status_code != 200:
                self.invalidURL()
            else:
                soup = Bs4(page.content, 'html.parser')

                tagDict = {}

                for tag in soup.findAll():
                    if tag.name in tagDict.keys():
                        tagDict[tag.name] += 1
                    else:
                        tagDict[tag.name] = 1

                self.validURL(url, tagDict)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    sys.exit(app.exec())
