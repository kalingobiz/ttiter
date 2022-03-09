import pandas as pd
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import pickle
import shrink
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk
from nltk.classify import ClassifierI
from statistics import mode




class voteClassifer(ClassifierI):
    def __init__(self, *classifiers):
        self.classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf





data = pd.read_csv("ab/list.csv")
y = np.array(data)
imsizex = 200
size = 180
finalsizex = 150
finalsizey = 150
n_trainimg = y.shape[0]

'''def adjustim(x):
    kernel = np.array([[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0]], np.uint8)
    kernel3 = np.array([[0,0,0],[1,1,1],[0,0,0]], np.uint8)
    kernel2 = np.ones((3,3), np.uint8)
    img = cv.imread(x,0)
    #img = cv.GaussianBlur(img,(35,35), 30)
    img = cv.medianBlur(img, 9)
    img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
    #print(img.mean())
    
   # re, image = cv.threshold(img,70, 1, cv.THRESH_BINARY)
    #image = cv.erode(image, kernel2, iterations=1)
    #ret3,image = cv.threshold(img,0,70,cv.THRESH_BINARY+cv.THRESH_OTSU)
    image = cv.dilate(img, kernel2, iterations=1)
    image = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,5,7)
    #print(image)
   # image = image.take(range(50, 150), axis=0).take(range(50, 150), axis=1)
   
    image = cv.erode(image, kernel2, iterations=1)
    #image = cv.erode(image, kernel, iterations=1)
    image = cv.dilate(image, kernel3, iterations=1)
    #image = cv.erode(image, kernel2, iterations=1)

    return byzero(image)


def adjustim2(x):
    img = cv.imread(x, 0)
    img = cv.medianBlur(img, 11)
    #img = cv.GaussianBlur(img,(35,35), 13)
    img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
    #print(img.mean())
    #re, img = cv.threshold(img,80, 1, cv.THRESH_BINARY)
    image = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,35,19)
    #print(image)
    #image = image.take(range(10, 90), axis=0).take(range(10, 90), axis=1)
    kernel = np.array([[0,0,0],[1,1,1],[0,0,0]], np.uint8)
    kernel3 = np.array([[0,1,0],[0,1,0],[0,1,0]], np.uint8)
    kernel2 = np.ones((3,3), np.uint8)
    image = cv.erode(image, kernel, iterations=1)
    image = cv.dilate(image, kernel, iterations=1)
    image = cv.erode(image, kernel2, iterations=1)
    #image = cv.dilate(image, kernel3, iterations=1)
    return byzero(image)'''


def byzero(image):
    binaryImage3 = np.zeros((size, size), np.uint0)
    A = image
    for i in range(size):
        for j in range(size):

            if (A[i][j] == 0 and j > 40 and j < 175 and i < 165 and i > 40):
                binaryImage3[i][j] = 1

    return binaryImage3


