import numpy as np
import cv2
import base64
from random import randint
from MagPhaseMixer import *
from Transformer import *
from boundaryCropper import *


def boundary_handling(edge):
    return int(float(edge))


def Img_Decode(encoded_img):
    return base64.b64decode(encoded_img.split(',')[1])


def Decode_Img_saveing(img, path):
    with open(path, 'wb') as f:
        f.write(img)


def Combine_Uploaded_Images(Boundaries1, Boundaries2, Phase_Checkbox, Mag_Checkbox, Selection):
    First_Img = Transform_Img("static/Imgs/uploaded_imgs/uploaded1.png")
    Second_Img = Transform_Img("static/Imgs/uploaded_imgs/uploaded2.png")
    Boundaries_Editing_Img1 = Boundaries_Editing(
        Boundaries1, Mag_Checkbox, Phase_Checkbox, First_Img.Trans_To_Gray().Edit_Size(width=639, height=426).Disc_Fourier_Trans(), (Selection == "option1")).IMAGE_CROPPING()
    Boundaries_Editing_Img2 = Boundaries_Editing(
        Boundaries2, Mag_Checkbox, Phase_Checkbox, Second_Img.Trans_To_Gray().Edit_Size(width=639, height=426).Disc_Fourier_Trans(), (Selection != "option1")).IMAGE_CROPPING()
    Result_Img = Mag_Phase_Mixer(
        Boundaries_Editing_Img1, Boundaries_Editing_Img2)
    Result_Img_Dir = Transform_Img.Result_Img_Dir("static/Imgs/result_img/")
    Transform_Img.Result_Img_Saving(
        Result_Img_Dir, Result_Img.Two_Img_Mixing())
    return Result_Img_Dir
