import numpy as np
from random import randint
import cv2


class Transform_Img:

    def __init__(self, Image):
        self.Image = Image

    @staticmethod
    def Result_Img_Dir(path):
        num = str(randint(1, 9000000))
        dir = path + num + ".png"
        # print("dir = ", dir)
        return dir

    @staticmethod
    # here we save the combined images
    def Result_Img_Saving(path, Image):
        with open(path, 'wb') as f:
            cv2.imwrite(path, Image)

    def Edit_Size(self, width, height):
        self.Image = cv2.resize(self.Image, (width, height))
        return self

    def Disc_Fourier_Trans(self):
        Img_To_Fourier = np.fft.fft2((self.Image))
        Shifted_Img_To_Fourier = np.fft.fftshift(Img_To_Fourier)
        self.Image = Shifted_Img_To_Fourier
        return self.Image

    def Trans_To_Gray(self):
        self.Image = cv2.imread(self.Image, cv2.IMREAD_GRAYSCALE)
        return self
