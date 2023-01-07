from flask import Flask, render_template, request
import os
import json
from starter import *


app = Flask(__name__)


@app.route('/processing', methods=['POST', "GET"])
def processing():
    if request.method == "POST":

        PATH = "static/Imgs/result_img"
        PATH1 = './static/Imgs/uploaded_imgs/uploaded1.png'
        PATH2 = './static/Imgs/uploaded_imgs/uploaded2.png'

        BoundariesImg1 = ((boundary_handling(request.form["up1"]), boundary_handling(request.form["down1"])), (
            boundary_handling(request.form["left1"]), boundary_handling(request.form["right1"])))
        BoundariesImg2 = ((boundary_handling(request.form["up2"]), boundary_handling(request.form["down2"])), (
            boundary_handling(request.form["left2"]), boundary_handling(request.form["right2"])))
        Selection = request.form["Selection_Value"]
        Decode_Img_saveing(Img_Decode(request.form["Encoded_Img1"]),
                           PATH1)
        Decode_Img_saveing(Img_Decode(request.form["Encoded_Img2"]),
                           PATH2)
        All_Images = os.listdir(PATH)
        for i in All_Images:
            Image_Path = PATH + "/" + i
            os.remove(Image_Path)
        Final_Image = Combine_Uploaded_Images(BoundariesImg1, BoundariesImg2,
                                              request.form["Phase_Checkbox"], request.form["Mag_Checkbox"], Selection)
    return json.dumps({1: f'<img src="{Final_Image}"  id="FINAL_RESULT" alt="" >'})


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
