from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import pandas as pd
import pickle
##import shrink
import os
import numpy as np
import cv2
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
import cv2 as cv
import basic
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
#data = pd.read_csv("list.csv")
#y = np.array(data)

files="ghjg"
#size2=basic.size
default_image_size = tuple((256, 256))
model = load_model('H:/ggg.h5')

label_encoder = open(r'H:/label_transform.pkl', 'rb')
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

def shrink(x):
    image=basic.adjustim3(x)
    image = image.take(range(0, basic.finalsizex), axis=0).take(range(0, basic.finalsizey), axis=1)
    # image = cv.resize(image, (32, 32), interpolation=cv.INTER_CUBIC)
    #image = np.double(np.round((1.2 * np.log(image))))
    s = np.empty([basic.size, 2], dtype=int)
    s2 = np.empty([basic.size, 2], dtype=int)
    c = 0
    c2 = 0
    o = np.zeros((60, 80), dtype=int)
    o2 = np.zeros((60, 80), dtype=int)
    '''for a in range(image.shape[0]):
        for b in range(image.shape[1]):
            if image[a][b] == 1:
                image[a][b] = 1
            else:
                image[a][b] = 0'''
    k = 0
    k2 = 0
    for r2 in range(image.shape[1]):
        #print(image[r])
        if np.max(image[:,r2]) == 0:
            
            c2 = c2 + 1
        else:
            s2[k2][0] = r2
            k2 = k2 + 1
            c2 = 0
    #print(s2[0][0])    
    for r in range(image.shape[0]):
        #print(image[r])
        if np.max(image[r]) == 0:
            
            c = c + 1
        else:
            s[k][0] = r
            k = k + 1
            c = 0
     
    #print("first",s2[0][0])
    image2 = image.take(range(s[0][0], basic.finalsizex - c), axis=0).take(range(s2[0][0], basic.finalsizey-c2), axis=1)
    # print(60-image2.shape[0])
    #o = np.append(image2, np.int8(np.zeros((basic.size - image2.shape[0]) * basic.size))).reshape(basic.size, basic.size)
    # v = v
    # o = v
    image2 = cv.resize(image2, (basic.finalsizex, basic.finalsizey), interpolation=cv.INTER_NEAREST)
    # o = cv.dilate(o, kernel, iterations=1)
    # o = cv.erode(o, kernel, iterations=1)
    #o = o.take(range(0, basic.finalsizex), axis=0).take(range(30, 120), axis=1)
    #o = cv.resize(o, (16, 16), interpolation=cv.INTER_CUBIC)

    return image2


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
   app.run(host="127.0.0.1", port=8082)
