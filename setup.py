import plotly.express as px
import csv 
import numpy as np

def plotFigure(data_path):
    with open (data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Roll No',y='Marks In Percentage')
        fig.show()

def getDataSource(data_path):
    student_marks=[]
    day_present=[] 
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Roll No"]))
            day_present.append(float(row["Marks In Percentage"]))
    
    return{"x":student_marks,"y":day_present}

def findCorealation(datasource):
    corealtion=np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between student marks vs days present:-\n-->",corealtion[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findCorealation(datasource)
    plotFigure(data_path)

setup()
