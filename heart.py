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
    with pd.option_context('display.max_columns', None):
        print(corr_matrix)
    ageGroup()
    cpGroup()
    thalachGroup()
    exangGroup()
    plt.show()

# Make a function that calculates number of ones for each category
def ageGroup():
    agerList = [0, 0, 0, 0, 0, 0]
    whList = [0, 0, 0, 0, 0, 0]
    perList = []
    rangeList = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
    for i in range(0, len(ageList)):
        if ageList[i] >= 20 and ageList[i] < 30:
            agerList[0] += 1
            if targetList[i] == 1:
                whList[0] += 1
        elif ageList[i] >= 30 and ageList[i] < 40:
            agerList[1] += 1
            if targetList[i] == 1:
                whList[1] += 1
        elif ageList[i] >= 40 and ageList[i] < 50:
            agerList[2] += 1
            if targetList[i] == 1:
                whList[2] += 1
        elif ageList[i] >= 50 and ageList[i] < 60:
            agerList[3] += 1
            if targetList[i] == 1:
                whList[3] += 1
        elif ageList[i] >= 60 and ageList[i] < 70:
            agerList[4] += 1
            if targetList[i] == 1:
                whList[4] += 1
        elif ageList[i] >= 70 and ageList[i] < 80:
            agerList[5] += 1
            if targetList[i] == 1:
                whList[5] += 1
    for i in range(0, len(agerList)):
        perList.append((whList[i]/agerList[i]) * 100)
    plt.bar(rangeList, perList)
    plt.title("The Effect of Age on Chance of Heart Disease")
    plt.xlabel("Age Ranges")
    plt.ylabel("Percent with Heart Disease")
    
def cpGroup():
    cptList = [0, 0, 0, 0]
    whcpList = [0, 0, 0, 0]
    percpList = []
    cpxList = ["0", "1", "2", "3"]
    for i in range(0, len(cpList)):
        if cpList[i] == 0:
            cptList[0] += 1
            if targetList[i] == 1:
                whcpList[0] += 1
        elif cpList[i] == 1:
            cptList[1] += 1
            if targetList[i] == 1:
                whcpList[1] += 1
        elif cpList[i] == 2:
            cptList[2] += 1
            if targetList[i] == 1:
                whcpList[2] += 1
        elif cpList[i] == 3:
            cptList[3] += 1
            if targetList[i] == 1:
                whcpList[3] += 1
    for i in range(0, len(cptList)):
        percpList.append((whcpList[i]/cptList[i]) * 100)
    plt.figure()
    plt.bar(cpxList, percpList)
    plt.title("The Effect of Type of Chest Pain on Chance of Heart Disease")
    plt.xlabel("Chest Pain Type")
    plt.ylabel("Percent with Heart Disease")

def thalachGroup():
    tList = [0, 0, 0, 0, 0, 0, 0]
    whtList = [0, 0, 0, 0, 0, 0, 0]
    pertList = []
    txList = ["70-89", "90-109", "110-129", "130-149", "150-169", "170-189", "190-209"]
    for i in range(0, len(thalachList)):
        if thalachList[i] >= 70 and thalachList[i] < 90:
            tList[0] += 1
            if targetList[i] == 1:
                whtList[0] += 1
        elif thalachList[i] >= 90 and thalachList[i] < 110:
            tList[1] += 1
            if targetList[i] == 1:
                whtList[1] += 1
        elif thalachList[i] >= 110 and thalachList[i] < 130:
            tList[2] += 1
            if targetList[i] == 1:
                whtList[2] += 1
        elif thalachList[i] >= 130 and thalachList[i] < 150:
            tList[3] += 1
            if targetList[i] == 1:
                whtList[3] += 1
        elif thalachList[i] >= 150 and thalachList[i] < 170:
            tList[4] += 1
            if targetList[i] == 1:
                whtList[4] += 1
        elif thalachList[i] >= 170 and thalachList[i] < 190:
            tList[5] += 1
            if targetList[i] == 1:
                whtList[5] += 1
        elif thalachList[i] >= 190 and thalachList[i] < 210:
            tList[6] += 1
            if targetList[i] == 1:
                whtList[6] += 1
    for i in range(0, len(tList)):
        pertList.append((whtList[i]/tList[i]) * 100)
    plt.figure()
    plt.bar(txList, pertList)
    plt.title("The Effect of Maximum Haert Rate Achieved on Chance of Heart Disease")
    plt.xlabel("Maximum Heart Rate Achieved")
    plt.ylabel("Percent with Heart Disease")

def exangGroup():
    eList = [0, 0]
    wheList = [0, 0]
    pereList = []
    exList = ["0", "1"]
    for i in range(0, len(exangList)):
        if exangList[i] == 0:
            eList[0] += 1
            if targetList[i] == 1:
                wheList[0] += 1
        elif exangList[i] == 1:
            eList[1] += 1
            if targetList[i] == 1:
                wheList[1] += 1
    for i in range(0, len(eList)):
        pereList.append((wheList[i]/eList[i]) * 100)
    plt.figure()
    plt.bar(exList, pereList)
    plt.title("The Effect of Exercise Induced Angina on Chance of Heart Disease")
    plt.xlabel("Presence of Exercise Induced Angina")
    plt.ylabel("Percent with Heart Disease")
main()

