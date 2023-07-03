The SMD Void Calculator is a Python project designed to calculate the voids of solder joints. It is a simple tool that analyzes images of solder joints and accurately(relativley to how well you mark the areas) determines the void percentages.

## How it works

1. First, a pop-up window will appear, allowing you to select the image on which you want to calculate the void percentage.

   ![slika](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/34a3baf0-b839-44c1-8368-5fa8e6bc1783)

   


3. After selecting the image and clicking "Open," the image(in my example i will use a x-ray image of a soldered pcb) will open in a new window. You can start marking the areas as seen below:

   ![slika](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/4e97b5d2-09bc-4341-9b9b-6ffb23619672)

   

   - The first marked area is considered the entire soldered pad and is marked green.
   - All subsequent marked areas are considered voids and are marked in red.

4. When you finish marking the areas, press the "esc" key. A new window will appear, showing the calculated void percentage.
   ![slika](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/14fc9d68-9410-4b5c-9323-e8ff0935270d)

   

5. Press the "esc" key one more time to save the picture with the calculated void percentage in the app's directory. The saved picture will have the same name as the initial image, with "-measured" appended at the end.
   ![slika](https://github.com/icrnjavic/SMD-VoidCalculator/assets/32548477/246dbdb0-3f62-4c9e-8fa3-536fcb0306d6)

   

6. After saving the processed image, the application will close.
