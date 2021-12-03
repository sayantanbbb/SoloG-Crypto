import os
from tensorflow.keras.models import load_model
import pickle
class HDD:
   
    def export(self,models,save,directory):
        try:
            os.mkdir(directory)
        except:
            pass
        for key in models.keys():
            model=models[key]
            if save=='pickle':
                pickle.dump(model,open(os.path.join(directory,f'{key}.lgdm'),'wb'))
            if save=='tf':
                model.save(os.path.join(directory,f'{key}.h5'))
    def load_models(self,directory,save):
        models=dict()
        for pth in os.listdir(directory):
            key=int(pth.split('.')[0])
            pth=os.path.join(directory,pth)
            if save=='pickle':
                models[key]=pickle.load(open(pth,'rb'))
            else:
                models[key]=load_model(pth)
        return models
            
hdd=HDD()
