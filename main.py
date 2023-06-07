import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

#Spremenljivke za point-e in slike.
areas = []
img = None
drawing = False
zoom_level = 1.0


#Izračun void-a.
def calculate_void_percentage():
    soldered_area = areas[0]
    individual_void_area = sum([cv2.contourArea(cv2.convexHull(np.array(contour))) for contour in areas[1:]])
    combined_void_area = individual_void_area

    if cv2.contourArea(cv2.convexHull(np.array(soldered_area))) == 0:
        return 0

    void_percentage = (combined_void_area / cv2.contourArea(cv2.convexHull(np.array(soldered_area)))) * 100
    return void_percentage

#Izpis izračunenega void-a.
def draw_text(image, text, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 0, 255)  # Red color za void-e.
    thickness = 2
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_position = (position[0], position[1] - text_size[1])
    cv2.putText(image, text, text_position, font, font_scale, color, thickness, cv2.LINE_AA)

#Označevanje območij solder pad/voids.
def draw_areas(image, areas):
    img_copy = image.copy()
    for i, contour in enumerate(areas):
        color = (0, 255, 0) if i == 0 else (0, 0, 255)
        cv2.polylines(img_copy, np.array([contour]), False, color, 1)
    return img_copy

#Poskus za zoomiranje -> še ni na nivoju.
def resize_image(image, zoom_level):
    new_width = int(image.shape[1] * zoom_level)
    new_height = int(image.shape[0] * zoom_level)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

#Sprememba kontrasti za lažjo označevanje voidov.
def adjust_contrast(image, contrast):
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast)
    return adjusted_image

def mouse_callback(event, x, y, flags, param):
    global areas, img, drawing, zoom_level
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        areas.append([(x, y)])
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            areas[-1].append((x, y))

#Kreacija popup-a za izbiro slike.
root = tk.Tk()
root.withdraw()

#Izbira input slike ter ime output slike.
image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
file_name = os.path.splitext(os.path.basename(image_path))[0]
new_file_name = file_name + "-measured"

#Beri izbrano sliko
img = cv2.imread(image_path)
original_img = img.copy()
contrast_factor = 1.5  #Vrednost za spreminjanje kontrasi
adjusted_img = adjust_contrast(img, contrast_factor)

#Kreiraj okno za Image in aktiviraj mouse callback.
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    img_copy = resize_image(adjusted_img, zoom_level)
    img_copy = draw_areas(img_copy, areas)
    cv2.imshow('Image', img_copy)
    key = cv2.waitKey(1) & 0xFF #Wait for key

    # + to zoom in
    if key == ord('+'):
        zoom_level += 0.1
        zoom_level = min(3.0, zoom_level)  # Max zoom = 3x
    # to zoom out
    elif key == ord('-'):
        zoom_level -= 0.1
        zoom_level = max(0.1, zoom_level)  # Minimum = 0.1x

    # enter za izpis kalkulacije void-a v terminalu.
    elif key == 13:
        void_percentage = calculate_void_percentage()
        print('Void Percentage:', void_percentage)

    # esc za izpis void-a ter ponovni esc za shranjevanje izračuna.
    elif key == 27:
        void_percentage = calculate_void_percentage()
        result_text = f'Void Percentage: {void_percentage:.2f}%'
        draw_text(img_copy, result_text, (10, img_copy.shape[0] - 10))
        for i, contour in enumerate(areas):
            area_size = cv2.contourArea(cv2.convexHull(np.array(contour)))
            print(f'Area {i + 1} Size:', area_size)
        cv2.imshow('Image with Void Percentage', img_copy)
        cv2.waitKey(0)
        cv2.imwrite(new_file_name+".jpg", img_copy)
        break
cv2.destroyAllWindows()
