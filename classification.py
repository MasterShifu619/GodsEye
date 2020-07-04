import pickle
import pandas as pd
#file='C:/Users/Bipin Gowda/PycharmProjects/GodsEye/model_jairaj_home.sav'
#loaded_model = pickle.load(open(file, 'rb'))

def classify(distance_vector,env):
    file = 'C:/Users/Bipin Gowda/PycharmProjects/GodsEye/'+env+'.sav'
    loaded_model = pickle.load(open(file, 'rb'))
    l=[]
    for key, value in distance_vector.items():
        l.append(value)

    d=pd.DataFrame([l],columns=list('123456789123'))
    result = loaded_model.predict(d)
    print(result)
    if result=='V':
        return 'red'
    elif result=='NV':
        return 'lime'
    else:
        return 'lime'

