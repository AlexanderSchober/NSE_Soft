# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_import.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_import_window(object):
    def setupUi(self, import_window):
        import_window.setObjectName("import_window")
        import_window.resize(1088, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(import_window.sizePolicy().hasHeightForWidth())
        import_window.setSizePolicy(sizePolicy)
        import_window.setMinimumSize(QtCore.QSize(0, 750))
        import_window.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralWidget = QtWidgets.QWidget(import_window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_group_dialog = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_group_dialog.sizePolicy().hasHeightForWidth())
        self.data_group_dialog.setSizePolicy(sizePolicy)
        self.data_group_dialog.setMinimumSize(QtCore.QSize(0, 0))
        self.data_group_dialog.setMaximumSize(QtCore.QSize(300, 16777215))
        self.data_group_dialog.setObjectName("data_group_dialog")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.data_group_dialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.data_label_meta = QtWidgets.QLabel(self.data_group_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_label_meta.sizePolicy().hasHeightForWidth())
        self.data_label_meta.setSizePolicy(sizePolicy)
        self.data_label_meta.setObjectName("data_label_meta")
        self.verticalLayout_12.addWidget(self.data_label_meta)
        self.data_list_meta = QtWidgets.QListWidget(self.data_group_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_list_meta.sizePolicy().hasHeightForWidth())
        self.data_list_meta.setSizePolicy(sizePolicy)
        self.data_list_meta.setMinimumSize(QtCore.QSize(0, 30))
        self.data_list_meta.setSizeIncrement(QtCore.QSize(0, 0))
        self.data_list_meta.setAcceptDrops(True)
        self.data_list_meta.setLineWidth(0)
        self.data_list_meta.setAutoScrollMargin(10)
        self.data_list_meta.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.data_list_meta.setObjectName("data_list_meta")
        self.verticalLayout_12.addWidget(self.data_list_meta)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.data_button_meta_all = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_meta_all.setObjectName("data_button_meta_all")
        self.horizontalLayout_7.addWidget(self.data_button_meta_all)
        self.data_button_meta_remove = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_meta_remove.setObjectName("data_button_meta_remove")
        self.horizontalLayout_7.addWidget(self.data_button_meta_remove)
        self.data_button_meta_add = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_meta_add.setObjectName("data_button_meta_add")
        self.horizontalLayout_7.addWidget(self.data_button_meta_add)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.data_label_files = QtWidgets.QLabel(self.data_group_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_label_files.sizePolicy().hasHeightForWidth())
        self.data_label_files.setSizePolicy(sizePolicy)
        self.data_label_files.setObjectName("data_label_files")
        self.verticalLayout_10.addWidget(self.data_label_files)
        self.data_list_files = QtWidgets.QListView(self.data_group_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_list_files.sizePolicy().hasHeightForWidth())
        self.data_list_files.setSizePolicy(sizePolicy)
        self.data_list_files.setMinimumSize(QtCore.QSize(0, 30))
        self.data_list_files.setAcceptDrops(True)
        self.data_list_files.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.data_list_files.setObjectName("data_list_files")
        self.verticalLayout_10.addWidget(self.data_list_files)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.data_button_files_reset = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_files_reset.setObjectName("data_button_files_reset")
        self.horizontalLayout_8.addWidget(self.data_button_files_reset)
        self.data_button_files_remove = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_files_remove.setObjectName("data_button_files_remove")
        self.horizontalLayout_8.addWidget(self.data_button_files_remove)
        self.data_button_files_add = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_files_add.setObjectName("data_button_files_add")
        self.horizontalLayout_8.addWidget(self.data_button_files_add)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.data_label_prev = QtWidgets.QLabel(self.data_group_dialog)
        self.data_label_prev.setObjectName("data_label_prev")
        self.verticalLayout_13.addWidget(self.data_label_prev)
        self.data_widget_graph = QtWidgets.QWidget(self.data_group_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_widget_graph.sizePolicy().hasHeightForWidth())
        self.data_widget_graph.setSizePolicy(sizePolicy)
        self.data_widget_graph.setMinimumSize(QtCore.QSize(268, 250))
        self.data_widget_graph.setMaximumSize(QtCore.QSize(250, 250))
        self.data_widget_graph.setSizeIncrement(QtCore.QSize(0, 1))
        self.data_widget_graph.setBaseSize(QtCore.QSize(268, 250))
        self.data_widget_graph.setObjectName("data_widget_graph")
        self.verticalLayout_13.addWidget(self.data_widget_graph)
        self.verticalLayout.addLayout(self.verticalLayout_13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.data_button_populate = QtWidgets.QPushButton(self.data_group_dialog)
        self.data_button_populate.setDefault(True)
        self.data_button_populate.setObjectName("data_button_populate")
        self.horizontalLayout_2.addWidget(self.data_button_populate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.data_group_dialog)
        self.data_group_loaded = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_group_loaded.sizePolicy().hasHeightForWidth())
        self.data_group_loaded.setSizePolicy(sizePolicy)
        self.data_group_loaded.setObjectName("data_group_loaded")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.data_group_loaded)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.data_group_loaded)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.data_input_foils = QtWidgets.QLineEdit(self.data_group_loaded)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_input_foils.sizePolicy().hasHeightForWidth())
        self.data_input_foils.setSizePolicy(sizePolicy)
        self.data_input_foils.setMinimumSize(QtCore.QSize(50, 0))
        self.data_input_foils.setMaximumSize(QtCore.QSize(50, 16777215))
        self.data_input_foils.setBaseSize(QtCore.QSize(50, 0))
        self.data_input_foils.setMaxLength(32763)
        self.data_input_foils.setAlignment(QtCore.Qt.AlignCenter)
        self.data_input_foils.setObjectName("data_input_foils")
        self.horizontalLayout_3.addWidget(self.data_input_foils)
        self.data_input_time_channel = QtWidgets.QLineEdit(self.data_group_loaded)
        self.data_input_time_channel.setMinimumSize(QtCore.QSize(50, 0))
        self.data_input_time_channel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.data_input_time_channel.setSizeIncrement(QtCore.QSize(50, 0))
        self.data_input_time_channel.setBaseSize(QtCore.QSize(50, 0))
        self.data_input_time_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.data_input_time_channel.setObjectName("data_input_time_channel")
        self.horizontalLayout_3.addWidget(self.data_input_time_channel)
        self.data_input_pix_x = QtWidgets.QLineEdit(self.data_group_loaded)
        self.data_input_pix_x.setMinimumSize(QtCore.QSize(50, 0))
        self.data_input_pix_x.setMaximumSize(QtCore.QSize(50, 16777215))
        self.data_input_pix_x.setBaseSize(QtCore.QSize(50, 0))
        self.data_input_pix_x.setAlignment(QtCore.Qt.AlignCenter)
        self.data_input_pix_x.setObjectName("data_input_pix_x")
        self.horizontalLayout_3.addWidget(self.data_input_pix_x)
        self.data_input_pix_y = QtWidgets.QLineEdit(self.data_group_loaded)
        self.data_input_pix_y.setMinimumSize(QtCore.QSize(50, 0))
        self.data_input_pix_y.setMaximumSize(QtCore.QSize(50, 16777215))
        self.data_input_pix_y.setBaseSize(QtCore.QSize(50, 0))
        self.data_input_pix_y.setAlignment(QtCore.Qt.AlignCenter)
        self.data_input_pix_y.setObjectName("data_input_pix_y")
        self.horizontalLayout_3.addWidget(self.data_input_pix_y)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.data_list_loaded = QtWidgets.QListWidget(self.data_group_loaded)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_list_loaded.sizePolicy().hasHeightForWidth())
        self.data_list_loaded.setSizePolicy(sizePolicy)
        self.data_list_loaded.setSizeIncrement(QtCore.QSize(2, 0))
        self.data_list_loaded.setAcceptDrops(True)
        self.data_list_loaded.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_list_loaded.setLineWidth(0)
        self.data_list_loaded.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.data_list_loaded.setViewMode(QtWidgets.QListView.ListMode)
        self.data_list_loaded.setSelectionRectVisible(True)
        self.data_list_loaded.setObjectName("data_list_loaded")
        self.verticalLayout_2.addWidget(self.data_list_loaded)
        self.horizontalLayout.addWidget(self.data_group_loaded)
        import_window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(import_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1088, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        import_window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(import_window)
        self.mainToolBar.setObjectName("mainToolBar")
        import_window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(import_window)
        self.statusBar.setObjectName("statusBar")
        import_window.setStatusBar(self.statusBar)
        self.actionLoad = QtWidgets.QAction(import_window)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(import_window)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd_Element = QtWidgets.QAction(import_window)
        self.actionAdd_Element.setObjectName("actionAdd_Element")
        self.actionRemove_Element = QtWidgets.QAction(import_window)
        self.actionRemove_Element.setObjectName("actionRemove_Element")
        self.actionGenerate_Dataset = QtWidgets.QAction(import_window)
        self.actionGenerate_Dataset.setObjectName("actionGenerate_Dataset")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_Element)
        self.menuFile.addAction(self.actionRemove_Element)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGenerate_Dataset)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(import_window)
        QtCore.QMetaObject.connectSlotsByName(import_window)

    def retranslateUi(self, import_window):
        _translate = QtCore.QCoreApplication.translate
        import_window.setWindowTitle(_translate("import_window", "Import"))
        self.data_group_dialog.setTitle(_translate("import_window", "Loading dialog"))
        self.data_label_meta.setText(_translate("import_window", "Metadata keywords:"))
        self.data_button_meta_all.setText(_translate("import_window", "All"))
        self.data_button_meta_remove.setText(_translate("import_window", "Remove"))
        self.data_button_meta_add.setText(_translate("import_window", "Add"))
        self.data_label_files.setText(_translate("import_window", "Files:"))
        self.data_button_files_reset.setText(_translate("import_window", "Reset"))
        self.data_button_files_remove.setText(_translate("import_window", "Remove"))
        self.data_button_files_add.setText(_translate("import_window", "Add"))
        self.data_label_prev.setText(_translate("import_window", "Preview:"))
        self.data_button_populate.setText(_translate("import_window", "Populate"))
        self.data_group_loaded.setTitle(_translate("import_window", "Loaded data"))
        self.label.setText(_translate("import_window", "Dimension (foils x time channels x pixels x pixels)"))
        self.data_input_foils.setText(_translate("import_window", "8"))
        self.data_input_time_channel.setText(_translate("import_window", "16"))
        self.data_input_pix_x.setText(_translate("import_window", "128"))
        self.data_input_pix_y.setText(_translate("import_window", "128"))
        self.menuFile.setTitle(_translate("import_window", "File"))
        self.actionLoad.setText(_translate("import_window", "Load"))
        self.actionLoad.setShortcut(_translate("import_window", "Ctrl+L"))
        self.actionSave.setText(_translate("import_window", "Save"))
        self.actionSave.setShortcut(_translate("import_window", "Ctrl+S"))
        self.actionAdd_Element.setText(_translate("import_window", "Add Element"))
        self.actionAdd_Element.setShortcut(_translate("import_window", "Ctrl++"))
        self.actionRemove_Element.setText(_translate("import_window", "Remove Element"))
        self.actionRemove_Element.setShortcut(_translate("import_window", "Ctrl+-"))
        self.actionGenerate_Dataset.setText(_translate("import_window", "Generate Dataset"))
        self.actionGenerate_Dataset.setShortcut(_translate("import_window", "Ctrl+G"))

