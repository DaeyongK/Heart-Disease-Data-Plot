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



#Loads the data and creates a dataframe for it
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



#Generates correlation matrix
def matrix():
    data = load_data("heart.csv")
    corr_matrix = data.corr(method="pearson")
    with pd.option_context('display.max_columns', None):
        print(corr_matrix)



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



def sexGroup():
    gList = [0, 0]
    whgList = [0, 0]
    pergList = []
    gxList = ["0", "1"]
    for i in range(0, len(sexList)):
        if sexList[i] == 0:
            gList[0] += 1
            if targetList[i] == 1:
                whgList[0] += 1
        elif sexList[i] == 1:
            gList[1] += 1
            if targetList[i] == 1:
                whgList[1] += 1
    for i in range(0, len(gList)):
        pergList.append((whgList[i]/gList[i]) * 100)
    plt.figure()
    plt.bar(gxList, pergList)
    plt.title("The Effect of Sex on Chance of Heart Disease")
    plt.xlabel("Sex")
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



def oldGroup():
    oldList = [0, 0, 0, 0, 0, 0]
    wholdList = [0, 0, 0, 0, 0, 0]
    peroldList = []
    oldxList = ["0-0.9", "1-1.9", "2-2.9", "3-3.9", "4-4.9", "5-6.9"]
    for i in range(0, len(oldpeakList)):
        if oldpeakList[i] >= 0 and oldpeakList[i] < 1:
            oldList[0] += 1
            if targetList[i] == 1:
                wholdList[0] += 1
        elif oldpeakList[i] >= 1 and oldpeakList[i] < 2:
            oldList[1] += 1
            if targetList[i] == 1:
                wholdList[1] += 1
        elif oldpeakList[i] >= 2 and oldpeakList[i] < 3:
            oldList[2] += 1
            if targetList[i] == 1:
                wholdList[2] += 1
        elif oldpeakList[i] >= 3 and oldpeakList[i] < 4:
            oldList[3] += 1
            if targetList[i] == 1:
                wholdList[3] += 1
        elif oldpeakList[i] >= 4 and oldpeakList[i] < 5:
            oldList[4] += 1
            if targetList[i] == 1:
                wholdList[4] += 1
        elif oldpeakList[i] >= 5 and oldpeakList[i] < 7:
            oldList[5] += 1
            if targetList[i] == 1:
                wholdList[5] += 1
    for i in range(0, len(oldList)):
        peroldList.append((wholdList[i]/oldList[i]) * 100)
    plt.figure()
    plt.bar(oldxList, peroldList)
    plt.title("The Effect of ST Depression Induced by Exercise Relative to Rest on Chance of Heart Disease")
    plt.xlabel("ST Depression (mm)")
    plt.ylabel("Percent with Heart Disease")



def slopeGroup():
    sList = [0, 0, 0]
    whsList = [0, 0, 0]
    persList = []
    sxList = ["0", "1", "2"]
    for i in range(0, len(slopeList)):
        if slopeList[i] == 0:
            sList[0] += 1
            if targetList[i] == 1:
                whsList[0] += 1
        elif slopeList[i] == 1:
            sList[1] += 1
            if targetList[i] == 1:
                whsList[1] += 1
        elif slopeList[i] == 2:
            sList[2] += 1
            if targetList[i] == 1:
                whsList[2] += 1
    for i in range(0, len(sList)):
        persList.append((whsList[i]/sList[i]) * 100)
    plt.figure()
    plt.bar(sxList, persList)
    plt.title("The Effect of the Slope of the Peak Exercise ST Segment on Chance of Heart Disease")
    plt.xlabel("Slope of the Peak Exercise ST Segment")
    plt.ylabel("Percent with Heart Disease")


 
def caGroup():
    cList = [0, 0, 0, 0, 0]
    whcList = [0, 0, 0, 0, 0]
    percList = []
    cxList = ["0", "1", "2", "3", "4"]
    for i in range(0, len(caList)):
        if caList[i] == 0:
            cList[0] += 1
            if targetList[i] == 1:
                whcList[0] += 1
        elif caList[i] == 1:
            cList[1] += 1
            if targetList[i] == 1:
                whcList[1] += 1
        elif caList[i] == 2:
            cList[2] += 1
            if targetList[i] == 1:
                whcList[2] += 1
        elif caList[i] == 3:
            cList[3] += 1
            if targetList[i] == 1:
                whcList[3] += 1
        elif caList[i] == 4:
            cList[4] += 1
            if targetList[i] == 1:
                whcList[4] += 1
    for i in range(0, len(cList)):
        percList.append((whcList[i]/cList[i]) * 100)
    plt.figure()
    plt.bar(cxList, percList)
    plt.title("The Effect of Number of Major Vessels Colored by Fluoroscopy on Chance of Heart Disease")
    plt.xlabel("Number of Major Vessels Colored by Fluoroscopy")
    plt.ylabel("Percent with Heart Disease")



#This main function executes all of the functions stated above
def main():
    create()
    matrix()
    ageGroup()
    cpGroup()
    thalachGroup()
    exangGroup()
    oldGroup()
    slopeGroup()
    sexGroup()
    caGroup()
    plt.show()


    
main()

