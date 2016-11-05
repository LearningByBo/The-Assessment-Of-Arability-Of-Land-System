# -*- coding: utf-8 -*-
from django.db import models
import numpy as np
import scipy as sp
from sklearn import tree
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

# Create your models here.
class Factor(models.Model):
    organic_matter = models.IntegerField()
    total_nitrogen = models.IntegerField()
    available_P = models.IntegerField()
    available_K = models.IntegerField()
    land_capability = models.IntegerField()

    # function __unicode__ must return a string value , or may get a error like : coercing to Unicode: need string or buffer, int found
    def __unicode__ (self):
        return self.organic_matter.__str__() + self.total_nitrogen.__str__() + self.available_P.__str__() + self.available_K.__str__() + self.land_capability.__str__()

    def generate_DesicionTree(self):
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
        with open("tree.dot", 'w') as f:
            f = tree.export_graphviz(clf, out_file=f)

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
        print(classification_report(y, answer, target_names = ['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']))

