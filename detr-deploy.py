from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import time
import cv2


# Open the default camera (usually the first camera device)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Read a frame from the camera
ret, frame = cap.read()

if not ret:
    print("Error: Could not capture frame.")
    cap.release()
    exit()

# Convert the OpenCV BGR image to RGB format
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Convert the RGB frame to a PIL Image
pil_image = Image.fromarray(rgb_frame)

# Save the PIL Image as an image file
image_filename = "captured_image.jpg"
pil_image.save(image_filename)

print(f"Image saved as {image_filename}")

# Release the camera
cap.release()

# Now you can use 'pil_image' as a PIL Image


# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
beginning = time.time()
# image  = Image.open('000000039769 - 01.jpg') 
image = pil_image

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.9
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
    )
end = time.time()
print(f'time elapsed {end - beginning}')