import numpy as np
import pandas as pd
import os,sys,random

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from bisect import bisect_right, bisect_left
from tqdm import tqdm

from catboost import CatBoostRegressor

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, BatchNormalization
from keras.regularizers import l2, l1

from keras import layers

from sklearn.preprocessing import scale

def get_model(model_name):

    def SVM():
        model=SVC(gamma='auto', probability=True)
        return model

    def LR():
        model = LogisticRegression()
        return model

    def XGBOOST():
        model=GradientBoostingClassifier(max_features='auto')
        return model

    def RF():
        model=RandomForestClassifier()
        return model

    def ERT():
        model=ExtraTreesClassifier()
        return model

    def NN():
        dropout=0.5
        batchNorm=True
        num_classer=1

        model=Sequential()
        model.add(Dense(1024))
        if batchNorm:
            model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(dropout))
        model.add(Dense(512))
        if batchNorm:
            model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(dropout))
        model.add(Dense(num_classer,activation='sigmoid'))
        return model

    def CatBoost():
        params = {
             'iterations':600,
            'learning_rate':0.1,
            'depth':9,
            'loss_function':'RMSE'
        }
        model = CatBoostRegressor(**params)
        return model


    model = locals()[model_name]()
    return model



