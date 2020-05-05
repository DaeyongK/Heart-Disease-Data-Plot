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
    data = load_data("heart.csv")
    corr_matrix = data.corr(method="pearson")
    #data[["age"]].plot.hist()
    #with pd.option_context('display.max_columns', None):
        #print(corr_matrix)
    #plt.scatter(targetList, sexList, alpha = 0.005, c = "blue", s = 100)
    ageGroup()
    plt.show()

# Make a function that calculates number of ones for each category
def ageGroup():
    agerList = [0, 0, 0, 0, 0, 0]
    whList = [0, 0, 0, 0, 0, 0]
    perList = []
    rangeList = ["20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]
    for i in range(0, len(ageList)):
        if ageList[i] > 20 and ageList[i] <= 30:
            agerList[0] += 1
            if targetList[i] == 1:
                whList[0] += 1
        elif ageList[i] > 30 and ageList[i] <= 40:
            agerList[1] += 1
            if targetList[i] == 1:
                whList[1] += 1
        elif ageList[i] > 40 and ageList[i] <= 50:
            agerList[2] += 1
            if targetList[i] == 1:
                whList[2] += 1
        elif ageList[i] > 50 and ageList[i] <= 60:
            agerList[3] += 1
            if targetList[i] == 1:
                whList[3] += 1
        elif ageList[i] > 60 and ageList[i] <= 70:
            agerList[4] += 1
            if targetList[i] == 1:
                whList[4] += 1
        elif ageList[i] > 70 and ageList[i] <= 80:
            agerList[5] += 1
            if targetList[i] == 1:
                whList[5] += 1
    for i in range(0, len(agerList)):
        perList.append((whList[i]/agerList[i]) * 100)
    print(perList)
    plt.bar(rangeList, perList)

    
main()

