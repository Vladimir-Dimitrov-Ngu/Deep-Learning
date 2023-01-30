# Deep-Learning


1. Computer Vision. We have the OxfordIIITPet dataset in which there are the following pictures and masks : 

Picture            |  Mask
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/84929000/215315718-3692faba-c4a2-48ba-b519-58ae9a623bd5.png)  |  ![image](https://user-images.githubusercontent.com/84929000/215316254-f20a3dfd-339c-4656-b79f-f59150cffbbb.png)


![image](https://user-images.githubusercontent.com/84929000/215315750-41baf247-7d05-4da4-b821-bd1970bd6496.png) |
![image](https://user-images.githubusercontent.com/84929000/215316272-e4457b2c-6e38-40cb-bbaf-d9b971b4d912.png)


![image](https://user-images.githubusercontent.com/84929000/215315836-51c8fa6f-ab34-4317-8e2a-f028e45a0dc2.png)|![image](https://user-images.githubusercontent.com/84929000/215316284-60c6ff76-d3b0-45e4-8bc5-e4691685cbea.png)


**Task**: semantic segmentation. Guess the background, animal and 'dividing element'

**Model**: Unet

**Results:**

![image](https://user-images.githubusercontent.com/84929000/215321341-55634f48-8216-404d-922c-8dc6860601d6.png)

![image](https://user-images.githubusercontent.com/84929000/215321385-392f834c-c5e2-48e8-8652-3f471ae996f9.png)

![image](https://user-images.githubusercontent.com/84929000/215321966-47947dcc-8ac2-459f-a8bf-5baf7524411c.png)


2. Computer Vision. We have VOCDetection dataset in which there are the following pictures and bounding boxes:

![image](https://user-images.githubusercontent.com/84929000/215387732-66c3901b-bf0f-4536-97cb-496574bd4604.png)

![image](https://user-images.githubusercontent.com/84929000/215387764-568adda3-5024-4ba5-83d3-b031b7500d5d.png)

![image](https://user-images.githubusercontent.com/84929000/215387778-932c1516-18a4-4431-b2e9-1f10b65297d7.png)


**Task**: object detection. Guess 1 of 20 classes and frame it'

**Model**: FastRCNNPredictor

**Results:** Train mAP 0.68044 Valid mAP 0.37185

![image](https://user-images.githubusercontent.com/84929000/215387861-61a4a377-fd02-4b5e-9b1c-f737e874e626.png)

![image](https://user-images.githubusercontent.com/84929000/215387872-f6a94617-4825-4e96-b9c5-7ab9a7e45052.png)

![image](https://user-images.githubusercontent.com/84929000/215387904-df645c28-acd7-465b-88ad-723b112349dd.png)
