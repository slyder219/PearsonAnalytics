from scipy import stats
import os
import csv
import mysql.connector
import sys
import pandas as pd
sys.path.append(r'C:/Users/seanl/Documents/tempSysPath')

from password import password


# create a class that holds two sets of data and can perform different tests on them
class significance_tests:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def t_test(self):
        return stats.ttest_ind(self.data1, self.data2)

    def chi_squared(self):
        return stats.chisquare(self.data1, self.data2)

    def mann_whitney(self):
        return stats.mannwhitneyu(self.data1, self.data2)

    def wilcoxon(self):
        return stats.wilcoxon(self.data1, self.data2)

    def kruskal_wallis(self):
        return stats.kruskal(self.data1, self.data2)

    def f_test(self):
        return stats.f_oneway(self.data1, self.data2)

    def levene_test(self):
        return stats.levene(self.data1, self.data2)

    def anderson_darling(self):
        return stats.anderson_ksamp([self.data1, self.data2])

    def mood_test(self):
        return stats.mood(self.data1, self.data2)

    def bartlett_test(self):
        return stats.bartlett(self.data1, self.data2)

    def mann_whitney_ranksum(self):
        return stats.ranksums(self.data1, self.data2)

    def mann_whitney_u(self):
        return stats.mannwhitneyu(self.data1, self.data2)

    def kruskal_wallis(self):
        return stats.kruskal(self.data1, self.data2)

    def friedman_test(self):
        return stats.friedmanchisquare(self.data1, self.data2)

    def kstest(self):
        return stats.ks_2samp(self.data1, self.data2)

    def ks_2samp(self):
        return stats.ks_2samp(self.data1, self.data2)

    def ks_1samp(self):
        return stats.kstest(self.data1, self.data2)

    def ks_2samp(self):
        return stats.ks_2samp(self.data1, self.data2)

    def ks_1samp(self):
        return stats.kstest(self.data1, self.data2)

    def ks_2samp(self):
        return stats.ks_2samp(self.data1, self.data2)

    def ks_1samp(self):
        return stats.kstest(self.data1, self.data2)





if __name__ == '__main__':

    # connect to data base and run query to get the sets of data we want
    seniorCapGrades = 'select numericalgrade from combined where issenior = 1'
    juniorCapGrades = 'select numericalgrade from combined where isjunior = 1'


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database = "pearson"
    )

    cursor = conn.cursor()

    cursor.execute(seniorCapGrades)
    seniorCapGrades = cursor.fetchall()
    seniorCapGrades = [grade[0] for grade in seniorCapGrades]

    cursor.execute(juniorCapGrades)
    juniorCapGrades = cursor.fetchall()
    juniorCapGrades = [grade[0] for grade in juniorCapGrades]


    # create an instance of the significance_tests class
    tests = significance_tests(seniorCapGrades, juniorCapGrades)
    # print t test
    print(tests.t_test())

    