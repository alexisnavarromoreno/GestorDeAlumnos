# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 681)
        icon = QIcon()
        icon.addFile(u":/rsc/Iconos/alumno.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 75 12pt \"Calibri\";")
        self.actionAniadir = QAction(MainWindow)
        self.actionAniadir.setObjectName(u"actionAniadir")
        icon1 = QIcon()
        icon1.addFile(u":/rsc/Iconos/a\u00f1adir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAniadir.setIcon(icon1)
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon2 = QIcon()
        icon2.addFile(u":/rsc/Iconos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar.setIcon(icon2)
        self.actionModificarAlumno = QAction(MainWindow)
        self.actionModificarAlumno.setObjectName(u"actionModificarAlumno")
        icon3 = QIcon()
        icon3.addFile(u":/rsc/Iconos/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModificarAlumno.setIcon(icon3)
        self.actionGenerar_Informe = QAction(MainWindow)
        self.actionGenerar_Informe.setObjectName(u"actionGenerar_Informe")
        icon4 = QIcon()
        icon4.addFile(u":/rsc/Iconos/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerar_Informe.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pestanias = QTabWidget(self.centralwidget)
        self.pestanias.setObjectName(u"pestanias")
        self.pestanias.setEnabled(True)
        self.pestanias.setGeometry(QRect(0, 0, 851, 591))
        self.pestanias.setStyleSheet(u"background-color:#CACFD2")
        self.pestanias.setTabPosition(QTabWidget.North)
        self.pestanias.setTabShape(QTabWidget.Rounded)
        self.AniadirModificarEliminar = QWidget()
        self.AniadirModificarEliminar.setObjectName(u"AniadirModificarEliminar")
        self.formLayoutWidget = QWidget(self.AniadirModificarEliminar)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 20, 491, 281))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelDNI = QLabel(self.formLayoutWidget)
        self.labelDNI.setObjectName(u"labelDNI")
        self.labelDNI.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDNI)

        self.lineEdit_DNI = QLineEdit(self.formLayoutWidget)
        self.lineEdit_DNI.setObjectName(u"lineEdit_DNI")
        self.lineEdit_DNI.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_DNI)

        self.label_Nombre = QLabel(self.formLayoutWidget)
        self.label_Nombre.setObjectName(u"label_Nombre")
        self.label_Nombre.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_Nombre)

        self.lineEdit_Nombre = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Nombre.setObjectName(u"lineEdit_Nombre")
        self.lineEdit_Nombre.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_Nombre)

        self.label_Apellidos = QLabel(self.formLayoutWidget)
        self.label_Apellidos.setObjectName(u"label_Apellidos")
        self.label_Apellidos.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_Apellidos)

        self.lineEdit_Apellidos = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Apellidos.setObjectName(u"lineEdit_Apellidos")
        self.lineEdit_Apellidos.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_Apellidos)

        self.label_Curso = QLabel(self.formLayoutWidget)
        self.label_Curso.setObjectName(u"label_Curso")
        self.label_Curso.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_Curso)

        self.lineEdit_Curso = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Curso.setObjectName(u"lineEdit_Curso")
        self.lineEdit_Curso.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_Curso)

        self.label_Nota1Ev = QLabel(self.formLayoutWidget)
        self.label_Nota1Ev.setObjectName(u"label_Nota1Ev")
        self.label_Nota1Ev.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_Nota1Ev)

        self.lineEdit_Nota1Ev = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Nota1Ev.setObjectName(u"lineEdit_Nota1Ev")
        self.lineEdit_Nota1Ev.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_Nota1Ev)

        self.label_Nota2Ev = QLabel(self.formLayoutWidget)
        self.label_Nota2Ev.setObjectName(u"label_Nota2Ev")
        self.label_Nota2Ev.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_Nota2Ev)

        self.lineEdit_Nota2Ev = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Nota2Ev.setObjectName(u"lineEdit_Nota2Ev")
        self.lineEdit_Nota2Ev.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_Nota2Ev)

        self.label_Nota3Ev = QLabel(self.formLayoutWidget)
        self.label_Nota3Ev.setObjectName(u"label_Nota3Ev")
        self.label_Nota3Ev.setStyleSheet(u"font: 75 12pt \"Calibri\";")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_Nota3Ev)

        self.lineEdit_Nota3Ev = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Nota3Ev.setObjectName(u"lineEdit_Nota3Ev")
        self.lineEdit_Nota3Ev.setStyleSheet(u"background-color:white")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.lineEdit_Nota3Ev)

        self.verticalLayoutWidget = QWidget(self.AniadirModificarEliminar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(550, 20, 201, 271))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.botonAniadirAlumno = QPushButton(self.verticalLayoutWidget)
        self.botonAniadirAlumno.setObjectName(u"botonAniadirAlumno")
        self.botonAniadirAlumno.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(70, 208, 205);\n"
