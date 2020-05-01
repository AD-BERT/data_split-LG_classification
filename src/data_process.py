import pandas as pd
import os
import random

def _createDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def csv2list(fdataname):
    data = pd.read_csv(fdataname)

    titles = data['Title']
    abstracts = data['Abstract']

    datalist = []
    for t, a in zip(titles, abstracts):
        datalist.append(str(t) + ' ' + str(a))
    return datalist

def separate_AD_nonAD(datalist):
    adlist = []
    eczemalist = []
    dermatitislist = []
    nonadlist = []
    for item in datalist:
        if 'atopic dermatitis' in item.lower():
            adlist.append(item)
        elif ' eczema ' in item.lower():
            eczemalist.append(item)
        elif ' dermatitis ' in item.lower():
            dermatitislist.append(item)
        else:
            nonadlist.append(item)
    return list(set(adlist)), list(set(eczemalist)), list(set(dermatitislist)), list(set(nonadlist))

def _TrainDevTest_split(datalist):
    random.shuffle(datalist)
    dev = datalist[:300]
    test = datalist[300:600]
    train = datalist[600:]
    return train, dev, test

def _writeOutData(datalist, dirname):
    _createDir(dirname)
    for i, item in enumerate(datalist):
        fname = dirname + str(i+1)+'.txt'
        with open(fname, 'w') as fw:
            fw.write(item)

def data_TrainDevTest(adlist, eczemalist):
    '''
    split adlist to dev=300, test=300, train=remaining
    randomly pick 2691 out of eczemalist, and do the same split
    '''
    posdir = 'AD_nonAD/pos/'
    negdir = 'AD_nonAD/neg/'
    random.shuffle(adlist)
    random.shuffle(eczemalist)
    eczemalist_now = eczemalist[:2691]

    pos_train, pos_dev, pos_test = _TrainDevTest_split(adlist)
    neg_train, neg_dev, neg_test = _TrainDevTest_split(eczemalist_now)

    _writeOutData(pos_train, posdir+'train/')
    _writeOutData(pos_dev, posdir+'dev/')
    _writeOutData(pos_test, posdir+'test/')

    _writeOutData(neg_train, negdir + 'train/')
    _writeOutData(neg_dev, negdir + 'dev/')
    _writeOutData(neg_test, negdir + 'test/')


if __name__ == "__main__":
    fdataname = 'pubmed_abstracts/ad_pubmed_abstracts.csv'
    datalist = csv2list(fdataname)
    adlist, eczemalist, dermatitislist, nonadlist = separate_AD_nonAD(datalist)
    print('AD:', len(adlist), '\neczema non-AD:', len(eczemalist),
          '\ndermatitis non-AD:', len(dermatitislist),'\nother non-AD:', len(nonadlist))

    data_TrainDevTest(adlist, eczemalist)




