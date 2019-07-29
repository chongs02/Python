import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Exam(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		btn = QPushButton('hi there', self)
		btn.resize(btn.sizeHint())
		btn.move(20,30)
		btn.setToolTip('안녕하세요<b>굵은글씨</b>')

		self.setGeometry(300,300,400,500)
		self.setWindowTitle('첫번째tool')

		self.show()


app = QApplication(sys.argv)
w = Exam()

# 이벤트 처리
sys.exit(app.exec_())

