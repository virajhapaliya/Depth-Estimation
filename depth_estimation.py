from PIL import Image
import numpy as np
import requests
import torch
import time
import cv2
from transformers import DPTForDepthEstimation, DPTFeatureExtractor
import argparse
import os


def load_model(low_cpu_mem_usage=True):
    model = DPTForDepthEstimation.from_pretrained("Intel/dpt-hybrid-midas", low_cpu_mem_usage=low_cpu_mem_usage)
    feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-hybrid-midas")
    return model,feature_extractor

def generate_image(model,feature_extractor,image_name:str,
                    output_folder:str,show_image=True):
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    image_basename = os.path.basename(image_name).split('.')[0]
    depth_output_imagepath = os.path.join(output_folder,f"{image_basename}_depth.jpg")
    contacted_depth_output_imagepath = os.path.join(output_folder,f"{image_basename}_concate.jpg")

    image = Image.open(image_name)
    image_org  =cv2.imread(image_name)

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
    out_image = cv2.hconcat([grey_image, depth])

    cv2.imwrite(depth_output_imagepath,depth)
    cv2.imwrite(contacted_depth_output_imagepath,out_image)

    if show_image:
        out_image = cv2.resize(out_image,(1280,720))
        cv2.imshow("Image",out_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', help='Enter Single Image Path', type=str,required=True)
    parser.add_argument('-output', help='Enter Output Folder name', type=str,default='output')
    parser.add_argument('-show_image',help="Show output image",type=bool,default=True)

    args = parser.parse_args()

    model,feature_extractor = load_model()
    generate_image(model,feature_extractor,args.input,args.output,args.show_image)