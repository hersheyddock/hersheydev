import os
print(os.getcwd())

import sys
import matplotlib.pyplot as plt

print(os.getcwd())

os.chdir("/Users/heosangbeom/Desktop/VOC2007/JPEGImages")
os.getcwd()

import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# 이미지 정상 출력 여부 확인
image_path = ("/Users/heosangbeom/Desktop/VOC2007/JPEGImages/000001.jpg")

image = Image.open(image_path).convert("RGB")

plt.figure(figsize=(5,5))
plt.imshow(image)
plt.show()
plt.close()

# XML 데이터 파싱용 라이브러리 임포트
import xml.etree.ElementTree as Et
from xml.etree.ElementTree import Element, ElementTree

xml_path = ("/Users/heosangbeom/Desktop/VOC2007/Annotations/000001.xml")

print("XML parsing Start\n") #폭, 높이, 채널값 파싱
xml = open(xml_path, "r")
tree = Et.parse(xml)
root = tree.getroot()
size = root.find("size")
width = size.find("width").text
height = size.find("height").text
channels = size.find("depth").text

print("Image properties\nwidth : {}\nheight : {}\nchannels : {}\n".format(width, height, channels))

objects = root.findall("object")
print("Objects Description\n")
for _object in objects: #바운딩 박스 처리될 xmin, ymin, xmax, ymax 값 파싱
    name = _object.find("name").text
    bndbox = _object.find("bndbox")
    xmin = bndbox.find("xmin").text
    ymin = bndbox.find("ymin").text
    xmax = bndbox.find("xmax").text
    ymax = bndbox.find("ymax").text

    print("class : {}\nxmin : {}\nymin : {}\nxmax : {}\nymax : {}\n".format(name, xmin, ymin, xmax, ymax))

print("XML parsing END")

# 45도 회전한 이미지 출력 테스트
image = Image.open(image_path).convert("RGB")
image_new = image.rotate(45)
plt.figure(figsize=(5,5))
plt.imshow(image_new)
plt.show()
plt.close()

# Annotation XML 파일 파싱
IMAGE_FOLDER = "/Users/heosangbeom/Desktop/VOC2007/JPEGImages"
ANNOTATIONS_FOLDER = "/Users/heosangbeom/Desktop/VOC2007/Annotations"
dataset_path = sys.argv[1]

ann_root, ann_dir, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))

print("ROOT : {}\n".format(ann_root))
print("DIR : {}\n".format(ann_dir))
print("FILES : {}\n".format(ann_files))

for xml_file in ann_files:
    xml = open(os.path.join(ann_root, xml_file), "r")
    tree = Et.parse(xml)
    root = tree.getroot()

    size = root.find("size")

    width = size.find("width").text
    height = size.find("height").text
    channels = size.find("depth").text
    
print("Image properties\nwidth : {}\nheight : {}\nchannels : {}\n".format(width, height, channels))

objects = root.findall("object")
print("Objects Description")

for _object in objects:
        name = _object.find("name").text
        bndbox = _object.find("bndbox")
        xmin = bndbox.find("xmin").text
        ymin = bndbox.find("ymin").text
        xmax = bndbox.find("xmax").text
        ymax = bndbox.find("ymax").text

        print("class : {}\nxmin : {}\nymin : {}\nxmax : {}\nymax : {}\n".format(name, xmin, ymin, xmax, ymax))

# 이미지 파일을 45도 변환하여 라벨링하여 데이터 증강
img_root, img_dir, img_files = next(os.walk(os.path.join(dataset_path, IMAGE_FOLDER)))

for xml_file in ann_files:
    img_name = img_files[img_files.index(".".join([xml_file.split(".")[0], "jpg"]))]
    img_file = os.path.join(img_root, img_name)
    image = Image.open(img_file).convert("RGB")
    image_new = image.rotate(45)
    draw = ImageDraw.Draw(image_new)

    xml = open(os.path.join(ann_root, xml_file), "r")
    tree = Et.parse(xml)
    root = tree.getroot()

    size = root.find("size")

    width = size.find("width").text
    height = size.find("height").text
    channels = size.find("depth").text

    objects = root.findall("object")

    for _object in objects:
        name = _object.find("name").text
        bndbox = _object.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)

# matplotlib 라이브러리 활용하여 최종 이미지 데이터 출력
        draw.rectangle(((xmin, ymin), (xmax, ymax)), outline="red")
        draw.text((xmin, ymin), name)

    plt.figure(figsize=(10, 10))
    plt.imshow(image_new)
    plt.show()
    plt.close()

### 바운딩 박스의 좌표를 45도 회전했을시 어떻게 변환해야 하는지 몰라서 해당 부분은 생략함..
