# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_io_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_io_widget(object):
    def setupUi(self, io_widget):
        io_widget.setObjectName("io_widget")
        io_widget.resize(936, 697)
        io_widget.setStyleSheet("#io_widget{background-color: rgb(179, 179, 179);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(io_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(io_widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.io_label_load_path = QtWidgets.QLabel(self.groupBox)
        self.io_label_load_path.setObjectName("io_label_load_path")
        self.horizontalLayout.addWidget(self.io_label_load_path)
        self.io_input_load_path = QtWidgets.QLineEdit(self.groupBox)
        self.io_input_load_path.setObjectName("io_input_load_path")
        self.horizontalLayout.addWidget(self.io_input_load_path)
        self.io_button_load_path = QtWidgets.QToolButton(self.groupBox)
        self.io_button_load_path.setObjectName("io_button_load_path")
        self.horizontalLayout.addWidget(self.io_button_load_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.io_check_load_data = QtWidgets.QCheckBox(self.groupBox)
        self.io_check_load_data.setChecked(True)
        self.io_check_load_data.setObjectName("io_check_load_data")
        self.horizontalLayout_2.addWidget(self.io_check_load_data)
        self.io_check_load_mask = QtWidgets.QCheckBox(self.groupBox)
        self.io_check_load_mask.setChecked(False)
        self.io_check_load_mask.setObjectName("io_check_load_mask")
        self.horizontalLayout_2.addWidget(self.io_check_load_mask)
        self.io_check_load_scripts = QtWidgets.QCheckBox(self.groupBox)
        self.io_check_load_scripts.setChecked(True)
        self.io_check_load_scripts.setObjectName("io_check_load_scripts")
        self.horizontalLayout_2.addWidget(self.io_check_load_scripts)
        self.io_check_load_add = QtWidgets.QCheckBox(self.groupBox)
        self.io_check_load_add.setChecked(True)
        self.io_check_load_add.setObjectName("io_check_load_add")
        self.horizontalLayout_2.addWidget(self.io_check_load_add)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.io_button_load = QtWidgets.QPushButton(self.groupBox)
        self.io_button_load.setDefault(True)
        self.io_button_load.setObjectName("io_button_load")
        self.horizontalLayout_2.addWidget(self.io_button_load)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.io_tree_load = QtWidgets.QTreeView(self.groupBox)
        self.io_tree_load.setObjectName("io_tree_load")
        self.verticalLayout_2.addWidget(self.io_tree_load)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(io_widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.io_label_save_path = QtWidgets.QLabel(self.groupBox_2)
        self.io_label_save_path.setObjectName("io_label_save_path")
        self.horizontalLayout_3.addWidget(self.io_label_save_path)
        self.io_input_save_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.io_input_save_path.setObjectName("io_input_save_path")
        self.horizontalLayout_3.addWidget(self.io_input_save_path)
        self.io_button_save_path = QtWidgets.QToolButton(self.groupBox_2)
        self.io_button_save_path.setObjectName("io_button_save_path")
        self.horizontalLayout_3.addWidget(self.io_button_save_path)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.io_check_save_data = QtWidgets.QCheckBox(self.groupBox_2)
        self.io_check_save_data.setObjectName("io_check_save_data")
        self.horizontalLayout_4.addWidget(self.io_check_save_data)
        self.io_check_save_mask = QtWidgets.QCheckBox(self.groupBox_2)
        self.io_check_save_mask.setObjectName("io_check_save_mask")
        self.horizontalLayout_4.addWidget(self.io_check_save_mask)
        self.io_check_save_scripts = QtWidgets.QCheckBox(self.groupBox_2)
        self.io_check_save_scripts.setObjectName("io_check_save_scripts")
        self.horizontalLayout_4.addWidget(self.io_check_save_scripts)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.io_button_save = QtWidgets.QPushButton(self.groupBox_2)
        self.io_button_save.setDefault(True)
        self.io_button_save.setObjectName("io_button_save")
        self.horizontalLayout_4.addWidget(self.io_button_save)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.io_tree_save = QtWidgets.QTreeView(self.groupBox_2)
        self.io_tree_save.setObjectName("io_tree_save")
        self.verticalLayout_3.addWidget(self.io_tree_save)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(io_widget)
        QtCore.QMetaObject.connectSlotsByName(io_widget)

    def retranslateUi(self, io_widget):
        _translate = QtCore.QCoreApplication.translate
        io_widget.setWindowTitle(_translate("io_widget", "Form"))
        self.groupBox.setTitle(_translate("io_widget", "Load Session"))
        self.io_label_load_path.setText(_translate("io_widget", "Path:"))
        self.io_button_load_path.setText(_translate("io_widget", "..."))
        self.io_check_load_data.setText(_translate("io_widget", "Load Data"))
        self.io_check_load_mask.setText(_translate("io_widget", "Load Masks"))
        self.io_check_load_scripts.setText(_translate("io_widget", "Load scripts"))
        self.io_check_load_add.setText(_translate("io_widget", "append"))
        self.io_button_load.setText(_translate("io_widget", "Load"))
        self.groupBox_2.setTitle(_translate("io_widget", "Save Session"))
        self.io_label_save_path.setText(_translate("io_widget", "Path:"))
        self.io_button_save_path.setText(_translate("io_widget", "..."))
        self.io_check_save_data.setText(_translate("io_widget", "Load Data"))
        self.io_check_save_mask.setText(_translate("io_widget", "Load Masks"))
        self.io_check_save_scripts.setText(_translate("io_widget", "Load scripts"))
        self.io_button_save.setText(_translate("io_widget", "Save"))