def adjustim3(x):
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    kernel3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], np.uint8)
    kernel4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    img = cv.imread(x, cv.IMREAD_GRAYSCALE)
    '''b, g, r = cv.split(img)
    rgb = cv.merge([r,g,b])
    dst = cv.fastNlMeansDenoisingColored(img,None, 10, 10, 7, 21)
    b, g, r =cv.split(dst)
    rgbdst = cv.merge([r, g, b])'''
    # img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    # img2 = np.uint8(np.round((np.float64(img[:,:,1])+np.float64(img[:,:,1])+np.float64(img[:,:,2]))/3))
    # print(img2.dtype)
    # img = cv.medianBlur(img, 11)
    # <<<<<<< .mine
    img = cv.GaussianBlur(img, (17, 19), 23)
    # img= midpoint(img)
    '''||||||| .r10
    img = cv.GaussianBlur(img,(31,31), 33)
    #img= midpoint(img)
=======
    img = cv.GaussianBlur(img,(33,33), 31)
    #img= shrink.midpoint(img)
    >>>>>>> .r11'''

    # v= np.ones((15,15),np.uint8)/9
    # img = cv.filter2D(img, -1, v)
    # print(img.dtype)
    # img = cv.blur(img,(5,5))
    # img = cv.GaussianBlur(img,(31,31), 31)
    img = cv.dilate(img, np.ones((5, 5), np.uint8), iterations=1)
    img = cv.erode(img, np.ones((5, 5), np.uint8), iterations=1)

    img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
    # print(img.mean())
    # img = cv.blur(img,(3,3))
    img = cv.erode(img, kernel, iterations=1)
    img = cv.dilate(img, kernel, iterations=1)
    # re, image = cv.threshold(img,80, 1, cv.THRESH_BINARY)
    image = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 15)
    # print(image)
    # image = image.take(range(10, 90), axis=0).take(range(10, 90), axis=1)

    '''image = cv.erode(image, kernel, iterations=1)
    image = cv.erode(image, kernel3, iterations=1)
    image = cv.dilate(image, kernel2, iterations=1)
   
    image = cv.erode(image, kernel4, iterations=1)
    image = cv.dilate(image, kernel2, iterations=1)

#>>>>>>> .r11
    image = cv.erode(image, kernel, iterations=1)

    
    image = cv.dilate(image, kernel, iterations=1)
    image = cv.erode(image, kernel, iterations=1)
    #image = cv.dilate(image, kernel, iterations=1)'''
    image = cv.erode(image, kernel, iterations=1)
    image = cv.erode(image, kernel3, iterations=1)
    image = cv.dilate(image, kernel2, iterations=1)

    image = cv.erode(image, kernel4, iterations=1)
    image = cv.dilate(image, kernel2, iterations=1)
    image = cv.erode(image, kernel, iterations=1)

    image = cv.dilate(image, kernel, iterations=1)
    image = cv.erode(image, kernel, iterations=1)

    return byzero(image)


train = 1


def trainme():
    lists = np.empty([n_trainimg, finalsizex, finalsizey])
    classes = np.empty([n_trainimg])

    for i in range(0, y.shape[0]):
        x = "ab/upload\/" + y[i][0]
        if i % 50 == 0:
            print("training image data: ", i)
        image = shrink.shrink(x)

        lists[i] = image

        classes[i] = y[i][1]
        # print(image[:,:,1])

    # n_samples = len(lists)
    # axes2[0][1].imshow(lists[2,:,:])
    data = lists.reshape(n_trainimg, -1)
    classifier = svm.SVC(gamma='auto', kernel="linear", C=0.9, random_state=0)
    print(classes.shape)

    # Split data into train and test subsets
    X_train, X_test, y_train, y_test = train_test_split(data, classes, test_size=0.2, shuffle=True)
    # classifier.fit(data, classes)
    classifier.fit(X_train, y_train)
    predicted = classifier.predict(X_test)

    '''images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
    for ax, (image, prediction) in zip(axes[1, :], images_and_predictions[:4]):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title('Prediction: %i' % prediction)'''

    print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(y_test, predicted)))
    # disp = metrics.confusion_matrix(y_test, predicted)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix:\n%s" % disp)
    classifier.fit(data, classes)
    with open("svm.pickle", "wb") as f:
        pickle.dump(classifier, f)

    rfc = RandomForestClassifier(random_state=142)
    rfc.fit(data, classes)
    with open("Rforest.pickle", "wb") as f1:
        pickle.dump(rfc, f1)


    MNB_classifier = MultinomialNB()
    MNB_classifier.fit(X_train, y_train)
    #print("MNB_classifier Accuracy: ", (nltk.classify.accuracy(MNB_classifier, X_test)) * 100)
    MB_pred = MNB_classifier.predict(X_test)
    print("Classification report for MNB_classifier  %s:\n%s\n"
          % (MNB_classifier, metrics.classification_report(y_test, MB_pred)))
    # disp = metrics.confusion_matrix(y_test, MB_pred)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix for MNB_classifier:\n%s" % disp)

    BernoulliNB_classifier = BernoulliNB()
    BernoulliNB_classifier.fit(X_train, y_train)
    Bern_pred = BernoulliNB_classifier.predict(X_test)
    print("Classification report for BernoulliNB_classifier  %s:\n%s\n"
          % (BernoulliNB_classifier, metrics.classification_report(y_test, Bern_pred)))
    # disp = metrics.confusion_matrix(y_test, predicted)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix for BernoulliNB_classifier:\n%s" % disp)

    LinearSVC_classifier = LinearSVC(random_state=0, tol=1e-5, C=0.9)
    LinearSVC_classifier.fit(X_train, y_train)
    Lin_pred = LinearSVC_classifier.predict(X_test)
    print("Classification report for LinearSVC_classifier  %s:\n%s\n"
          % (LinearSVC_classifier, metrics.classification_report(y_test, Lin_pred)))
    # disp = metrics.confusion_matrix(y_test, Lin_pred)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix for LinearSVC_classifier:\n%s" % disp)


    NuSVC_classifier = NuSVC(gamma="auto", nu=0.03, kernel='linear')
    NuSVC_classifier.fit(X_train, y_train)

    NuS_pred = NuSVC_classifier.predict(X_test)
    print("Classification report for NuSVC_classifier  %s:\n%s\n"
          % (NuSVC_classifier, metrics.classification_report(y_test, NuS_pred)))
    # disp = metrics.confusion_matrix(y_test, NuS_pred)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix for NuSVC_classifier:\n%s" % disp)
    #NuSVC_classifier.fit(data, classes)
    with open("NuSVC.pickle", "wb") as f:
        pickle.dump(NuSVC_classifier, f)
    GaussianNB_classifier = GaussianNB()
    GaussianNB_classifier.fit(X_train, y_train)
    GNB_pred = GaussianNB_classifier.predict(X_test)
    print("Classification report for GaussianNB_classifier  %s:\n%s\n"
          % (GaussianNB_classifier, metrics.classification_report(y_test, GNB_pred)))
    # disp = metrics.confusion_matrix(y_test, GNB_pred)
    # # disp.figure_.suptitle("Confusion Matrix")
    # print("Confusion matrix for GaussianNB_classifier:\n%s" % disp)

    # X_train2, X_test2 = train_test_split(data22, test_size=0.2, shuffle=True)
    # naive_classifier = nltk.NaiveBayesClassifier.train(X_train2)
    # print("Orginal Naive bayes Accuracy: ", (nltk.classify.accuracy(classifier, X_test)) * 100)
    # classifier.show_most_informative_features(15)

    voted_classifier = voteClassifer(classifier, MNB_classifier, BernoulliNB_classifier, NuSVC_classifier,
                                      LinearSVC_classifier, NuSVC_classifier)
    print("voted_classifier Accuracy: ", (nltk.classify.accuracy(voted_classifier, X_test)) * 100)


