
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('WIdgets')

        self.combobox = QComboBox()
        self.combobox.addItems(['Item', 'item', 'Eithem'])
        self.combobox.currentIndexChanged.connect(self.selected)

        '''
        self.checkbox = QCheckBox('check')
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.selected)
        '''

        #label = QLabel("Hello World")


        ''' Line Edits
        line_edit = QLineEdit()
        #line_edit.setEchoMode(QLineEdit.Password)
        #line_edit.setText('Hello World')
        #line_edit.selectAll()
        #line_edit.setReadOnly(True)
        
        print(line_edit.text())

        line_edit.setPlaceholderText('Test')
        print(line_edit.placeholderText())

        layout.addWidget(line_edit)
        '''


        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout = QVBoxLayout()
        #layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)
        #layout.addWidget(label)

        self.setLayout(layout)
        #self.setFocus()

    def selected(self):

        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_index + ": " + current_text)

        '''
        if self.checkbox.isChecked():
            print("YAY")
        else:
            print("No :(")
        '''

app = QApplication(sys.argv)
dl = QWidgetDemos()
dl.show()
app.exec_()