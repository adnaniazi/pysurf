__authors__ = 'Irfan Shah, Muhammad Waleed, and Adnan Niazi'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from my_gui import Ui_MainWindow
import math

class MyMainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)
        app.setStyle(QStyleFactory.create('Plastique'))
        # define signals and slots
        self.toolButton_go.clicked.connect(self.load_web_page)
        self.toolButton_next.clicked.connect(self.go_next_page)
        self.toolButton_previous.clicked.connect(self.go_previous_page)
        self.lineEdit_url.returnPressed.connect(self.load_web_page)
        self.toolButton_home.clicked.connect(self.go_to_home_page)
        self.webView.urlChanged.connect(self.update_url_in_lineEDit_url)
        self.toolButton_stop.clicked.connect(self.stop_loading)
        self.toolButton_refresh.clicked.connect(self.refresh_current_page)
        self.toolButton_zoom_in.clicked.connect(self.zoom_in)
        self.toolButton_zoom_out.clicked.connect(self.zoom_out)
        self.webView.loadProgress.connect(self.update_progress)
        self.webView.titleChanged.connect(self.update_webpage_title)

        # initialize display elements
        self.toolButton_stop.setDisabled(True)
        self.progressBar.setMaximumHeight(3)

    def update_webpage_title(self, title):
        """Get title of webpage and sets it as the title of browser window.
        Also enable and disable forward and back buttons"""

        self.setWindowTitle(title)

        h = self.webView.history()
        if h.currentItemIndex() == 0 and len(h.items()) == 1:
            # if only one webpage has been loaded then disable
            # both forward and back buttons
            self.toolButton_next.setEnabled(False)
            self.toolButton_previous.setEnabled(False)
        elif h.currentItemIndex() == 0 and len(h.items()) > 1:
            # if more than one webpage has been loaded and the user
            # is currently viewing the very first page, then:
            self.toolButton_next.setEnabled(True)
            self.toolButton_previous.setEnabled(False)
        elif h.currentItemIndex() == len(h.items())-1 and len(h.items()) > 1:
            # if more than one webpage has been loaded and the user
            # is currently viewing the very last page, then:
            self.toolButton_next.setEnabled(False)
            self.toolButton_previous.setEnabled(True)
        else:
            # if more than one webpage has been loaded and the user
            # is somewhere in the middle of the history stack, then:
            self.toolButton_next.setEnabled(True)
            self.toolButton_previous.setEnabled(True)

    def update_progress(self, current_progress):
        """Updates progress on the progress bar"""

        self.progressBar.setValue(current_progress)
        if current_progress == 100:
            self.toolButton_stop.setDisabled(True)
            for i in range(0,1000000):
                # wait a bit after the progress bar reaches 100 %
                # and then reset the progress bar just like in YouTube
                pass
            self.progressBar.setValue(0)
        else:
            self.toolButton_stop.setEnabled(True)

    def zoom_in(self):
        """Increases page zoom by 10% """

        self.current_zoom = self.webView.zoomFactor()
        self.current_zoom = self.current_zoom + 0.1
        self.webView.setZoomFactor(self.current_zoom)
        self.label_current_zoom.setText(str(math.floor(self.current_zoom * 100))+'%')

    def zoom_out(self):
        """Decreases page zoom by 10% """

        self.current_zoom = self.webView.zoomFactor()
        self.current_zoom = self.current_zoom - 0.1
        self.webView.setZoomFactor(self.current_zoom)
        self.label_current_zoom.setText(str(math.floor(self.current_zoom * 100))+'%')

    def stop_loading(self):
        """Stops loading a webpage"""

        self.webView.stop()

    def go_next_page(self):
        """Goes to the next page in current browser history"""

        self.webView.forward()

    def go_previous_page(self):
        """Goes to the previous page in current browser history"""

        self.webView.back()

    def load_web_page(self):
        """Constructs a proper url and then loads it into QWebView widget"""

        self.url = self.lineEdit_url.text()
        if 'http://www.' not in self.url and '.com' not in self.url:
            self.url = "http://www.google.com/search?q=" + self.url
        if '.com' not in self.url:
            self.url = self.url + '.com'
        if ('http://' or 'https://') not in self.url:
            self.url = 'http://' + self.url

        self.webView.setUrl(QUrl(self.url))
        self.lineEdit_url.setText(self.url)
        self.lineEdit_url.setCursorPosition(0) # brings cursor to the start of the URL

    def update_url_in_lineEDit_url(self):
        """Display the URL of page being currently viewed in the address bar"""

        current_url = self.webView.url()
        self.lineEdit_url.setText(QUrl.toString(current_url))
        self.lineEdit_url.setCursorPosition(0) # brings cursor to the start of the URL

    def go_to_home_page(self):
        """Display the homepage: google.com"""

        self.webView.setUrl(QUrl("http://www.google.com"))

    def refresh_current_page(self):
        """Reloads current page"""

        current_url = self.webView.url()
        self.webView.setUrl(current_url)
        self.lineEdit_url.setCursorPosition(0) # brings cursor to the start of the URL


if __name__ == "__main__":
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())