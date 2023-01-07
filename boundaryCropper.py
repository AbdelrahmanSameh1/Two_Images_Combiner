import numpy as np
import cv2


class Boundaries_Editing:
    def __init__(self, Boundaries, Mag_Checkbox, Phase_Checkbox, Img_After_Processes, Selection):
        self.Boundaries = Boundaries
        self.Selection = Selection
        self.Mag_Checkbox = Mag_Checkbox
        self.Phase_Checkbox = Phase_Checkbox
        self.Img_After_Processes = Img_After_Processes

    def IMAGE_CROPPING(self):
        if self.Selection == True:
            RESULT = np.abs(self.Img_After_Processes)
            RESULT = self.SELECT_CROPPING_INDICES(RESULT)
            if self.Mag_Checkbox == "true":
                RESULT = np.ones(RESULT.shape)
        elif self.Selection == False:
            RESULT = np.angle(self.Img_After_Processes)
            RESULT = self.SELECT_CROPPING_INDICES(RESULT)
            if self.Phase_Checkbox == 'true':
                RESULT = np.zeros(RESULT.shape)
            RESULT = np.exp(1j*RESULT)
        return RESULT

    def SELECT_CROPPING_INDICES(self, result):
        for HEIGHT in range(result.shape[0]):
            for WIDTH in range(result.shape[1]):
                if (WIDTH <= self.Boundaries[1][0] or WIDTH >= self.Boundaries[1][1]) or (HEIGHT < self.Boundaries[0][0] or HEIGHT >= self.Boundaries[0][1]):
                    result[HEIGHT][WIDTH] = self.Selection
        return result
