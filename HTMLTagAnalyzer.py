from PyQt5 import QtWidgets, uic
from bs4 import BeautifulSoup as Bs4
import requests
import sys
import tld


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("HTMLTagAnalyzerTable.ui", self)
        self.pushButton.clicked.connect(self.onClick)
        self.tableWidget.setHorizontalHeaderLabels(['HTML Tag ID', 'Occurrences'])

    def onClick(self):
        url = self.lineEdit.text()
        tagsAndCounts = parseHTML(url)
        self.fillTable(tagsAndCounts)
        self.lineEdit.clear()

    def fillTable(self, tagsAndCounts):
        row = 0
        for key, value in tagsAndCounts.items():
            tag = QtWidgets.QTableWidgetItem(key)
            count = QtWidgets.QTableWidgetItem(str(value))
            self.tableWidget.setItem(row, 0, tag)
            self.tableWidget.setItem(row, 1, count)
            row += 1


def parseHTML(url):
    page = requests.get(url)
    soup = Bs4(page.content, 'html.parser')

    tagDict = {}

    for tag in soup.findAll():
        if tag.name in tagDict.keys():
            tagDict[tag.name] += 1
        else:
            tagDict[tag.name] = 1

    return tagDict


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    sys.exit(app.exec())
