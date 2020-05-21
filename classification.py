import pickle
import pandas as pd
file='C:/Users/Bipin Gowda/PycharmProjects/GodsEye/rfc_model.sav'
loaded_model = pickle.load(open(file, 'rb'))

def classify(distance_vector):
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

