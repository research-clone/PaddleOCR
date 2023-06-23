# paddleocr --image_dir=ppstructure/docs/table/1.png --type=structure --recovery=true --lang='en'

python3 predict_system.py \
    --image_dir=./vutt_test/test2.png \
    --det_model_dir=/home/vutt/.paddleocr/whl/det/ch/ch_PP-OCRv3_det_infer \
    --rec_model_dir=/home/vutt/.paddleocr/whl/rec/ch/ch_PP-OCRv3_rec_infer \
    --rec_char_dict_path=/home/vutt/miniconda3/envs/py38/lib/python3.8/site-packages/paddleocr/ppocr/utils/ppocr_keys_v1.txt \
    --table_model_dir="/home/vutt/.paddleocr/whl/table/ch_ppstructure_mobile_v2.0_SLANet_infer" \
    --table_char_dict_path=/home/vutt/miniconda3/envs/py38/lib/python3.8/site-packages/paddleocr/ppocr/utils/dict/table_structure_dict_ch.txt \
    --layout_model_dir=/home/vutt/.paddleocr/whl/layout/picodet_lcnet_x1_0_fgd_layout_cdla_infer \
    --layout_dict_path=/home/vutt/miniconda3/envs/py38/lib/python3.8/site-packages/paddleocr/ppocr/utils/dict/layout_dict/layout_cdla_dict.txt \
    --vis_font_path=../doc/fonts/simfang.ttf \
    --recovery=True \
    --output=./vutt_output/

# python3 predict_system.py \
#     --image_dir=ppstructure/recovery/UnrealText.pdf \
#     --recovery=True \
#     --use_pdf2docx_api=True \
#     --output=../output/