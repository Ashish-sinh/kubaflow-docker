from fastapi import FastAPI 
from fastapi.responses import StreamingResponse 

app = FastAPI()

@app.get("/Iris")
def plot_data(): 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    from sklearn.datasets import load_iris  
    import seaborn as sns 

    df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names) 
    df['target'] = load_iris().target  

    fig, axis = plt.subplots(2, figsize=(8,6)) 
    sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='target', ax=axis[0]) 
    sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='target', ax=axis[1]) 

    fig.savefig('iris.png') 
    file = open('iris.png','rb') 

    return StreamingResponse(file, media_type='image/png') 

