from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request


class Downloader (QDialog):

    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        self.url.setPlaceholderText('Url...')
        self.save_location.setPlaceholderText('file...')

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle('PyDownloader')
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse)

    def browse(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save FIle as", directory=".", filter="All Files (*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The Download Failed")
            return

        QMessageBox.information(self, "Information", "The Download is completed")
        self.progress.setValue(0)
        self.url.setText('')
        self.save_location.setText('')

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize;
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))





app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()