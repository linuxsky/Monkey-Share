# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadWindow.ui'
#
# Created: Sun Dec  9 20:18:43 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DownloadWindow(object):
    def setupUi(self, DownloadWindow):
        DownloadWindow.setObjectName(_fromUtf8("DownloadWindow"))
        DownloadWindow.resize(620, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Downloads/1355009308_Gnome-Face-Monkey-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadWindow.setWindowIcon(icon)
        DownloadWindow.setWindowOpacity(1.0)
        self.verticalLayout = QtGui.QVBoxLayout(DownloadWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(DownloadWindow)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.frame_2 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setContentsMargins(15, 0, 0, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.requestedFileLabel = QtGui.QLabel(self.frame_2)
        self.requestedFileLabel.setObjectName(_fromUtf8("requestedFileLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.requestedFileLabel)
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.frame_6 = QtGui.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fileDestinationInput = QtGui.QLineEdit(self.frame_6)
        self.fileDestinationInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fileDestinationInput.setObjectName(_fromUtf8("fileDestinationInput"))
        self.horizontalLayout_2.addWidget(self.fileDestinationInput)
        self.browseButton = QtGui.QPushButton(self.frame_6)
        self.browseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.frame_6)
        self.label_5 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.sizeLabel = QtGui.QLabel(self.frame_2)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sizeLabel)
        self.label_6 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.sumLabel = QtGui.QLabel(self.frame_2)
        self.sumLabel.setObjectName(_fromUtf8("sumLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.sumLabel)
        self.label_7 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.userLabel = QtGui.QLabel(self.frame_2)
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.userLabel)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(15, -1, 9, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.progressBar = QtGui.QProgressBar(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.progressBar)
        self.speedLabel = QtGui.QLabel(self.frame_4)
        self.speedLabel.setText(_fromUtf8(""))
        self.speedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.speedLabel.setObjectName(_fromUtf8("speedLabel"))
        self.verticalLayout_3.addWidget(self.speedLabel)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout.addWidget(self.frame_5)
        self.cancelButton = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.downloadButton = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout.addWidget(self.downloadButton)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(DownloadWindow)
        QtCore.QMetaObject.connectSlotsByName(DownloadWindow)

    def retranslateUi(self, DownloadWindow):
        DownloadWindow.setWindowTitle(QtGui.QApplication.translate("DownloadWindow", "Download File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DownloadWindow", "Download File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DownloadWindow", "Requested File:", None, QtGui.QApplication.UnicodeUTF8))
        self.requestedFileLabel.setText(QtGui.QApplication.translate("DownloadWindow", "requestedfilename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DownloadWindow", "File Destination:", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("DownloadWindow", "Change Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DownloadWindow", "File Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLabel.setText(QtGui.QApplication.translate("DownloadWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DownloadWindow", "MD5 Checksum:", None, QtGui.QApplication.UnicodeUTF8))
        self.sumLabel.setText(QtGui.QApplication.translate("DownloadWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DownloadWindow", "File Owner:", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("DownloadWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DownloadWindow", "Download Progress:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DownloadWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("DownloadWindow", "Download File", None, QtGui.QApplication.UnicodeUTF8))

