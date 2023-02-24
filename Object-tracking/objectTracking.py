import imageai.Detaction import ObjectDetection
import os

execution_path = os.getcwd()
detector = ObjectDetection()
detector = setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detector = detector.detectObjectsfromImage(
    input_image=os.path.join(execution_path , "image.jpg"),
    output_image_path.join(execution_path , "imagenew.jpg")
)
for eachObject in detection:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"])