import thinkplot
import thinkstats2
import pandas as pd
import numpy as np
import pytest

import import_ipynb
import solution_file

df = pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")

df_in = df.copy()
splitCol = "Gender"
group1 = "Male"
group2 = "Female"
comparedCol = "Weight"

columnUsed = "Height"
metric = 168
isOver = True

@pytest.mark.q1
def test_compareMeans():
    dataSet1 = df_in[df_in[splitCol]==group1]
    dataSet2 = df_in[df_in[splitCol]==group2]
    mean1 = dataSet1[comparedCol].mean()
    mean2 = dataSet2[comparedCol].mean()
    correctAnswer = mean1-mean2
    #print(correctAnswer == solution_file.compareTwoMeans())
    assert correctAnswer == solution_file.compareTwoMeans(df_in,comparedCol,splitCol,group1,group2) 

@pytest.mark.q2
def test_compareMedians():
    dataSet1 = df_in[df_in[splitCol]==group1]
    dataSet2 = df_in[df_in[splitCol]==group2]
    mean1 = dataSet1[comparedCol].median()
    mean2 = dataSet2[comparedCol].median()
    correctAnswer = mean1-mean2
    #print(correctAnswer == solution_file.compareTwoMedians())
    assert correctAnswer == solution_file.compareTwoMedians(df_in,comparedCol,splitCol,group1,group2)

#def test_countMeetsCutoff(df_in, columnUsed, metric, isOver):
@pytest.mark.q3
def test_countMeetsCutoff():
    columnToCheck = df_in[columnUsed]
    if isOver:
        filteredCol = columnToCheck[columnToCheck[columnUsed] > metric]
        correctAnswer = filteredCol.size
    else:
        filteredCol = columnToCheck[columnToCheck[columnUsed] < metric]
        correctAnswer = filteredCol.size
    #print(correctAnswer == solution_file.countMeetsCutoff())
    assert correctAnswer == solution_file.countMeetsCutoff(df_in,columnUsed, metric,isOver)