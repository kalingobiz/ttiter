from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import pandas as pd
import pickle
##import shrink
import os
import numpy as np

from os import listdir
from sklearn.preprocessing import LabelBinarizer
from keras.models import Sequential
##from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import img_to_array
from keras.models import load_model



app = Flask(__name__)

app.config['APPLICATION_ROOT']="upload/"
#shrink.files=0
FOLDER = os.path.join('static','test')
app.config['UPLOAD_FOLDER']=FOLDER
@app.route('/')
def upload_file():
   #s=pd.read_html("upload.html")
   #s=open("applications.html","rb")
   #list_templates()
   return render_template("upload.html")
	
d= np.empty([5,5],dtype=str)
__x__="jhjh "
import pandas as pd


import numpy as np
import cv2
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
#data = pd.read_csv("list.csv")
#y = np.array(data)

files="ghjg"
#size2=basic.size
default_image_size = tuple((256, 256))
model = load_model('ggg.h5')

label_encoder = open(r'label_transform.pkl', 'rb')
label_transformer = pickle.load(label_encoder)

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


def prediction(imgpath="1547811666136.jpg"):
    imar = convert_image_to_array(imgpath)
    npimagelist = np.array([imar], dtype=np.float16) / 225.0
    pred = model.predict(npimagelist)

##    print(label_transformer.inverse_transform(pred)[0])
    result = label_transformer.inverse_transform(pred)[0].replace('\n','')
    ret = result.split('_')
    return " ".join(ret)




@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():

    if request.method == 'POST':
          f = request.files['file']
          print (f)
##          s = request.form['class']
          #print(s)
          #print(f)
          f.save("static/test/"+secure_filename(f.filename))
          he= open("head.txt")
          head = he.read()
          fo= open("foot.txt")
          foot = fo.read()
          pre= open("preview.txt")
          preview = pre.read()
          pickle_in = open("svm.pickle","rb")
          
          x="static/test/"+secure_filename(f.filename)
##          image= shrink(x)
          predicted=[prediction(x)]
##          tests2 = image.reshape(1,-1)
##          shrink.files=np.str(x)
##          classifier = pickle.load(pickle_in)
##          predicted = classifier.predict(tests2)
##          print(predicted)
          
                
    
	

      
      
    uimage = os.path.join(app.config['UPLOAD_FOLDER'],request.files['file'].filename)     
    return render_template("heads.html",user_image=uimage, predict=predicted[0])
      
  	
		
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8082, debug=False)
