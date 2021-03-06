# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_import_window(object):
    def setupUi(self, main_import_window):
        main_import_window.setObjectName("main_import_window")
        main_import_window.setWindowModality(QtCore.Qt.NonModal)
        main_import_window.resize(361, 293)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_import_window.sizePolicy().hasHeightForWidth())
        main_import_window.setSizePolicy(sizePolicy)
        main_import_window.setMinimumSize(QtCore.QSize(0, 0))
        main_import_window.setSizeIncrement(QtCore.QSize(0, 0))
        main_import_window.setBaseSize(QtCore.QSize(200, 200))
        main_import_window.setAnimated(True)
        self.centralWidget = QtWidgets.QWidget(main_import_window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_label_image = QtWidgets.QLabel(self.centralWidget)
        self.main_label_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_label_image.setLineWidth(0)
        self.main_label_image.setText("")
        self.main_label_image.setObjectName("main_label_image")
        self.horizontalLayout.addWidget(self.main_label_image)
        main_import_window.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(main_import_window)
        self.mainToolBar.setObjectName("mainToolBar")
        main_import_window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(main_import_window)
        self.statusBar.setObjectName("statusBar")
        main_import_window.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(main_import_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuConvert_dataset = QtWidgets.QMenu(self.menuBar)
        self.menuConvert_dataset.setObjectName("menuConvert_dataset")
        self.menuAnalysis = QtWidgets.QMenu(self.menuBar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuData = QtWidgets.QMenu(self.menuBar)
        self.menuData.setObjectName("menuData")
        main_import_window.setMenuBar(self.menuBar)
        self.actionConvert_dataset = QtWidgets.QAction(main_import_window)
        self.actionConvert_dataset.setText("Convert dataset")
        self.actionConvert_dataset.setPriority(QtWidgets.QAction.HighPriority)
        self.actionConvert_dataset.setObjectName("actionConvert_dataset")
        self.actionLoad_dataset = QtWidgets.QAction(main_import_window)
        self.actionLoad_dataset.setObjectName("actionLoad_dataset")
        self.actionOpen_browser = QtWidgets.QAction(main_import_window)
        self.actionOpen_browser.setObjectName("actionOpen_browser")
        self.actionSettings = QtWidgets.QAction(main_import_window)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(main_import_window)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPCA_NMF = QtWidgets.QAction(main_import_window)
        self.actionPCA_NMF.setObjectName("actionPCA_NMF")
        self.actionFitting = QtWidgets.QAction(main_import_window)
        self.actionFitting.setObjectName("actionFitting")
        self.actionEnvironments = QtWidgets.QAction(main_import_window)
        self.actionEnvironments.setObjectName("actionEnvironments")
        self.actionNew_environment = QtWidgets.QAction(main_import_window)
        self.actionNew_environment.setObjectName("actionNew_environment")
        self.actionSave_environment = QtWidgets.QAction(main_import_window)
        self.actionSave_environment.setObjectName("actionSave_environment")
        self.actionremove = QtWidgets.QAction(main_import_window)
        self.actionremove.setObjectName("actionremove")
        self.menuConvert_dataset.addAction(self.actionNew_environment)
        self.menuConvert_dataset.addSeparator()
        self.menuConvert_dataset.addAction(self.actionConvert_dataset)
        self.menuConvert_dataset.addAction(self.actionLoad_dataset)
        self.menuConvert_dataset.addAction(self.actionOpen_browser)
        self.menuConvert_dataset.addSeparator()
        self.menuConvert_dataset.addAction(self.actionSave_environment)
        self.menuConvert_dataset.addSeparator()
        self.menuConvert_dataset.addAction(self.actionSettings)
        self.menuConvert_dataset.addSeparator()
        self.menuConvert_dataset.addAction(self.actionQuit)
        self.menuAnalysis.addAction(self.actionPCA_NMF)
        self.menuAnalysis.addAction(self.actionFitting)
        self.menuData.addAction(self.actionEnvironments)
        self.menuData.addAction(self.actionremove)
        self.menuBar.addAction(self.menuConvert_dataset.menuAction())
        self.menuBar.addAction(self.menuData.menuAction())
        self.menuBar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(main_import_window)
        QtCore.QMetaObject.connectSlotsByName(main_import_window)

    def retranslateUi(self, main_import_window):
        _translate = QtCore.QCoreApplication.translate
        main_import_window.setWindowTitle(_translate("main_import_window", "R-Data"))
        self.menuConvert_dataset.setTitle(_translate("main_import_window", "File"))
        self.menuAnalysis.setTitle(_translate("main_import_window", "Analysis"))
        self.menuData.setTitle(_translate("main_import_window", "Environments"))
        self.actionLoad_dataset.setText(_translate("main_import_window", "Open datatset"))
        self.actionOpen_browser.setText(_translate("main_import_window", "Open browser"))
        self.actionSettings.setText(_translate("main_import_window", "Settings"))
        self.actionQuit.setText(_translate("main_import_window", "Quit"))
        self.actionPCA_NMF.setText(_translate("main_import_window", "PCA / NMF"))
        self.actionFitting.setText(_translate("main_import_window", "Fitting"))
        self.actionEnvironments.setText(_translate("main_import_window", "Select"))
        self.actionNew_environment.setText(_translate("main_import_window", "New environment"))
        self.actionSave_environment.setText(_translate("main_import_window", "Save environment"))
        self.actionremove.setText(_translate("main_import_window", "Remove"))

