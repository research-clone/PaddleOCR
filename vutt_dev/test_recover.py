import os
import cv2
from paddleocr import PPStructure,save_structure_res
from paddleocr.ppstructure.recovery.recovery_to_doc import sorted_layout_boxes, convert_info_docx

# Chinese image
# table_engine = PPStructure(recovery=True)
# English image
table_engine = PPStructure(recovery=True, 
                        lang='en',
                        structure_version="PP-StructureV2",
                        return_ocr_result_in_table=True,
                        use_pdf2docx_api=True)

save_folder = './pdftest'
img_path = './test2.png'
pdf_path = "./vbcp2.pdf"
# img = cv2.imread(pdf_path)
result = table_engine(pdf_path)
save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

for line in result:
    line.pop('img')
    print(line)

h, w, _ = img.shape
res = sorted_layout_boxes(result, w)
convert_info_docx(img, res, save_folder, os.path.basename(img_path).split('.')[0])