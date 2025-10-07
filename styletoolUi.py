try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

import importlib
from . import styletoolUtil as stylUtil
importlib.reload(stylutil)

IMAGE_DIR = "C:/Users/Pitinan/Documents/maya/2026/scripts/styletool/images"

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Style Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				font-family: Papyrus;
				backgground-color: #A124F2
			'''
		)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/EYE.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(64, 64),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaledPixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #F2C724, stop:1 #98F542);
					color: white;
					border-radius: 8px;
					font-family: Arial;
					font-weight: bold;
				}
			'''
		)

		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.selectButton = QtWidgets.QPushButton('Select')
		self.selectButton.setStyleSheet(
			'''
				QPushButton{
					background-color: E500F5;
					border-radius: 12px;
					font-size: 16ps;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px;
				}
				QPushButton:hover{
					backgorund-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed{
					background-color: green;
				}
			'''
			)
		self.selectButton.clicked.connect(self.onClickSelectButtonForRename)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.clicked.connect(self.close)
		self.buttonLayout.addWidget(self.selectButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

	def onClickSelectButtonForRename(self):
		name = self.nameLineEdit.text()
		stylUtil.renameSelection(name)
		


def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr =  wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()