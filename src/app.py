import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QInputDialog, QMessageBox
)
from PyQt6.QtGui import QPixmap
from src.vista.ui_main import Ui_MainWindow
from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexión de los menús
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionCirculo.triggered.connect(self.calcular_area_circulo)
        self.ui.actionTriangulo.triggered.connect(self.calcular_area_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.calcular_area_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.calcular_area_cuadrado)

        # Mostrar imagen con ruta absoluta
        ruta_imagen = r"C:\Users\Jhanp\OneDrive\Documentos\Universidad continental\Construccion de software\Semana 14\src\vista\img\figuras.png"
        if os.path.exists(ruta_imagen):
            pixmap = QPixmap(ruta_imagen)
            self.ui.labelImagen.setPixmap(pixmap)
            self.ui.labelImagen.setScaledContents(True)
        else:
            self.ui.labelImagen.setText("Imagen no encontrada")

    def calcular_area_circulo(self):
        radio, ok = QInputDialog.getDouble(self, "Círculo", "Radio:")
        if ok:
            if radio <= 0:
                QMessageBox.warning(self, "Error", "El radio debe ser mayor a cero.")
                return
            figura = Circulo(radio)
            area = figura.calcular_area()
            self.actualizar_vista("Círculo", "A = π × radio²", area, f"Radio: {radio}")

    def calcular_area_triangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Triángulo", "Base:")
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Triángulo", "Altura:")
            if ok2:
                if base <= 0 or altura <= 0:
                    QMessageBox.warning(self, "Error", "La base y la altura deben ser mayores a cero.")
                    return
                figura = Triangulo(base, altura)
                area = figura.calcular_area()
                self.actualizar_vista("Triángulo", "A = (base × altura) / 2", area,
                                      f"Base: {base}, Altura: {altura}")

    def calcular_area_rectangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Rectángulo", "Base:")
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Rectángulo", "Altura:")
            if ok2:
                if base <= 0 or altura <= 0:
                    QMessageBox.warning(self, "Error", "La base y la altura deben ser mayores a cero.")
                    return
                figura = Rectangulo(base, altura)
                area = figura.calcular_area()
                self.actualizar_vista("Rectángulo", "A = base × altura", area,
                                      f"Base: {base}, Altura: {altura}")

    def calcular_area_cuadrado(self):
        lado, ok = QInputDialog.getDouble(self, "Cuadrado", "Lado:")
        if ok:
            if lado <= 0:
                QMessageBox.warning(self, "Error", "El lado debe ser mayor a cero.")
                return
            figura = Cuadrado(lado)
            area = figura.calcular_area()
            self.actualizar_vista("Cuadrado", "A = lado × lado", area, f"Lado: {lado}")

    def actualizar_vista(self, figura, formula, area, datos):
        self.ui.labelResultado.setText(f"{figura} | {formula} | Área: {area:.2f}")
        self.ui.listHistorial.addItem(f"{figura} → {datos} → Área: {area:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Calculadora de Áreas")
    window.show()
    sys.exit(app.exec())
