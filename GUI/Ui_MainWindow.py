# Form implementation generated from reading ui file 'GUI/designer/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 440)
        MainWindow.setMinimumSize(QtCore.QSize(720, 440))
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.CentralContentWidget = QtWidgets.QWidget(MainWindow)
        self.CentralContentWidget.setObjectName("CentralContentWidget")
        self.CentralContentWidgetLayout = QtWidgets.QHBoxLayout(self.CentralContentWidget)
        self.CentralContentWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.CentralContentWidgetLayout.setSpacing(0)
        self.CentralContentWidgetLayout.setObjectName("CentralContentWidgetLayout")
        self.SplitterBody = QtWidgets.QSplitter(self.CentralContentWidget)
        self.SplitterBody.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SplitterBody.setObjectName("SplitterBody")
        self.LeftColumnWidget = QtWidgets.QWidget(self.SplitterBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftColumnWidget.sizePolicy().hasHeightForWidth())
        self.LeftColumnWidget.setSizePolicy(sizePolicy)
        self.LeftColumnWidget.setMinimumSize(QtCore.QSize(280, 0))
        self.LeftColumnWidget.setObjectName("LeftColumnWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.LeftColumnWidget)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.ThumbnailArea = QtWidgets.QScrollArea(self.LeftColumnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThumbnailArea.sizePolicy().hasHeightForWidth())
        self.ThumbnailArea.setSizePolicy(sizePolicy)
        self.ThumbnailArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ThumbnailArea.setWidgetResizable(True)
        self.ThumbnailArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.ThumbnailArea.setObjectName("ThumbnailArea")
        self.ThumbnailAreaWidget = QtWidgets.QWidget()
        self.ThumbnailAreaWidget.setGeometry(QtCore.QRect(0, 0, 270, 374))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThumbnailAreaWidget.sizePolicy().hasHeightForWidth())
        self.ThumbnailAreaWidget.setSizePolicy(sizePolicy)
        self.ThumbnailAreaWidget.setObjectName("ThumbnailAreaWidget")
        self.ThumbnailAreaLayout = QtWidgets.QGridLayout(self.ThumbnailAreaWidget)
        self.ThumbnailAreaLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.ThumbnailAreaLayout.setObjectName("ThumbnailAreaLayout")
        self.ThumbnailArea.setWidget(self.ThumbnailAreaWidget)
        self.gridLayout.addWidget(self.ThumbnailArea, 1, 1, 1, 1)
        self.RightColumnWidget = QtWidgets.QWidget(self.SplitterBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightColumnWidget.sizePolicy().hasHeightForWidth())
        self.RightColumnWidget.setSizePolicy(sizePolicy)
        self.RightColumnWidget.setMinimumSize(QtCore.QSize(380, 0))
        self.RightColumnWidget.setObjectName("RightColumnWidget")
        self.RightColumnWidgetLayout = QtWidgets.QVBoxLayout(self.RightColumnWidget)
        self.RightColumnWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.RightColumnWidgetLayout.setObjectName("RightColumnWidgetLayout")
        self.PreviewLabel = QtWidgets.QLabel(self.RightColumnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PreviewLabel.sizePolicy().hasHeightForWidth())
        self.PreviewLabel.setSizePolicy(sizePolicy)
        self.PreviewLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PreviewLabel.setObjectName("PreviewLabel")
        self.RightColumnWidgetLayout.addWidget(self.PreviewLabel)
        self.FileInfoGroupBox = QtWidgets.QGroupBox(self.RightColumnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileInfoGroupBox.sizePolicy().hasHeightForWidth())
        self.FileInfoGroupBox.setSizePolicy(sizePolicy)
        self.FileInfoGroupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.FileInfoGroupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.FileInfoGroupBox.setObjectName("FileInfoGroupBox")
        self.FileInfoGroupBoxLayout = QtWidgets.QFormLayout(self.FileInfoGroupBox)
        self.FileInfoGroupBoxLayout.setObjectName("FileInfoGroupBoxLayout")
        self.TitleFileNameLabel = QtWidgets.QLabel(self.FileInfoGroupBox)
        self.TitleFileNameLabel.setObjectName("TitleFileNameLabel")
        self.FileInfoGroupBoxLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.TitleFileNameLabel)
        self.FileNameLabel = QtWidgets.QLabel(self.FileInfoGroupBox)
        self.FileNameLabel.setText("")
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.FileInfoGroupBoxLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.FileNameLabel)
        self.TitleResolutionLabel = QtWidgets.QLabel(self.FileInfoGroupBox)
        self.TitleResolutionLabel.setObjectName("TitleResolutionLabel")
        self.FileInfoGroupBoxLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.TitleResolutionLabel)
        self.ResolutionLabel = QtWidgets.QLabel(self.FileInfoGroupBox)
        self.ResolutionLabel.setText("")
        self.ResolutionLabel.setObjectName("ResolutionLabel")
        self.FileInfoGroupBoxLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ResolutionLabel)
        self.RightColumnWidgetLayout.addWidget(self.FileInfoGroupBox)
        self.CentralContentWidgetLayout.addWidget(self.SplitterBody)
        MainWindow.setCentralWidget(self.CentralContentWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.MenuBar.setObjectName("MenuBar")
        self.FileMenu = QtWidgets.QMenu(self.MenuBar)
        self.FileMenu.setObjectName("FileMenu")
        self.SortMenu = QtWidgets.QMenu(self.MenuBar)
        self.SortMenu.setObjectName("SortMenu")
        self.menuView = QtWidgets.QMenu(self.MenuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.OpenAction = QtGui.QAction(MainWindow)
        self.OpenAction.setObjectName("OpenAction")
        self.CloseAction = QtGui.QAction(MainWindow)
        self.CloseAction.setObjectName("CloseAction")
        self.RefreshAction = QtGui.QAction(MainWindow)
        self.RefreshAction.setObjectName("RefreshAction")
        self.ByColorAction = QtGui.QAction(MainWindow)
        self.ByColorAction.setObjectName("ByColorAction")
        self.UnsortedAction = QtGui.QAction(MainWindow)
        self.UnsortedAction.setObjectName("UnsortedAction")
        self.MoreColumnsAction = QtGui.QAction(MainWindow)
        self.MoreColumnsAction.setObjectName("MoreColumnsAction")
        self.LessColumnsAction = QtGui.QAction(MainWindow)
        self.LessColumnsAction.setObjectName("LessColumnsAction")
        self.SlideshowAction = QtGui.QAction(MainWindow)
        self.SlideshowAction.setObjectName("SlideshowAction")
        self.StopSlideshowAction = QtGui.QAction(MainWindow)
        self.StopSlideshowAction.setObjectName("StopSlideshowAction")
        self.ShuffleAction = QtGui.QAction(MainWindow)
        self.ShuffleAction.setObjectName("ShuffleAction")
        self.ToggleFileInfoAction = QtGui.QAction(MainWindow)
        self.ToggleFileInfoAction.setObjectName("ToggleFileInfoAction")
        self.FileMenu.addAction(self.OpenAction)
        self.FileMenu.addAction(self.RefreshAction)
        self.FileMenu.addAction(self.CloseAction)
        self.SortMenu.addAction(self.ByColorAction)
        self.SortMenu.addSeparator()
        self.SortMenu.addAction(self.ShuffleAction)
        self.SortMenu.addAction(self.UnsortedAction)
        self.menuView.addAction(self.MoreColumnsAction)
        self.menuView.addAction(self.LessColumnsAction)
        self.menuView.addSeparator()
        self.menuView.addAction(self.SlideshowAction)
        self.menuView.addAction(self.StopSlideshowAction)
        self.menuView.addSeparator()
        self.menuView.addAction(self.ToggleFileInfoAction)
        self.MenuBar.addAction(self.FileMenu.menuAction())
        self.MenuBar.addAction(self.SortMenu.menuAction())
        self.MenuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.FileInfoGroupBox.setTitle(_translate("MainWindow", "File info"))
        self.TitleFileNameLabel.setText(_translate("MainWindow", "File name:"))
        self.TitleResolutionLabel.setText(_translate("MainWindow", "Resolution"))
        self.FileMenu.setTitle(_translate("MainWindow", "File"))
        self.SortMenu.setTitle(_translate("MainWindow", "Sort"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.OpenAction.setText(_translate("MainWindow", "Open"))
        self.CloseAction.setText(_translate("MainWindow", "Close"))
        self.RefreshAction.setText(_translate("MainWindow", "Refresh"))
        self.ByColorAction.setText(_translate("MainWindow", "By Color"))
        self.UnsortedAction.setText(_translate("MainWindow", "Unsorted"))
        self.MoreColumnsAction.setText(_translate("MainWindow", "More columns"))
        self.LessColumnsAction.setText(_translate("MainWindow", "Less columns"))
        self.SlideshowAction.setText(_translate("MainWindow", "Slideshow"))
        self.StopSlideshowAction.setText(_translate("MainWindow", "Stop slideshow"))
        self.ShuffleAction.setText(_translate("MainWindow", "Shuffle"))
        self.ToggleFileInfoAction.setText(_translate("MainWindow", "Toggle FileInfo"))