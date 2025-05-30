from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from PySide6 import QtCore
from PySide6.QtGui import QPixmap, QImage, QPainter
import cv2
import sys
import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from ui_main import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # This creates all widgets as attributes of `self`
        
        self.setWindowTitle("Image Viewer")

        # Image data
        self.image = None
        self.scale_factor = 1.0
        self.offset = QtCore.QPoint(0, 0)
        self.dragging = False
        self.original_image = None  # Keep original for repeated processing

        # Connect buttons and sliders
        self.ui.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.load_button.clicked.connect(self.load_image)
        self.ui.zoom_in_button.clicked.connect(self.zoom_in)
        self.ui.zoom_out_button.clicked.connect(self.zoom_out)
        self.ui.circle_button.clicked.connect(self.circle_tumor)
        self.ui.precise_button.clicked.connect(self.apply_precise_edge)
        self.ui.reset_button.clicked.connect(self.reset_image)
        self.ui.horizontalSlider.valueChanged.connect(self.apply_gaussian)
        self.ui.horizontalSlider_2.valueChanged.connect(self.apply_threshold)
        self.ui.horizontalSlider_3.valueChanged.connect(self.apply_canny)
        self.ui.horizontalSlider_4.valueChanged.connect(self.apply_otsu)
       

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.dcm)"
        )

        if file_path:
            if file_path.lower().endswith(".dcm"):
                dicom = pydicom.dcmread(file_path)
                img = apply_voi_lut(dicom.pixel_array, dicom)

                if dicom.PhotometricInterpretation == "MONOCHROME1":
                    img = np.amax(img) - img

                img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
                img = img.astype(np.uint8)
                self.image = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            else:
                self.image = cv2.imread(file_path)

            self.original_image = self.image.copy()
            self.display_image(self.image)
        else:
            QMessageBox.warning(self, "Error", "Failed to load image.")
    def zoom_in(self):
        self.scale_factor *= 1.2
        self.display_image(self.image)

    def zoom_out(self):
        self.scale_factor /= 1.2
        if self.scale_factor < 1.0:
            self.scale_factor = 1.0 
        self.display_image(self.image)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.last_mouse_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.pos() - self.last_mouse_position
            self.offset += delta
            self.last_mouse_position = event.pos()
            self.display_image(self.image)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False


    def display_image(self, image):
        if image is None:
            return  
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_image)

        scaled_pixmap = pixmap.scaled(
            self.ui.image_label.size() * self.scale_factor,
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )

        canvas = QPixmap(self.ui.image_label.size())
        canvas.fill(QtCore.Qt.transparent)
        painter = QPainter(canvas)
        painter.drawPixmap(self.offset, scaled_pixmap)
        painter.end()
        self.ui.image_label.setPixmap(canvas)

    def apply_otsu(self):
        if self.original_image is not None:
            gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        
            ksize = self.ui.horizontalSlider_4.value()  # Get from slider
            if ksize % 2 == 0:
                ksize += 1
            ksize = max(1, ksize)
            blurred = cv2.GaussianBlur(gray, (ksize, ksize), 0)
            equalized = cv2.equalizeHist(blurred)
            _, otsu = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            self.image = cv2.cvtColor(otsu, cv2.COLOR_GRAY2BGR)
            self.display_image(self.image)

    def apply_canny(self):
        if self.original_image is not None:
            gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            low = 50
            high = self.ui.horizontalSlider_3.value()
            edges = cv2.Canny(gray, low, high)
            self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            self.display_image(self.image)

    def apply_threshold(self):
        if self.original_image is not None:
            gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            val = self.ui.horizontalSlider_2.value()
            _, thresh = cv2.threshold(gray, val, 255, cv2.THRESH_BINARY)
            self.image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
            self.display_image(self.image)

    def apply_gaussian(self):
        if self.original_image is not None:
            ksize = self.ui.horizontalSlider.value()
            # Kernel size must be odd and >= 1
            if ksize % 2 == 0:
                ksize += 1
            ksize = max(1, ksize)
            blurred = cv2.GaussianBlur(self.original_image, (ksize, ksize), 0)
            self.image = blurred
            self.display_image(self.image)

    def circle_tumor(self):
        if self.original_image is None:
            return

        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

    # Step 1: Preprocess the brain image
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 2: Mask bright regions - tumors are often hyperintense
        _, bright_mask = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY)

    # Step 3: Clean up noise
        kernel = np.ones((3, 3), np.uint8)
        bright_mask = cv2.morphologyEx(bright_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        bright_mask = cv2.dilate(bright_mask, kernel, iterations=2)

    # Step 4: Find candidate regions
        contours, _ = cv2.findContours(bright_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        best_contour = None
        best_score = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 150 or area > 4000:
                continue

            perimeter = cv2.arcLength(cnt, True)
            if perimeter == 0:
                continue

        # Circularity helps reject long, stringy blobs
            circularity = 4 * np.pi * area / (perimeter ** 2)

            if 0.4 < circularity < 1.2:
                mask = np.zeros_like(gray)
                cv2.drawContours(mask, [cnt], -1, 255, -1)
                mean_val = cv2.mean(gray, mask=mask)[0]

                score = mean_val * circularity * area
                if score > best_score:
                    best_score = score
                    best_contour = cnt

        result = self.original_image.copy()

        if best_contour is not None:
            (x, y), radius = cv2.minEnclosingCircle(best_contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(result, center, radius, (0, 0, 255), 3)
            self.image = result
            self.display_image(self.image)
        else:
            QMessageBox.information(self, "Tumor Detection", "No clear tumor region found.")

    def reset_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.scale_factor = 1.0
            self.offset = QtCore.QPoint(0, 0)
            self.display_image(self.image)

            self.ui.horizontalSlider.setValue(16)        #blur
            self.ui.horizontalSlider_2.setValue(125)    #threshold
            self.ui.horizontalSlider_3.setValue(125)    #canny
            self.ui.horizontalSlider_4.setValue(16)    #otsu

    def apply_precise_edge(self):
        if self.original_image is None:
            return

        scharr_x = cv2.Scharr(self.original_image, cv2.CV_64F, 1, 0)
        scharr_y = cv2.Scharr(self.original_image, cv2.CV_64F, 0, 1)
        cv2.imshow("Precise edge detected image", scharr_x)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


