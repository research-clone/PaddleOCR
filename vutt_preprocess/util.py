import os 

path = "/home/ai22/Documents/VUTT/ocr_reg_datasets/vi_dict.txt"
outpath = "/home/ai22/Documents/VUTT/ocr_reg_datasets/vi_dict_full.txt"
with open(outpath, "a+") as fout:
    with open(path, "r") as fin:
        dicts = fin.readlines()[0]
        chars = list(dicts)
        for c in chars:
            fout.write(c+"\n")
        fin.close()
    fout.close()