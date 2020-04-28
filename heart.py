import pandas as pd
import matplotlib.pyplot as plt

ageList = []
sexList = []
cpList = []
trestbpsList = []
cholList = []
fbsList = []
restecgList = []
thalachList = []
exangList = []
oldpeakList = []
slopeList = []
caList = []
thalList = []
targetList = []


def load_data(filename):
    df = pd.read_csv(filename)
    return df

#generates a list of values for a specific column
def columnList(file, column_name, specList):
    columns = []
    for j in file.head(0):
        columns.append(j)
    column_df = pd.read_csv("heart.csv", usecols = columns)
    for i in column_df[column_name]:
        specList.append(i)

#creates lists for all columns
def create():
    columnList(load_data("heart.csv"), "age", ageList)
    columnList(load_data("heart.csv"), "sex", sexList)
    columnList(load_data("heart.csv"), "cp", cpList)
    columnList(load_data("heart.csv"), "trestbps", trestbpsList)
    columnList(load_data("heart.csv"), "chol", cholList)
    columnList(load_data("heart.csv"), "fbs", fbsList)
    columnList(load_data("heart.csv"), "restecg", restecgList)
    columnList(load_data("heart.csv"), "thalach", thalachList)
    columnList(load_data("heart.csv"), "exang", exangList)
    columnList(load_data("heart.csv"), "oldpeak", oldpeakList)
    columnList(load_data("heart.csv"), "slope", slopeList)
    columnList(load_data("heart.csv"), "ca", caList)
    columnList(load_data("heart.csv"), "thal", thalList)
    columnList(load_data("heart.csv"), "target", targetList)
    
def main():
    create()
    plt.scatter(targetList, sexList, alpha = 0.005, c = "blue", s = 100)
    plt.show()

# Make a function that calculates number of ones for each category
main()
