# -*- coding: utf-8 -*-
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
def getVector(vector):
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    ans = loaded_model.predict(vector)
    return ((np.where(ans>0.5, 1,0)), ans)



def getNext(vector):
    future_lectures = pd.read_excel('будущие лекции.xlsx')
    tmp = future_lectures[['Направление']].values
    print(vector[0][tmp[2][0]])
    for i in range(tmp.size):
        if (vector[0][tmp[i][0]]==1):
            print(future_lectures.loc[[i]])
            break
        
        
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def draw(data_values):
    data_names = [ 'Социальные проекты', 'Молодые профессионалы', 'Лидерские проекты',
                  'Национальная Технологическая Инициатива', 'Инфраструктурные проекты', 'Цифровая экономика', 'Направление «Развитие регионов»',
                  'Направление "Новый бизнес"', 'Департамент по коммуникациям','Корпоративный департамент','Административный департамент']
    
    
    dpi = 100
    fig = plt.figure(dpi = dpi, figsize = (1280 / dpi, 720 / dpi) )
    mpl.rcParams.update({'font.size': 10})
    
    plt.title('Предполагаемое распределение ваших интересов')
    
    xs = range(len(data_names))
    
    plt.pie( 
        np.squeeze(data_values), autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) )])
    plt.legend(
        bbox_to_anchor = (-0.6, 0.50, 0.25, 0.25),
        loc = 'lower left', labels = data_names )
    fig.savefig('pie.png')
    
(x,y) = getVector(np.array([[0,0,0,0,7,0,0,0,0,0,0,0]]))
print(y)
draw(y)