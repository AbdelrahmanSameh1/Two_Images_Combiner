import numpy as np


class Mag_Phase_Mixer:

    def __init__(self, Boundaries_Editing_Img1, Boundaries_Editing_Img2):
        self.Boundaries_Editing_Img1 = Boundaries_Editing_Img1
        self.Boundaries_Editing_Img2 = Boundaries_Editing_Img2

    def Two_Img_Mixing(self):
        return np.real(np.fft.ifft2(np.fft.ifftshift(np.multiply(self.Boundaries_Editing_Img1, self.Boundaries_Editing_Img2))))