" padding: 10px;\n"
" margin: 10px;\n"
"font: 75 12pt \"Calibri\";\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/rsc/Iconos/a\u00f1adir.png", QSize(), QIcon.Normal, QIcon.On)
        self.botonAniadirAlumno.setIcon(icon5)

        self.verticalLayout.addWidget(self.botonAniadirAlumno)

        self.botonModificar = QPushButton(self.verticalLayoutWidget)
        self.botonModificar.setObjectName(u"botonModificar")
        self.botonModificar.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(70, 208, 205);\n"
" padding: 10px;\n"
" margin: 10px;\n"
"font: 75 12pt \"Calibri\";\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/rsc/Iconos/editar.png", QSize(), QIcon.Normal, QIcon.On)
        self.botonModificar.setIcon(icon6)

        self.verticalLayout.addWidget(self.botonModificar)

        self.boton_Eliminar = QPushButton(self.verticalLayoutWidget)
        self.boton_Eliminar.setObjectName(u"boton_Eliminar")
        self.boton_Eliminar.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(70, 208, 205);\n"
" padding: 10px;\n"
" margin: 10px;\n"
"font: 75 12pt \"Calibri\";\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/rsc/Iconos/eliminar.png", QSize(), QIcon.Normal, QIcon.On)
        self.boton_Eliminar.setIcon(icon7)

        self.verticalLayout.addWidget(self.boton_Eliminar)

        self.tableView_2 = QTableView(self.AniadirModificarEliminar)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(20, 320, 821, 221))
        self.pestanias.addTab(self.AniadirModificarEliminar, icon, "")
        self.InformeAlumno = QWidget()
        self.InformeAlumno.setObjectName(u"InformeAlumno")
        icon8 = QIcon()
        icon8.addFile(u":/rsc/Iconos/pdf.png", QSize(), QIcon.Normal, QIcon.On)
        self.pestanias.addTab(self.InformeAlumno, icon8, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 30))
        self.menubar.setStyleSheet(u"background-color:(255, 255, 255)")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background-color:white")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.labelDNI.setBuddy(self.lineEdit_DNI)
        self.label_Nombre.setBuddy(self.lineEdit_Nombre)
        self.label_Apellidos.setBuddy(self.lineEdit_Apellidos)
        self.label_Curso.setBuddy(self.lineEdit_Curso)
        self.label_Nota1Ev.setBuddy(self.lineEdit_Nota1Ev)
        self.label_Nota2Ev.setBuddy(self.lineEdit_Nota2Ev)
        self.label_Nota3Ev.setBuddy(self.lineEdit_Nota3Ev)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAniadir)
        self.menuArchivo.addAction(self.actionModificarAlumno)
        self.menuArchivo.addAction(self.actionEliminar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGenerar_Informe)
        self.toolBar.addAction(self.actionAniadir)
        self.toolBar.addAction(self.actionModificarAlumno)
        self.toolBar.addAction(self.actionEliminar)
        self.toolBar.addAction(self.actionGenerar_Informe)

        self.retranslateUi(MainWindow)
        self.actionModificarAlumno.changed.connect(self.pestanias.show)
        self.actionAniadir.changed.connect(self.pestanias.show)
        self.actionEliminar.changed.connect(self.pestanias.show)

        self.pestanias.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Alumnos", None))
        self.actionAniadir.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir alumno", None))
#if QT_CONFIG(tooltip)
        self.actionAniadir.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionAniadir.setStatusTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Alumno", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionAniadir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar alumno", None))
