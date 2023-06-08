# SMD Void Calculator

The SMD Void Calculator is a Python project designed to calculate the voids of solder joints. It is a simple tool that analyzes images of solder joints and accurately(relativley to how well you mark the areas) determines the void percentages.

## How it works

1. First, a pop-up window will appear, allowing you to select the image on which you want to calculate the void percentage.

   ![image](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/37f5334a-4cde-45ad-a43a-adc621b28e6c)

2. After selecting the image and clicking "Open," the image will open in a new window. You can start marking the areas as seen below:

   ![image](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/215928cf-162a-425e-ae95-dc2f02836e25)

   - The first marked area is considered the entire soldered pad and is marked green.
   - All subsequent marked areas are considered voids and are marked in red.

3. When you finish marking the areas, press the "esc" key. A new window will appear, showing the calculated void percentage.

   ![image](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/a8a5da3a-dab9-4df0-807c-52a7556744ba)

4. Press the "esc" key one more time to save the picture with the calculated void percentage in the app's directory. The saved picture will have the same name as the initial image, with "-measured" appended at the end.

   ![image](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/b0d2ac9f-ce93-4451-a4d0-7c388309b1e9)

5. After saving the processed image, the application will close.
