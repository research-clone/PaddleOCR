import lmdb
import os
import cv2
from tqdm import tqdm
import numpy as np

# Đường dẫn đến folder chứa các file ảnh và folder label
# train_paths = [
#     {'image_folder': './ocr_reg_datasets/train/images1/',
#      'label_folder': './ocr_reg_datasets/train/labels1/'},
#      {'image_folder': './ocr_reg_datasets/train/images2/',
#      'label_folder': './ocr_reg_datasets/train/labels2/'},
#      {'image_folder': './ocr_reg_datasets/train/images3/',
#      'label_folder': './ocr_reg_datasets/train/labels3/'},
#       {'image_folder': './ocr_reg_datasets/train/images4/',
#      'label_folder': './ocr_reg_datasets/train/labels4/'},
#       {'image_folder': './ocr_reg_datasets/train/images5/',
#      'label_folder': './ocr_reg_datasets/train/labels5/'},
#       {'image_folder': './ocr_reg_datasets/train/images6/',
#      'label_folder': './ocr_reg_datasets/train/labels6/'},
#       {'image_folder': './ocr_reg_datasets/train/images7/',
#      'label_folder': './ocr_reg_datasets/train/labels7/'},
# ]

val_paths = [
    {'image_folder': './ocr_reg_datasets/val/images1/',
     'label_folder': './ocr_reg_datasets/val/labels1/'},
     {'image_folder': './ocr_reg_datasets/val/images2/',
     'label_folder': './ocr_reg_datasets/val/labels2/'},
     {'image_folder': './ocr_reg_datasets/val/images3/',
     'label_folder': './ocr_reg_datasets/val/labels3/'},
]
# paths = train_paths
paths = val_paths
# Đường dẫn đến file LMDB sẽ được tạo
# lmdb_path = "./ocr_reg_lmdb/train/"
lmdb_path = "./ocr_reg_lmdb/val/"
# Mở file LMDB để ghi dữ liệu
env = lmdb.open(lmdb_path, map_size=int(1e12))


def checkImageIsValid(imageBin):
    if imageBin is None:
        return False
    imageBuf = np.frombuffer(imageBin, dtype=np.uint8)
    img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
    imgH, imgW = img.shape[0], img.shape[1]
    if imgH * imgW == 0:
        return False
    return True


# Khởi tạo transaction để ghi dữ liệu
with env.begin(write=True) as txn:
    # Duyệt qua các file ảnh trong folder
    cnt = 1
    cache = {}
    for path in paths:
        image_folder = path['image_folder']
        label_folder = path['label_folder']
        for image_file in tqdm(sorted(os.listdir(image_folder))):
            # Đọc file ảnh
            with open(os.path.join(image_folder, image_file), 'rb') as f:
                imageBin = f.read()
            if 'synth_data' not in image_folder:
                nparr = np.fromstring(imageBin, np.uint8)
                img_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                h, w, c = img_cv2.shape
                if h < 5 or w < 5:
                    # print('Continue')
                    continue

            # Đọc label tương ứng với file ảnh
            label_file = image_file[:-4] + ".txt"
            with open(os.path.join(label_folder, label_file), "r") as f:
                label = f.read().strip()

            # Ghi dữ liệu vào LMDB
            imageKey = 'image-%09d'.encode() % cnt
            labelKey = 'label-%09d'.encode() % cnt
            txn.put(imageKey, imageBin)
            txn.put(labelKey, label.encode())
            cnt += 1

    txn.put('num-samples'.encode(), str(cnt-1).encode())

# Đóng file LMDB
env.close()