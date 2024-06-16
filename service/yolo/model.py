from ultralytics import YOLO
from yolo.config import Config

class YoloModel:
    def __init__(self) -> None:
        self.model = YOLO(model=Config.MODEL_PATH)

    def predict(self, image):
        results = self.model(image)

        # # Process results list
        # for result in results:
        #     boxes = result.boxes  # Boxes object for bounding box outputs
        #     masks = result.masks  # Masks object for segmentation masks outputs
        #     keypoints = result.keypoints  # Keypoints object for pose outputs
        #     probs = result.probs  # Probs object for classification outputs
        #     obb = result.obb  # Oriented boxes object for OBB outputs
        #     result.show()  # display to screen
        #     result.save(filename="result.jpg")  # save to disk

        return results
        
        