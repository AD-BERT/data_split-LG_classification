import os
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.pipeline import Pipeline
import numpy as np

def file2datalist(datadir):
    datalist = []
    for item in os.listdir(datadir):
        fname = os.path.join(datadir, item)
        lines = ''
        with open(fname) as f:
            for line in f:
                lines += ' ' + line.strip()
        # mask keywords used to split the text
        lines = lines.lower().replace('atopic dermatitis', '').replace(' eczema ', '')
        datalist.append(lines)
    return datalist

def checkOverlap(trainlist, devlist, testlist):
    devdup = 0
    for item in devlist:
        if item in trainlist or item in testlist:
            devdup += 1
    testdup = 0
    for item in testlist:
        if item in trainlist or item in devlist:
            testdup += 1
    print('dev-dup:', devdup, 'test-dup:', testdup)

if __name__ == "__main__":
    posdir = 'classification/AD_nonAD/pos/'
    negdir = 'classification/AD_nonAD/neg/'

    pos_train = file2datalist(posdir+'train/')
    pos_dev = file2datalist(posdir + 'dev/')
    pos_test = file2datalist(posdir + 'test/')

    neg_train = file2datalist(negdir + 'train/')
    neg_dev = file2datalist(negdir + 'dev/')
    neg_test = file2datalist(negdir + 'test/')

    print("pos train-dev-test #:", len(pos_train), len(pos_dev), len(pos_test))
    print("neg train-dev-test #:", len(neg_train), len(neg_dev), len(neg_test))
    # checkOverlap(pos_train, pos_dev, pos_test)
    # checkOverlap(neg_train, neg_dev, neg_test)
    # print(pos_train[0])


    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', LogisticRegression())])

    text_clf.fit(pos_train+neg_train, [1]*len(pos_train)+[0]*len(neg_train))
    predicted = text_clf.predict(pos_dev+neg_dev)
    # print(predicted)
    # evaluate
    acc = np.mean(predicted == [1]*len(pos_dev)+[0]*len(neg_dev))
    print('Accuracy: {}%'.format(round(100*acc, 2)))

