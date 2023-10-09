from roboflow import Roboflow
rf = Roboflow(api_key="PCJeKJYq8srNbgqs93xm")
project = rf.workspace("school-95f9t").project("human-detection-uerkn")
dataset = project.version(3).download("yolov8")
