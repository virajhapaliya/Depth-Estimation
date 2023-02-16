from PIL import Image
import numpy as np
import requests
import torch
import time
import cv2
from transformers import DPTForDepthEstimation, DPTFeatureExtractor

model = DPTForDepthEstimation.from_pretrained("Intel/dpt-hybrid-midas", low_cpu_mem_usage=True)
feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-hybrid-midas")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
image = Image.open("test.jpg")
image_org  =cv2.imread("test.jpg")

start_time = time.time()
# prepare image for the model
inputs = feature_extractor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

# interpolate to original size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],
    mode="bicubic",
    align_corners=False,
)
print("Total TIME")
print(time.time()-start_time)
# visualize the prediction
output = prediction.squeeze().cpu().numpy()
formatted = (output * 255 / np.max(output)).astype("uint8")
depth = Image.fromarray(formatted)
# depth.show()
depth = np.asarray(depth)
grey_image = cv2.cvtColor(image_org,cv2.COLOR_BGR2GRAY)
print(grey_image.shape)
print(depth.shape)

out_image = cv2.hconcat([grey_image, depth])
out_image = cv2.resize(out_image,(1280,720))
cv2.imshow("Image",out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()