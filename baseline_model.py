import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from xgboost import plot_importance
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error,accuracy_score, f1_score,roc_auc_score, recall_score, precision_score
from sklearn.model_selection import cross_val_score

def baseline_prediction(X,y):
    '''
    This function will take input of the dataset split into the feature set and target
    It runs logistic regression, decision tree, random forest, and xgboost
    output train and test scores'''
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=99)

    # Scaling is Needed for Knn
    scaler = StandardScaler()  
    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)  
    X_test_scaled = scaler.transform(X_test)

    # Logistic Regression
    lr_base = LogisticRegression(random_state=99)
    lr_base.fit(X_train,y_train)
    pred_lr_base = lr_base.predict(X_train)
    score_lr_base = accuracy_score(y_train,pred_lr_base)
    
    pred_lr_base_test = lr_base.predict(X_test)
    score_lr_base_test = accuracy_score(y_test,pred_lr_base_test)
    print('Logistic Regression Accuracy\nTrain={} Test={}'.format(round(score_lr_base,3),round(score_lr_base_test,3)))
    
    
    # Decision Tree
    tree_base = DecisionTreeClassifier(max_depth=15)
    tree_base.fit(X_train,y_train)
    pred_tree_base = tree_base.predict(X_train)
    score_tree_base = accuracy_score(y_train,pred_tree_base)

    pred_tree_base_test = tree_base.predict(X_test)
    score_tree_base_test = accuracy_score(y_test,pred_tree_base_test)
    print('Decision Tree Accuracy\nTrain={} Test={}'.format(round(score_tree_base,3),round(score_tree_base_test,3)))

          
    # Random Forest
    rand_base = RandomForestClassifier()
    rand_base.fit(X_train,y_train)
    pred_rand_base = rand_base.predict(X_train)
    score_rand_base = accuracy_score(y_train,pred_rand_base)

    pred_rand_base_test = rand_base.predict(X_test)
    score_rand_base_test = accuracy_score(y_test,pred_rand_base_test)
    print('Random Forest Accuracy\nTrain={} Test={}'.format(round(score_rand_base,3),round(score_rand_base_test,3)))

    
    #XG Boost
    xg_base = xgb.XGBClassifier(objecteve='binary:logistic')
    xg_base.fit(X_train,y_train)
    pred_xg_base = xg_base.predict(X_train)
    score_xg_base = accuracy_score(y_train,pred_xg_base)

    pred_xg_base_test = xg_base.predict(X_test)
    score_xg_base_test = accuracy_score(y_test,pred_xg_base_test)
    print('XGBoost Accuracy\nTrain={} Test={}'.format(round(score_xg_base,3),round(score_xg_base_test,3)))