# -*- coding: utf-8 -*-
from django.db import models
import numpy as np
import scipy as sp
from sklearn import tree
from sklearn import neighbors
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import sys


# Create your models here.
class Factor(models.Model):
    organic_matter = models.IntegerField()
    total_nitrogen = models.IntegerField()
    available_P = models.IntegerField()
    available_K = models.IntegerField()
    land_capability = models.IntegerField()

    # function __unicode__ must return a string value , or may get a error like : coercing to Unicode: need string or buffer, int found
    def __unicode__(self):
        return self.organic_matter.__str__() + self.total_nitrogen.__str__() + self.available_P.__str__() + self.available_K.__str__() + self.land_capability.__str__()

    @staticmethod
    def generate_DesicionTree():
        # 数据读入
        data = []
        labels = []
        factors = Factor.objects.all()
        for factor in factors:
            temp = []
            temp.append(factor.organic_matter)
            temp.append(factor.total_nitrogen)
            temp.append(factor.available_P)
            temp.append(factor.available_K)
            data.append(temp)
            labels.append(factor.land_capability)
        x = np.array(data)
        y = np.array(labels)
        print x
        print y

        # 拆分训练数据与测试数据
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # 使用信息熵作为划分标准，对决策树进行训练
        clf = tree.DecisionTreeClassifier(criterion='entropy')
        print(clf)
        clf.fit(x_train, y_train)

        # 把决策树结构写入文件
        # method 1
        #with open(sys.path[0] + '\\static\\model_file\\' + "tree.dot", 'w') as f:
        #    f = tree.export_graphviz(clf, out_file=f)
        # method 2
        fname = "decisiontree.dot"
        joblib.dump(clf, sys.path[0] + '\\static\\model_file\\' + fname,compress=3)

        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        print(clf.feature_importances_)

        # 测试结果的打印
        answer = clf.predict(x_train)
        print(x_train)
        print(answer)
        print(y_train)
        print(np.mean(answer == y_train))

        # 准确率与召回率
        precision, recall, fbeta_score, support = precision_recall_fscore_support(y_test, clf.predict(x_test))
        answer = clf.predict(x)
        print answer
        print y
        print(classification_report(y, answer,
                                    target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))
        return clf

    @staticmethod
    def predict_data(al_select,organic_matter, total_nitrogen, available_p, available_k):
        temp = []
        temp.append(organic_matter)
        temp.append(total_nitrogen)
        temp.append(available_p)
        temp.append(available_k)
        x = np.array(temp)

        if al_select == 'dt':
            # score : 0.93 0.90 0.89 20
            fname = "decisiontree.dot"
            dt_clf = joblib.load(sys.path[0] + '\\static\\model_file\\' + fname)
            answer = dt_clf.predict(x)
            score = 0.89
        elif al_select == 'knn':
            # score :  0.57 0.60 0.51 20
            fname = "knntree.dot"
            knn_clf = joblib.load(sys.path[0] + '\\static\\model_file\\' + fname)
            answer = knn_clf.predict(x)
            score = 0.51
        elif al_select == 'svm':
            # score : 0.91 0.85 0.85 20
            fname = "svmtree.dot"
            svm_clf = joblib.load(sys.path[0] + '\\static\\model_file\\' + fname)
            answer = svm_clf.predict(x)
            score = 0.85
        elif al_select == 'lr':
            # score : 0.69 0.70 0.69 20
            fname = "lrtree.dot"
            lr_clf = joblib.load(sys.path[0] + '\\static\\model_file\\' + fname)
            answer = lr_clf.predict(x)
            score = 0.69

        return answer,score

    @staticmethod
    def algorithm_compare():
        # 数据读入
        data = []
        labels = []
        factors = Factor.objects.all()
        for factor in factors:
            temp = []
            temp.append(factor.organic_matter)
            temp.append(factor.total_nitrogen)
            temp.append(factor.available_P)
            temp.append(factor.available_K)
            data.append(temp)
            labels.append(factor.land_capability)
        x = np.array(data)
        y = np.array(labels)
        # print x
        # print y

        # 拆分训练数据与测试数据
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Decision Tree Fit
        dt_clf = tree.DecisionTreeClassifier(criterion='entropy')
        # print(dt_clf)
        dt_clf.fit(x_train, y_train)
        # fname = "decisiontree.dot"
        # joblib.dump(dt_clf, sys.path[0] + '\\static\\model_file\\' + fname,compress=3)

        # KNN Fit
        knn_clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
        # print(knn_clf)
        knn_clf.fit(x_train, y_train)
        # fname = "knntree.dot"
        # joblib.dump(knn_clf, sys.path[0] + '\\static\\model_file\\' + fname,compress=3)

        # SVM Fit
        # C represent the request of the precision , but too large may cause overfitting
        svm_clf_linear = svm.LinearSVC(C=3.5)
        # print(svm_clf_rbf)
        svm_clf_linear.fit(x_train, y_train)
        # fname = "svmtree.dot"
        # joblib.dump(svm_clf_linear, sys.path[0] + '\\static\\model_file\\' + fname,compress=3)

        # LR Fit
        lr_clf = linear_model.LogisticRegression()
        # print(lr_clf)
        lr_clf.fit(x_train, y_train)
        # fname = "lrtree.dot"
        # joblib.dump(lr_clf, sys.path[0] + '\\static\\model_file\\' + fname,compress=3)

        # 测试结果的打印
        dt_answer = dt_clf.predict(x_train)
        # print(dt_answer)
        # print(y_train)

        # 准确率与召回率
        precision, recall, fbeta_score, support = precision_recall_fscore_support(y_test, dt_clf.predict(x_test))
        dt_x_answer = dt_clf.predict(x)
        # print dt_x_answer
        # print y
        # print(classification_report(y, dt_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))
        dt_report = classification_report(y, dt_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5','class 6'])

        # 测试结果的打印
        knn_answer = knn_clf.predict(x_train)
        # print(x_train)
        # print(knn_answer)
        # print(y_train)
        # print(np.mean(answer == y_train))

        # 准确率与召回率
        precision, recall, fbeta_score, support = precision_recall_fscore_support(y_test, knn_clf.predict(x_test))
        knn_x_answer = knn_clf.predict(x)
        # print knn_x_answer
        # print y
        # print(classification_report(y, knn_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))
        knn_report = classification_report(y, knn_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5','class 6'])

        # 测试结果的打印
        svm_answer = svm_clf_linear.predict(x_train)
        # print(x_train)
        # print(svm_answer)
        # print(y_train)
        # print(np.mean(answer == y_train))

        # 准确率与召回率
        precision, recall, fbeta_score, support = precision_recall_fscore_support(y_test, svm_clf_linear.predict(x_test))
        svm_x_answer = svm_clf_linear.predict(x)
        # print svm_x_answer
        # print y
        # print(classification_report(y, svm_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))
        svm_report = classification_report(y, svm_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5','class 6'])

        # 测试结果的打印
        lr_answer = lr_clf.predict(x_train)
        # print(x_train)
        # print(lr_answer)
        # print(y_train)
        # print(np.mean(answer == y_train))

        # 准确率与召回率
        precision, recall, fbeta_score, support = precision_recall_fscore_support(y_test, lr_clf.predict(x_test))
        lr_x_answer = lr_clf.predict(x)
        # print lr_x_answer
        # print y
        # print(classification_report(y, lr_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))
        lr_report = classification_report(y, lr_x_answer,target_names=['class 1', 'class 2', 'class 3', 'class 4', 'class 5','class 6'])

        data = []
        data.append(x)
        data.append(y)
        data.append(x_train)
        data.append(y_train)
        data.append(x_test)
        data.append(y_test)

        clf = []
        clf.append(dt_clf)
        clf.append(knn_clf)
        clf.append(svm_clf_linear)
        clf.append(lr_clf)

        clf_data = []
        clf_data.append(dt_answer)
        clf_data.append(dt_x_answer)
        clf_data.append(dt_report)
        clf_data.append(knn_answer)
        clf_data.append(knn_x_answer)
        clf_data.append(knn_report)
        clf_data.append(svm_answer)
        clf_data.append(svm_x_answer)
        clf_data.append(svm_report)
        clf_data.append(lr_answer)
        clf_data.append(lr_x_answer)
        clf_data.append(lr_report)

        return data, clf, clf_data
