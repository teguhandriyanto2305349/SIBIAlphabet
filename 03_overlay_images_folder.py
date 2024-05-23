from PIL import Image 
import os

i = 0
dir_bg = r'E:\S3 UM\PROPOSAL DISERTASI\DATASET_SIBI_ABJAD_GOOOO\Background_Images\selected'
dir_img = r'E:\S3 UM\PROPOSAL DISERTASI\DATASET_SIBI_ABJAD_GOOOO\02_Transparent_Background\Y_trf' 
dir_out = r'E:\S3 UM\PROPOSAL DISERTASI\DATASET_SIBI_ABJAD_GOOOO\03_Overlay_Background\Y'

for filename_img in os.listdir(dir_img):
    img = Image.open(dir_img+"/"+filename_img)
    img_resized = img.resize((900, 900))
    prefix_img = filename_img.split(".png")[0]
    for filename_bg in os.listdir(dir_bg):
        #print(filename_bg," ",filename_img)
        bg = Image.open(dir_bg+"/"+filename_bg)
        bg_resized = bg.resize((900, 900))
        prefix_bg = filename_bg.split(".png")[0]
        bg_resized.paste(img_resized, (0,0), mask = img_resized)
        bg_resized.save(dir_out+"/"+prefix_bg+"__"+prefix_img+".png")
        i+=1
        print(i," Create ",prefix_bg+"__",prefix_img,".png")

print("FINISH")
