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
    inputImage = np.uint8
    targetImage = np.uint8
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

        self.inputImage = cv2.imread(fileName,cv2.IMREAD_COLOR)
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
        hist = self.calcHistogram(self.inputImage)

        print(hist)
        #index = np.arange(len(hist))
        #plt.bar(index, hist)
        #plt.show()


        # plt.legend(loc='upper right')




        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        histogram_red = np.zeros([256,1], dtype=np.uint8)
        histogram_green = np.zeros([256, 1], dtype=np.uint8)
        histogram_blue = np.zeros([256, 1], dtype=np.uint8)


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

        self.targetImage = cv2.imread(fileName, cv2.IMREAD_COLOR)
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

        hist = self.calcHistogram(self.targetImage)

        print(hist)
        #index = np.arange(len(hist))
        #plt.bar(index, hist)
        #plt.show()


        # plt.legend(loc='upper right')

        #red_hist = hist[:, 0, 1]
        #plotCanvas = PlotCanvas(hist)
        #plotCanvas = PlotCanvas(hist)
        #plotCanvas.plotHistogram(hist)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        #histogram_red = np.zeros([256, 1], dtype=np.uint8)
        #histogram_green = np.zeros([256, 1], dtype=np.uint8)
        #histogram_blue = np.zeros([256, 1], dtype=np.uint8)

        #return targetImage

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
        #if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
         #   return NotImplementedError
        #if not self.inputLoaded:
            # Error: "Load input image" in MessageBox
         #   return NotImplementedError
        #elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
         #   return NotImplementedError
        #construct PDF
        self.createCDF(self.inputImage)
        self.createCDF(self.targetImage)

        #construct CDF
        #construct LUT

    def createCDF(self, image):
        hist = self.calcHistogram(image)
        imagePdf = self.getPdfFromHist(hist)
        sum = 0
        for i in range(len(hist)):
            sum = sum + imagePdf[i]
            imagePdf[i] = sum
        index = np.arange(len(imagePdf))
        plt.bar(index, imagePdf)
        # plt.legend(loc='upper right')
        plt.show()
    def getPdfFromHist(self, hist):
        sum = hist.sum()
        for i in range(len(hist)):
            hist[i] = hist[i]/sum
        return hist
    def calcHistogram(self, I):
        # Calculate histogram
        R, C, B = I.shape
        # allocate the histogram
        hist = np.zeros([256])
        # range through the intensity values
        for row in range(R):
            for column in range(C):
                hist[I[row,column,2]] = hist[I[row,column,2]] + 1

        return hist


class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        #return NotImplementedError
        # Init Canvas
        super(PlotCanvas,self).__init__()
        #fig = plt.hist(hist)
        #FigureCanvas.__init__(self)
        #FigureCanvas.__init__(self, self.figure)
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        #return NotImplementedError
        # Plot histogram
        print(hist)
        #index = np.arange(len(hist))
        #plt.bar(index, hist)
        # plt.legend(loc='upper right')
        #plt.show()
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setAccessibleName("main window")
    sys.exit(app.exec_())
