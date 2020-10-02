from PySide2.QtWidgets import QPushButton, QApplication
import sys
from mainwindow import MainWindow

#pyside2-uic mainwindow.ui > ui_mainwindow.py
# Aplicación de Qt
app = QApplication()
window = MainWindow()
window.show()
# Qt loop
sys.exit(app.exec_())