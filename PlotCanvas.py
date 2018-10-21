class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        #return NotImplementedError
        # Init Canvas
        #super(PlotCanvas,self).__init__(hist)
        #fig = plt.hist(hist)
        #FigureCanvas.__init__(self)
        #FigureCanvas.__init__(self, self.figure)
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        #return NotImplementedError
        # Plot histogram
        fig = plt.figure()
        hist_fig = fig.add_subplot(1, 1, 1)
        bins = np.linspace(0, 255, 100)
        red_hist = hist[:,:,0]
        plt.hist(red_hist, bins, alpha=0.5, label='x')
        plt.legend(loc='upper right')
        plt.show()

        self.draw()