# return rfc


def ploter():
    for i in range(1, y.shape[0]):
        # plt.subplot(510+i)
        # plt.Subplot.set_axis_off()
        print(y[i][1])
        plt.imshow(shrink.shrink("ab/upload/" + y[i][0]), cmap=plt.cm.gray_r)
        plt.show()


def binarize(x):
    img = cv.imread(x, 0)
    img = cv.medianBlur(img, 11)
    img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
    A = 0.889 * np.log(img + 1)
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)

    kernel2 = np.ones((3, 3), np.uint8)  # Gray level transformation by using log Transformation
    # Finding the avarage of intensity in R,G,B
    binaryImage3 = np.zeros((200, 200), np.uint8)
    A = np.uint8(A)  # Intializing 2-D array for storing the binary image
    avg = np.mean(A)
    img = cv.erode(img, kernel, iterations=1)
    img = cv.dilate(img, kernel, iterations=1)  # calculating the threshold
    image = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 23)
    # This loop will segment the image into two using the threshold 'avg'
    A = image
    for i in range(180):
        for j in range(180):

            if (A[i][j] == 1) and ((j > 40 and j < 150) and (i > 40 and i < 170)):
                binaryImage3[i][j] = 1

    p = cv.erode(binaryImage3, np.ones(3), iterations=1)
    # p=cv.dilate(p,np.ones(3))
    return p


def ClassNum(x):
    count = 0
    for i in range(1, y.shape[0]):
        if y[i][1] == x:
            count += 1
        else:
            pass
    print(count)


def Spesific_ploter(x):
    counts = 0
    for i in range(1, y.shape[0]):
        if y[i][1] == x:
            print(i)
            plt.imshow(shrink.shrink("ab/upload/" + y[i][0]))
            plt.show()
            counts += 1
        else:
            pass
    print("There Are ", counts, "training data for classes", x)