#if QT_CONFIG(tooltip)
        self.actionEliminar.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar Alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionEliminar.setStatusTip(QCoreApplication.translate("MainWindow", u"Eliminar Alumno", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionEliminar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionModificarAlumno.setText(QCoreApplication.translate("MainWindow", u"ModificarAlumno", None))
#if QT_CONFIG(tooltip)
        self.actionModificarAlumno.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar registro del alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionModificarAlumno.setStatusTip(QCoreApplication.translate("MainWindow", u"Modificar registro", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionModificarAlumno.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionGenerar_Informe.setText(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
#if QT_CONFIG(tooltip)
        self.actionGenerar_Informe.setToolTip(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionGenerar_Informe.setStatusTip(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionGenerar_Informe.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pestanias.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pestanias.setStatusTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir alumno", None))
#endif // QT_CONFIG(statustip)
        self.labelDNI.setText(QCoreApplication.translate("MainWindow", u"DNI:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_DNI.setToolTip(QCoreApplication.translate("MainWindow", u"DNI", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_DNI.setStatusTip(QCoreApplication.translate("MainWindow", u"DNI", None))
#endif // QT_CONFIG(statustip)
        self.label_Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Nombre.setToolTip(QCoreApplication.translate("MainWindow", u"Nombre", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Nombre.setStatusTip(QCoreApplication.translate("MainWindow", u"Nombre", None))
#endif // QT_CONFIG(statustip)
        self.label_Apellidos.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Apellidos.setToolTip(QCoreApplication.translate("MainWindow", u"Apellidos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Apellidos.setStatusTip(QCoreApplication.translate("MainWindow", u"Apellidos", None))
#endif // QT_CONFIG(statustip)
        self.label_Curso.setText(QCoreApplication.translate("MainWindow", u"Curso:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Curso.setToolTip(QCoreApplication.translate("MainWindow", u"Curso", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Curso.setStatusTip(QCoreApplication.translate("MainWindow", u"Curso", None))
#endif // QT_CONFIG(statustip)
        self.label_Nota1Ev.setText(QCoreApplication.translate("MainWindow", u"Nota Primera Evaluaci\u00f3n:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Nota1Ev.setToolTip(QCoreApplication.translate("MainWindow", u"Nota Primera Evaluacion", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Nota1Ev.setStatusTip(QCoreApplication.translate("MainWindow", u"Nota Primera Evaluaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
        self.label_Nota2Ev.setText(QCoreApplication.translate("MainWindow", u"Nota Segunda Evaluaci\u00f3n:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Nota2Ev.setToolTip(QCoreApplication.translate("MainWindow", u"Nota Segunda Evaluacion", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Nota2Ev.setStatusTip(QCoreApplication.translate("MainWindow", u"Nota Segunda Evaluacion", None))
#endif // QT_CONFIG(statustip)
        self.label_Nota3Ev.setText(QCoreApplication.translate("MainWindow", u"Nota Tercera Evaluaci\u00f3n: ", None))
#if QT_CONFIG(statustip)
        self.lineEdit_Nota3Ev.setStatusTip(QCoreApplication.translate("MainWindow", u"Nota Tercera Evaluacion", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.botonAniadirAlumno.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.botonAniadirAlumno.setStatusTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir alumno", None))
#endif // QT_CONFIG(statustip)
        self.botonAniadirAlumno.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
#if QT_CONFIG(tooltip)
        self.botonModificar.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.botonModificar.setStatusTip(QCoreApplication.translate("MainWindow", u"Modificar Alumno", None))
#endif // QT_CONFIG(statustip)
        self.botonModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
#if QT_CONFIG(tooltip)
        self.boton_Eliminar.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar Alumno", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.boton_Eliminar.setStatusTip(QCoreApplication.translate("MainWindow", u"Eliminar alumno", None))
#endif // QT_CONFIG(statustip)
        self.boton_Eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pestanias.setTabText(self.pestanias.indexOf(self.AniadirModificarEliminar), QCoreApplication.translate("MainWindow", u"Base de Datos de Alumnos", None))
#if QT_CONFIG(tooltip)
        self.pestanias.setTabToolTip(self.pestanias.indexOf(self.AniadirModificarEliminar), QCoreApplication.translate("MainWindow", u"A\u00f1adir, modificar o eliminar alumnos", None))
#endif // QT_CONFIG(tooltip)
        self.pestanias.setTabText(self.pestanias.indexOf(self.InformeAlumno), QCoreApplication.translate("MainWindow", u"Informe del alumno", None))
#if QT_CONFIG(tooltip)
        self.pestanias.setTabToolTip(self.pestanias.indexOf(self.InformeAlumno), QCoreApplication.translate("MainWindow", u"Informe del Alumno", None))
#endif // QT_CONFIG(tooltip)
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
#if QT_CONFIG(tooltip)
        self.toolBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

