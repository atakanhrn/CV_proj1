import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2

##########################################
## Do not forget to delete "return NotImplementedError"
## while implementing a function
########################################

class App(QMainWindow):

    def __init__(self):

        super(App, self).__init__()

        #return NotImplementedError


        self.title = 'Histogram Equalization'

        # You can define other things in here
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

        inputImage = cv2.imread(fileName,cv2.IMREAD_COLOR)
        #cv2.namedWindow("main window")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        lay.addWidget(label)
        self.show()




        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        histogram_red = np.zeros([256,1], dtype=np.uint8)
        histogram_green = np.zeros([256, 1], dtype=np.uint8)
        histogram_blue = np.zeros([256, 1], dtype=np.uint8)

        return inputImage
        #for g in range(256):

        #return NotImplementedError

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

        inputImage = cv2.imread(fileName, cv2.IMREAD_COLOR)
        # cv2.namedWindow("main window")
        lay = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(1000,500)
        lay.addWidget(label)
        lay.addStretch()

        #self.setGeometry(300, 300, 250, 150)
        label.show()

        self.show()
        

        return inputImage

    def initUI(self):
        #return NotImplementedError
        # Write GUI initialization code
        #self.setWindowTitle(self.title)
        #self.setAccessibleName("main window")
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        openInput = QAction('Open Input', self)
        openTarget = QAction('Open Target', self)
        exit = QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        fileMenu.addAction(openInput)
        fileMenu.addAction(openTarget)
        fileMenu.addAction(exit)

        self.toolbar = self.addToolBar('Equalize Histogram')
        equalize = QAction('Equalize Histogram', self)
        self.toolbar.addAction(equalize)

        openInput.triggered.connect(self.openInputImage)
        openTarget.triggered.connect(self.openTargetImage)
        #exit.triggered.connect(app.exit())
        equalize.triggered.connect(self.histogramButtonClicked)


        self.show()

    def histogramButtonClicked(self):
        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            return NotImplementedError
        if not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            return NotImplementedError
        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            return NotImplementedError

    def calcHistogram(self, I):
        # Calculate histogram

        return hist

class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        #return NotImplementedError
        # Plot histogram

        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setAccessibleName("main window")
    sys.exit(app.exec_())
