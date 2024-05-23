from PIL import Image
import os

dir_jpg = r'E:\S3 UM\PROPOSAL DISERTASI\DATASET_SIBI_ABJAD_GOOOO\Mono_Background\Y'
dir_png = r'E:\S3 UM\PROPOSAL DISERTASI\DATASET_SIBI_ABJAD_GOOOO\01_PNG_Images\Y' 
i = 0
for filename in os.listdir(dir_jpg): 
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        im = Image.open(dir_jpg+"/"+filename)
        im.save(dir_png+"/"+prefix+'.png')
        i+=1
        print(i,' ',filename,' ==>.png')
print("FINISH")