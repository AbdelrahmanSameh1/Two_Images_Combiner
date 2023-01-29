var script = document.createElement("script");
script.src = "https://code.jquery.com/jquery-3.6.0.min.js";
document.getElementsByTagName("head")[0].appendChild(script);

let Encoded_Img1 = "";
let Encoded_Img2 = "";

let Mag_Checkbox = document.getElementById("CheckboxMag");
Mag_Checkbox.addEventListener("change", (object) => {
  main();
});

let selections = document.getElementById("options1");
selections.addEventListener("change", (object) => {
  main();
});

let Phase_Checkbox = document.getElementById("CheckboxPhase");
Phase_Checkbox.addEventListener("change", (object) => {
  main();
});



let Image1_File = document.querySelector("#UploadImage1");
let First_Image = document.querySelector("#Image1");
let left1, right1, up1, down1;
let Inverter_Checkbox = document.getElementById("inverter");
Inverter_Checkbox.addEventListener("change", (object) => {
  console.log(Inverter_Checkbox.checked)
  main();
});
Image1_File.addEventListener("change", (object) => {
  if (object.target.files.length) {
    // console.log(e.target.files.length);
    const reader = new FileReader(); // createing object from fileReader class
    reader.onload = (object) => {
      if (object.target.result) {
        console.log(object.target.result);
        let element = document.createElement("img");
        element.id = "image";
        element.src = object.target.result;
        First_Image.innerHTML = "";
        First_Image.appendChild(element);
        Encoded_Img1 = object.target.result;
        // create Cropper object
        First_Image_Cropper = new Cropper(element, {
          guides: false,
          movable: false,
          zoomOnWheel: false,
          crop: function (object) {
            left11 = object.detail.x;
            right11 = object.detail.width + object.detail.x;
            up11 = object.detail.y;
            down11 = object.detail.height + object.detail.y;
              
          },
          // after cropping we call main() function
          cropend: function (object) {
            console.log(left1)
            console.log(right1)
            console.log(up1)
            console.log(down1)
            main();
          },
        });
      }
    };
    reader.readAsDataURL(object.target.files[0]);
  }
});

let Image2_File = document.querySelector("#UploadImage2");
let Second_Image = document.querySelector("#Image2");
let left2, right2, up2, down2;
Image2_File.addEventListener("change", (object) => {
  if (object.target.files.length) {
    const reader = new FileReader(); // create fileReader object
    reader.onload = (object) => {
      if (object.target.result) {
        let element2 = document.createElement("img");
        element2.id = "image";
        element2.src = object.target.result;
        Encoded_Img2 = object.target.result;
        Second_Image.innerHTML = "";
        Second_Image.appendChild(element2);
        Second_Image_Cropper = new Cropper(element2, {
          guides: false,
          zoomOnWheel: false,
          movable: false,
          crop: function (object) {
            left22 = object.detail.x;
            right22 = object.detail.width + object.detail.x;
            up22 = object.detail.y;
            down22 = object.detail.height + object.detail.y;

          },
          cropend: function (object) {
            main();
          },
        });
      }
    };
    reader.readAsDataURL(object.target.files[0]);
  }
});
let Combine = document.getElementById("Combine");
Combine.addEventListener("click", (object) => {
  object.preventDefault();
  main();
});






function main() {
  if (Inverter_Checkbox.checked) {
    left1 = 0;
    right1 = 230;
    up1 = 145;
    down1 = 345;
    left2 = 0;
    right2 = 230;
    up2 = 145;
    down2 = 345;
  } else {
    left1 = left11;
    right1 = right11;
    up1 = up11;
    down1 = down11;
    left2 = left22;
    right2 = right22;
    up2 = up22;
    down2 = down22;

  }
  // console.log(left1);
  // console.log(right1);
  const Selection = document.getElementById("options1");
  if (Encoded_Img1 == "" || Encoded_Img2 == "") {
    throw "Error : Please Upload The Images ";
  }
  Phase_Checkbox = document.querySelector("#CheckboxPhase").checked;
  // console.log(checkbox_value);
  Mag_Checkbox = document.querySelector("#CheckboxMag").checked;
  // using ajax to send the data to backend
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/processing",
    data: {
      Encoded_Img1: Encoded_Img1, Encoded_Img2: Encoded_Img2, Selection_Value: Selection.value,
      left1: left1, right1: right1, up1: up1, down1: down1, left2: left2, right2: right2, up2: up2, down2: down2,
      Phase_Checkbox: Phase_Checkbox, Mag_Checkbox: Mag_Checkbox,
    },
    success: function (Response) {
      console.log(Selection);
      console.log(Response);
      var New_Response = JSON.parse(Response);
      console.log(New_Response);
      var OuterResultContainer = document.getElementById("ResultCont");
      const InnerResultContainer = document.getElementById("Final");
      InnerResultContainer.remove();
      var ResultImage = document.createElement("div");
      ResultImage.className = "FinalImg";
      ResultImage.id = "Final";
      ResultImage.innerHTML = New_Response[1];
      OuterResultContainer.appendChild(ResultImage);
    },
  });
}
