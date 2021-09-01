import plotly.express as px
import csv 

with open ("cups of coffee vs hours of sleep.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='Coffee in ml',y='sleep in hours',color='week')
    fig.show()

def findCorealation(datasource):
    corealtion=np.corrcoef(datasource["x"], datasource["y"])
    print("cups of coffe vs sleep:-\n-->",corealtion[0,1])
