import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog, QHBoxLayout, QTabWidget
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
    box2 = QGroupBox
    box1 = QGroupBox
    box3 = QGroupBox
    box4 = QGroupBox
    box5 = QGroupBox
    box6 = QGroupBox
    ver_lay = QVBoxLayout
    ver_lay2 = QVBoxLayout
    ver_lay3 = QVBoxLayout
    def __init__(self):
        QMainWindow.__init__(self)
        self.setup_main_window()
        self.set_window_layout()
        self.initUI()
    def setup_main_window(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        #self.resize(800, 600)
        self.setWindowTitle("Equalize histogram")

    def set_window_layout(self):
        self.startSimulationButton = QPushButton('Start Simulation')

        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.box1 = QGroupBox("Input")
        self.box2 = QGroupBox("Input Hist")
        self.box3 = QGroupBox("Target")
        self.box4 = QGroupBox("Target Hist")
        self.box5 = QGroupBox("Output")
        self.box6 = QGroupBox("Output Hist")
        self.ver_lay = QVBoxLayout()
        self.ver_lay2 = QVBoxLayout()
        self.ver_lay3 = QVBoxLayout()
        self.ver_lay.addWidget(self.box1)
        self.ver_lay.addWidget(self.box2)
        self.horizontalLayout.addLayout(self.ver_lay)
        self.ver_lay2.addWidget(self.box3)
        self.ver_lay2.addWidget(self.box4)
        self.horizontalLayout.addLayout(self.ver_lay2)
        self.ver_lay3.addWidget(self.box5)
        self.ver_lay3.addWidget(self.box6)
        self.horizontalLayout.addLayout(self.ver_lay3)
        #self.horizontalLayout.addWidget(self.box1)
        layout = QHBoxLayout()
        self.box1.setLayout(layout)
        layout2 = QHBoxLayout()
        self.box2.setLayout(layout2)
        layout3 = QHBoxLayout()
        self.box3.setLayout(layout3)
        layout4 = QHBoxLayout()
        self.box4.setLayout(layout4)
        layout5 = QHBoxLayout()
        self.box5.setLayout(layout5)
        layout6 = QHBoxLayout()
        self.box6.setLayout(layout6)
        #self.main_vertical_layout = QVBoxLayout()
        #self.box2.setLayout(self.main_vertical_layout)
        #self.main_vertical_layout.addStretch(1)
        #self.box1.layout().addStretch(1)

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
        #lay = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(20, 20)
        #lay.addWidget(label)
        #lay.addStretch()

        # self.setGeometry(300, 300, 250, 150)
        #label.show()
        fig = plt.figure(figsize=(5,5))
        self.box1.layout().addWidget(label)
        self.show()
        hist = self.calcHistogram(self.inputImage,2)
        hist1 = self.calcHistogram(self.inputImage,1)
        hist2 = self.calcHistogram(self.inputImage,0)
        index = np.arange(len(hist))
        a = fig.add_subplot(311)
        a.bar(index, hist)
        canvas = FigureCanvas(fig)
        #canvas.resize(50,25)
        self.box2.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist1))
        b = fig.add_subplot(312)
        b.bar(index, hist1)
        #canvas = FigureCanvas(fig)
        #canvas.resize(100,50)
        self.box2.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist2))
        c = fig.add_subplot(313)
        c.bar(index, hist2)
        #canvas = FigureCanvas(fig)
        #canvas.resize(100,50)
        self.box2.layout().addWidget(canvas)
        #fig.tight_layout()
        canvas.show()
        #print(hist)
        #index = np.arange(len(hist))
        #plt.bar(index, hist)
        #plt.show()


        # plt.legend(loc='upper right')




        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


        #for g in range(256):

        #return NotImplementedError

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,options = options)
        if fileName:
            print(fileName)

        self.targetImage = cv2.imread(fileName, cv2.IMREAD_COLOR)
        # cv2.namedWindow("main window")
        # lay = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(20, 20)
        # lay.addWidget(label)
        # lay.addStretch()

        # self.setGeometry(300, 300, 250, 150)
        # label.show()
        fig = plt.figure(figsize=(5, 5))
        self.box3.layout().addWidget(label)
        self.show()
        hist = self.calcHistogram(self.targetImage, 2)
        hist1 = self.calcHistogram(self.targetImage, 1)
        hist2 = self.calcHistogram(self.targetImage, 0)
        index = np.arange(len(hist))
        a = fig.add_subplot(311)
        a.bar(index, hist)
        canvas = FigureCanvas(fig)
        # canvas.resize(50,25)
        self.box4.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist1))
        b = fig.add_subplot(312)
        b.bar(index, hist1)
        # canvas = FigureCanvas(fig)
        # canvas.resize(100,50)
        self.box4.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist2))
        c = fig.add_subplot(313)
        c.bar(index, hist2)
        # canvas = FigureCanvas(fig)
        # canvas.resize(100,50)
        self.box4.layout().addWidget(canvas)
        # fig.tight_layout()
        canvas.show()
        # print(hist)
        # index = np.arange(len(hist))
        # plt.bar(index, hist)
        # plt.show()

        # plt.legend(loc='upper right')

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # for g in range(256):

        # return NotImplementedError

    def initUI(self):
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        #self.createGridLayout()
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



        #self.setLayout(windowLayout)


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
        #construct CDF

        R, C, B = self.inputImage.shape
        K = np.zeros((R, C, B))
        inputCDF = self.createCDF(self.inputImage, 2)
        targetCDF = self.createCDF(self.targetImage, 2)
        inputCDF1 = self.createCDF(self.inputImage, 1)
        targetCDF1 = self.createCDF(self.targetImage, 1)
        inputCDF2 = self.createCDF(self.inputImage, 0)
        targetCDF2 = self.createCDF(self.targetImage, 0)

        #construct LUT
        LUT = self.createLUT(inputCDF,targetCDF)
        LUT1 = self.createLUT(inputCDF1,targetCDF1)
        LUT2 = self.createLUT(inputCDF2,targetCDF2)

        print(LUT)
        for row in range(R):
            for column in range(C):
                self.inputImage[row][column][2] = LUT[self.inputImage[row][column][2]]
                self.inputImage[row][column][1] = LUT1[self.inputImage[row][column][1]]
                self.inputImage[row][column][0] = LUT2[self.inputImage[row][column][0]]
        K = self.inputImage
        hist = self.calcHistogram(K, 2)
        hist1 = self.calcHistogram(K, 1)
        hist2 = self.calcHistogram(K, 0)
        #K = np.uint8(LUT[self.inputImage])
        #his = K

        #his = self.calcHistogram(K)


        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()" + ".png", options=options)
        cv2.imwrite(fileName, K)
        print(fileName)

        fig = plt.figure(figsize=(5,5))

        # lay = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(20, 20)
        # lay.addWidget(label)
        # lay.addStretch()

        # self.setGeometry(300, 300, 250, 150)
        # label.show()
        fig = plt.figure(figsize=(5, 5))
        self.box5.layout().addWidget(label)
        self.show()
        hist = self.calcHistogram(K, 2)
        hist1 = self.calcHistogram(K, 1)
        hist2 = self.calcHistogram(K, 0)
        index = np.arange(len(hist))
        a = fig.add_subplot(311)
        a.bar(index, hist)
        canvas = FigureCanvas(fig)
        # canvas.resize(50,25)
        self.box6.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist1))
        b = fig.add_subplot(312)
        b.bar(index, hist1)
        # canvas = FigureCanvas(fig)
        # canvas.resize(100,50)
        self.box6.layout().addWidget(canvas)
        canvas.show()
        index = np.arange(len(hist2))
        c = fig.add_subplot(313)
        c.bar(index, hist2)
        # canvas = FigureCanvas(fig)
        # canvas.resize(100,50)
        self.box6.layout().addWidget(canvas)
        # fig.tight_layout()
        canvas.show()
        # print(hist)
        # index = np.arange(len(hist))
        # plt.bar(index, hist)
        # plt.show()

        # plt.legend(loc='upper right')

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # for g in range(256):

        # return NotImplementedError
    def createLUT(self,inputCDF, targetCDF):
        LUT = np.zeros((256, 1))
        j = 0
        for i in range(len(inputCDF)):
            while(inputCDF[i]>targetCDF[j] and j<len(targetCDF)-1):
                j = j + 1
            LUT[i] = j
        return LUT

    def createCDF(self, image, color):
        hist = self.calcHistogram(image, color)
        imageCDF = self.getPdfFromHist(hist)
        sum = 0
        for i in range(len(hist)):
            sum = sum + imageCDF[i]
            imageCDF[i] = sum

        return imageCDF
        #index = np.arange(len(imagePdf))
        #plt.bar(index, imagePdf)
        # plt.legend(loc='upper right')
        #plt.show()
    def getPdfFromHist(self, hist):
        sum = hist.sum()
        for i in range(len(hist)):
            hist[i] = hist[i]/sum
        return hist
    def calcHistogram(self, I, color):
        # Calculate histogram
        R,C,B= I.shape
        # allocate the histogram
        hist = np.zeros([256])
        # range through the intensity values
        for row in range(R):
            for column in range(C):
                hist[I[row,column,color]] = hist[I[row,column,color]] + 1

        return hist


class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        #return NotImplementedError
        # Init Canvas
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        #fig = plt.hist(hist)
        #FigureCanvas.__init__(self)
        #FigureCanvas.__init__(self, self.figure)

        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        #return NotImplementedError
        # Plot histogram
        print(hist)
        ax = self.figure.add_subplot(111)

        index = np.arange(len(hist))
        ax.bar(index,hist)

        #self.figure=plt.bar(index, hist)
        # plt.legend(loc='upper right')
        #plt.show()
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setAccessibleName("main window")
    sys.exit(app.exec_())
