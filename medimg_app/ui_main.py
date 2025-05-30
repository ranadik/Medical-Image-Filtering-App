# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(916, 880)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setAutoFillBackground(False)
        self.load_button = QPushButton(Form)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(780, 480, 111, 39))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(18, 238, 183, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(121, 255, 222, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(69, 246, 202, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(9, 119, 91, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(12, 159, 122, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        brush7 = QBrush(QColor(136, 246, 219, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
        brush10 = QBrush(QColor(9, 119, 91, 127))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(74, 255, 210, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.load_button.setPalette(palette)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 861, 451))
        self.vboxLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.verticalLayoutWidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(400, 300))
        self.image_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.image_label.setLineWidth(1)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.image_label)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(150, 490, 201, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.horizontalSlider.setPalette(palette1)
        self.horizontalSlider.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background: #dddddd;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #12eeb7;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #cccccc;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #12eeb7;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -5px 0;  /* Center the handle vertically */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #0abf96;\n"
"}\n"
"")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(31)
        self.horizontalSlider.setSliderPosition(16)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_2 = QSlider(Form)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(150, 540, 201, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.horizontalSlider_2.setPalette(palette2)
        self.horizontalSlider_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background: #dddddd;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #12eeb7;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #cccccc;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #12eeb7;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -5px 0;  /* Center the handle vertically */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #0abf96;\n"
"}\n"
"\n"
"")
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setSliderPosition(125)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 490, 101, 20))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 540, 81, 20))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 590, 121, 31))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalSlider_3 = QSlider(Form)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(150, 590, 201, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.horizontalSlider_3.setPalette(palette3)
        self.horizontalSlider_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider_3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background: #dddddd;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #12eeb7;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #cccccc;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #12eeb7;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -5px 0;  /* Center the handle vertically */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #0abf96;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalSlider_3.setMinimum(50)
        self.horizontalSlider_3.setMaximum(200)
        self.horizontalSlider_3.setSliderPosition(125)
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)
        self.zoom_in_button = QPushButton(Form)
        self.zoom_in_button.setObjectName(u"zoom_in_button")
        self.zoom_in_button.setGeometry(QRect(700, 710, 83, 29))
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.zoom_in_button.setPalette(palette4)
        self.zoom_out_button = QPushButton(Form)
        self.zoom_out_button.setObjectName(u"zoom_out_button")
        self.zoom_out_button.setGeometry(QRect(800, 710, 83, 29))
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.zoom_out_button.setPalette(palette5)
        self.horizontalSlider_4 = QSlider(Form)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setGeometry(QRect(150, 630, 201, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.horizontalSlider_4.setPalette(palette6)
        self.horizontalSlider_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider_4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background: #dddddd;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #12eeb7;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #cccccc;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #12eeb7;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -5px 0;  /* Center the handle vertically */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #0abf96;\n"
"}\n"
"\n"
"")
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(31)
        self.horizontalSlider_4.setSliderPosition(16)
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 640, 121, 20))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.circle_button = QPushButton(Form)
        self.circle_button.setObjectName(u"circle_button")
        self.circle_button.setGeometry(QRect(260, 700, 91, 29))
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.circle_button.setPalette(palette7)
        self.circle_button.setStyleSheet(u"selection-color: rgb(18, 238, 183);")
        self.circle_button.setCheckable(False)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 700, 111, 20))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.reset_button = QPushButton(Form)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(780, 530, 111, 41))
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.reset_button.setPalette(palette8)
        self.precise_button = QPushButton(Form)
        self.precise_button.setObjectName(u"precise_button")
        self.precise_button.setGeometry(QRect(260, 740, 91, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush6)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush6)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush11)
#endif
        self.precise_button.setPalette(palette9)
        self.precise_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.precise_button.setCheckable(False)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 740, 191, 31))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Test", None))
        self.load_button.setText(QCoreApplication.translate("Form", u"Load Image", None))
        self.image_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#12eeb7;\">Image will appear here</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Blur</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Threshold</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Edge Detection</span></p></body></html>", None))
        self.zoom_in_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.zoom_out_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Otsu Filter</span></p></body></html>", None))
        self.circle_button.setText(QCoreApplication.translate("Form", u"Circle", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Circle the Tumor</span></p></body></html>", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"Reset Filters", None))
        self.precise_button.setText(QCoreApplication.translate("Form", u"Precise Edges", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">Precise Edge Detection</span></p></body></html>", None))
    # retranslateUi

