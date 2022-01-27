from asyncio.windows_events import NULL
import sys,os
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout,QApplication,QComboBox ,QMainWindow, QAbstractItemView,QMessageBox,QWizard,QWizardPage,QTextEdit, QHBoxLayout, QLabel
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel
from PySide6.QtCore import Qt,QUrl
from ui_design import Ui_MainWindow
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from datetime import datetime
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import pyqtgraph as pg
import sqlite3
from sqlite3 import Error
from pathlib import Path


db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("BDDalumnos.db")
db.open()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # Cargamos la UI
        self.setupUi(self)

    
         # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=db)
        # Establecemos Album como tabla del modelo
        self.modelo.setTable("persona")
        # Hacemos el select del modelo
        self.modelo.select()

        # Renombramos las cabeceras de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "DNI")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Apellidos")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Curso")
        self.modelo.setHeaderData(4, Qt.Horizontal, "Nota 1 Ev")
        self.modelo.setHeaderData(5, Qt.Horizontal, "Nota 2 Ev")
        self.modelo.setHeaderData(6, Qt.Horizontal, "Nota 3 Ev")

        self.tableView_2.setAlternatingRowColors(True)
        # Establecemos el modelo en el tableView
        self.tableView_2.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tableView_2.resizeColumnsToContents()

        # Deshabilitamos la edición directa de la tabla
        self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Establecemos que se seleccionen filas completas en lugar de celdas individuales
        self.tableView_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_2.setAlternatingRowColors(True)

        # Creamos la señal: Cuando cambie la seleccion, ejecuta self.seleccion
        self.tableView_2.selectionModel().selectionChanged.connect(self.seleccion)
        # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
        self.botonModificar.clicked.connect(self.modificar)
        self.actionModificarAlumno.triggered.connect(self.modificar)
        # Creamos la señal: Cuando se ejecute la acción Aniadir, ejecuta self.nueva
        self.botonAniadirAlumno.clicked.connect(self.nueva)
        self.actionAniadir.triggered.connect(self.nueva)
        # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
        self.actionEliminar.triggered.connect(self.borrar)
        self.boton_Eliminar.clicked.connect(self.borrar)
        self.actionGenerar_Informe.setDisabled(False)
        self.actionGenerar_Informe.triggered.connect(self.informe)

        # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
        self.fila = -1




        self.wizard = QWizard()

        self.wizard.setWizardStyle(QWizard.ModernStyle)
        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('Watermark.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('Logo.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('Banner.png'))

        self.page1 = QWizardPage()
        self.page1.setTitle('Generador de informes PDF')
        self.page1.setSubTitle('Generará un informe PDF detallado con los datos del alumno. ')
        self.labelNotaMedia = QLabel('¿Desea generar la nota final del alumno Si/No?:')
        self.comboBox_Bool_NotaMedia = QComboBox()
        self.comboBox_Bool_NotaMedia.addItem('Si')
        self.comboBox_Bool_NotaMedia.addItem('No')


        hLayout1 = QHBoxLayout(self.page1)
        hLayout1.addWidget(self.labelNotaMedia)
        hLayout1.addWidget(self.comboBox_Bool_NotaMedia)
        self.page1.registerField('miCampo', self.comboBox_Bool_NotaMedia,self.comboBox_Bool_NotaMedia.currentText())
        self.wizard.addPage(self.page1)

        self.page2 = QWizardPage()
        self.page2.setTitle('Gráficas')
        self.page2.setSubTitle('Mostrará graficas de las notas en comparación con los demás alumnos.')
        self.labelGraficas = QLabel('¿Desea mostrar graficas Si/No?')
        hLayout2 = QHBoxLayout(self.page2)
        self.comboBox_Bool_Graficas = QComboBox()
        self.comboBox_Bool_Graficas.addItem('Si')
        self.comboBox_Bool_Graficas.addItem('No')
        hLayout2.addWidget(self.labelGraficas)
        hLayout2.addWidget(self.comboBox_Bool_Graficas)
        self.page2.registerField('miCampo2',self.comboBox_Bool_Graficas,self.comboBox_Bool_Graficas.currentText())
        print(self.comboBox_Bool_Graficas.currentText())
        self.wizard.addPage(self.page2)

        self.page3 = QWizardPage()
        self.page3.setTitle('Informe del alumno: ')
        self.labelPaginaFin=QLabel('Pulse finalizar para generar el documento')
        hLayout3=QHBoxLayout(self.page3)
        hLayout3.addWidget(self.labelPaginaFin)
        self.page3.setFinalPage(True)
        self.wizard.addPage(self.page3)
        
         
        # Y también podemos recuperar la información cuando se complete el asistente
        finish = self.wizard.button(QWizard.FinishButton)
        # Por ejemplo, para cambiar el texto del label
        finish.clicked.connect(self.generate)

        

    def informe(self):
        dni = self.modelo.index(self.fila, 0).data()

        self.page1.setSubTitle(f'Informe del alumno con DNI: {dni}')
        self.wizard.show()

    def nueva(self):
        # Guardamos en la variable nuevaFila el número de filas del modelo
        nuevaFila = self.modelo.rowCount()
        # Insertamos una nueva fila en el modelo en la posición de ese valor
        self.modelo.insertRow(nuevaFila)
        # Seleccionamos la fila nueva
        self.tableView_2.selectRow(nuevaFila)

        # Cogemos los campos de los line edit
        dni = self.lineEdit_DNI.text()
        nombre = self.lineEdit_Nombre.text()
        apellidos = self.lineEdit_Apellidos.text()
        curso = self.lineEdit_Curso.text()
        nota1ev = self.lineEdit_Nota1Ev.text()
        nota2ev = self.lineEdit_Nota2Ev.text()
        nota3ev = self.lineEdit_Nota3Ev.text()
        
        # Establecemos en blanco los valores (título y artista) de esa nueva fila
        self.modelo.setData(self.modelo.index(nuevaFila, 0), dni)
        self.modelo.setData(self.modelo.index(nuevaFila, 1), nombre)
        self.modelo.setData(self.modelo.index(nuevaFila, 2), apellidos)
        self.modelo.setData(self.modelo.index(nuevaFila, 3), curso)
        self.modelo.setData(self.modelo.index(nuevaFila, 4), nota1ev)
        self.modelo.setData(self.modelo.index(nuevaFila, 5), nota2ev)
        self.modelo.setData(self.modelo.index(nuevaFila, 6), nota3ev)
        # Ejecutamos los cambios en el modelo
        self.modelo.submit()

        self.lineEdit_DNI.setText("")
        self.lineEdit_Nombre.setText("")
        self.lineEdit_Apellidos.setText("")
        self.lineEdit_Curso.setText("")
        self.lineEdit_Nota1Ev.setText("")
        self.lineEdit_Nota2Ev.setText("")
        self.lineEdit_Nota3Ev.setText("")
        QMessageBox.information(self, "Nueva Fila", "Se ha generado una nueva fila") 

    def seleccion(self, seleccion):
        # Recuerda que indexes almacena los índices de la selección
        if seleccion.indexes():
            # Nos quedamos con la fila del primer índice (solo se puede seleccionar una fila)
            self.fila = seleccion.indexes()[0].row()
            # Obtenemos los valores id, titulo y artista del modelo en esa fila
            dni = self.modelo.index(self.fila, 0).data()
            nombre = self.modelo.index(self.fila, 1).data()
            apellidos = self.modelo.index(self.fila, 2).data()
            curso = self.modelo.index(self.fila, 3).data()
            nota1ev = self.modelo.index(self.fila, 4).data()
            nota2ev = self.modelo.index(self.fila, 5).data()
            nota3ev = self.modelo.index(self.fila, 6).data()
            # Modificamos los campos del formulario para establecer esos valores
            self.lineEdit_DNI.setText(dni)
            self.lineEdit_Nombre.setText(nombre)
            self.lineEdit_Apellidos.setText(apellidos)
            self.lineEdit_Curso.setText(curso)
            self.lineEdit_Nota1Ev.setText(str(nota1ev))
            self.lineEdit_Nota2Ev.setText(str(nota2ev))
            self.lineEdit_Nota3Ev.setText(str(nota3ev))
        else:
            # Si no hay selección,  ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
            self.fila = -1

    def borrar(self):
        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            # Borramos la fila en el modelo
            self.modelo.removeRow(self.fila)
            # Actualizamos la tabla
            self.modelo.select()
            # Y ponemos la fila actual a -1
            self.fila = -1
            # Reseteamos los valores en los campos del formulario
            self.lineEdit_DNI.setText("")
            self.lineEdit_Nombre.setText("")
            self.lineEdit_Apellidos.setText("")
            self.lineEdit_Curso.setText("")
            self.lineEdit_Nota1Ev.setText("")
            self.lineEdit_Nota2Ev.setText("")
            self.lineEdit_Nota3Ev.setText("")
            QMessageBox.information(self, "Eliminado", "Se ha eliminado el alumno")

    def modificar(self):

        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            # Obtenemos los valores de los campos del formulario

            dni = self.lineEdit_DNI.text()
            nombre = self.lineEdit_Nombre.text()
            apellidos = self.lineEdit_Apellidos.text()
            curso = self.lineEdit_Curso.text()
            nota1ev = self.lineEdit_Nota1Ev.text()
            nota2ev = self.lineEdit_Nota2Ev.text()
            nota3ev = self.lineEdit_Nota3Ev.text()
            
            # Actualizamos los campos en el model

            self.modelo.setData(self.modelo.index(self.fila, 0), dni)
            self.modelo.setData(self.modelo.index(self.fila, 1), nombre)
            self.modelo.setData(self.modelo.index(self.fila, 2), apellidos)
            self.modelo.setData(self.modelo.index(self.fila, 3), curso)
            self.modelo.setData(self.modelo.index(self.fila, 4), nota1ev)
            self.modelo.setData(self.modelo.index(self.fila, 5), nota2ev)
            self.modelo.setData(self.modelo.index(self.fila, 6), nota3ev)
            # Ejecutamos los cambios en el modelo
            self.modelo.submit()
            QMessageBox.information(self, "Modificado", f"Se ha insertado el alumno con DNI: {dni}")

    def generate(self):
        self.actionGenerar_Informe.setDisabled(True)   
  

        BoolNotaMedia = self.page1.field('miCampo')
        BoolGraficas = self.page2.field('miCampo2')

        print(BoolNotaMedia)
        print(BoolGraficas)
            
        nota1ev=float(self.lineEdit_Nota1Ev.text())
        nota2ev=float(self.lineEdit_Nota2Ev.text())
        nota3ev=float(self.lineEdit_Nota3Ev.text())
        notaMedia=(nota1ev + nota2ev + nota3ev)/3

        self.data = {
            'dni': self.lineEdit_DNI.text(),
            'nombre': self.lineEdit_Nombre.text(),
            'apellidos': self.lineEdit_Apellidos.text(),
            'curso': self.lineEdit_Curso.text(),
            'notas1ev': self.lineEdit_Nota1Ev.text(),
            'notas2ev': self.lineEdit_Nota2Ev.text(),
            'notas3ev': self.lineEdit_Nota3Ev.text(),
            'notamedia':notaMedia
        }
        
        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        
        canvas.drawString(126, 500, self.data['dni'])

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(275, 638, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(165, 448, self.data['nombre'])

        canvas.drawString(181, 398, self.data['apellidos'])

        canvas.drawString(150, 345, self.data['curso'])

        canvas.drawString(275, 296, self.data['notas1ev'])

        canvas.drawString(275, 244, self.data['notas2ev'])

        canvas.drawString(275, 191,self.data['notas3ev'])

        canvas.drawString(252,140,str(notaMedia))

        canvas.save()
        

        # create list of floats
        #notas = [float(self.lineEdit_Nota1Ev.text()),float(self.lineEdit_Nota2Ev.text()),float(self.lineEdit_Nota3Ev.text())]
        #nombreCampos=['1 Evaluacion', '2 Evaluacion', '3 Evaluacion']

        # Generamos gráfica simple
        plt = pg.plot([1,5,2,4,3])

# Creamos una instancia de exportación con el ítem que queremos exportar
        exporter = pg.exporters.ImageExporter(plt.plotItem)

# Establecemos los parámetros de la exportación (anchura)
        exporter.parameters()['width'] = 100   # (afecta a la altura de forma proporcional)

# Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
        exporter.export('graphic.png')

        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 650
        canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

        canvas.save()
        

        self.PDFEmbed()

        QMessageBox.information(self, "Finalizado", "Se ha generado el PDF") 

  


    def PDFEmbed(self):
        # QWebEngineView es una vista de una web (vista de un navegador incrustada en una app)
        # Documentación de la clase: https://doc.qt.io/qtforpython/PySide6/QtWebEngineWidgets/QWebEngineView.html
        self.web = QWebEngineView(self.InformeAlumno)

        # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Obtenemos la ruta al documento PDF que queremos mostrar (a partir de la carpeta en la que se ejecuta el script)
        ruta = os.getcwd()
        rutaConPDF = ruta+"/result.pdf"

        # Cargamos el fichero con el protocolo file:// (por eso necesitábamos la ruta completa)
        # Usando http o https también se pueden cargar páginas web
        self.web.load(QUrl("file://"+rutaConPDF))

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())