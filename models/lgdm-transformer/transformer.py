from tqdm import tqdm
class LSTMtransformer:
    models=dict()
    def pad_samples(self,arr,window):
        add=window*((arr.shape[0]//window)+1)-arr.shape[0]
    
        if add > 0:
            arr=np.array(list(arr)+list(np.zeros((add,))))
        return arr,add
    
    def create_samples(self,arr,targets,window):
        arr,pad=self.pad_samples(arr,window)
        targets,_=self.pad_samples(targets,window)

        s=0
        values=[]
        t=[]
        for s in tqdm(range(int(arr.shape[0]//window))):
            values.append(arr[s*window:(s+1)*window])
            t.append(targets[s*window:(s+1)*window])
        return np.array(values),np.array(t),pad
    def create_samples_no_targets(self,arr,window):
        arr,pad=self.pad_samples(arr,window)
    

        s=0
        values=[]
   
        for s in tqdm(range(int(arr.shape[0]//window))):
            values.append(arr[s*window:(s+1)*window])
           
        return np.array(values),pad

    def create_model(self,shape):
        input=Input(shape=shape)
        x=LSTM(64,return_sequences=True)(input)
        x=LSTM(64,return_sequences=True)(x)
        x=LSTM(64,return_sequences=True)(x)
  
        x=Dense(1,activation='tanh')(x)
        model=Model(input,x)
        return model
    def train(self,S,Y):
        for a in S:

            x,y,ad=self.create_samples(S[a],Y[a],1000)
            print(ad)
            X=x[...,np.newaxis]
            y=y[...,np.newaxis]
            X_train=X[:int(0.7*X.shape[0])]
            y_train=y[:int(0.7*y.shape[0])]
            X_test=X[int(X.shape[0]*0.7):]
            y_test=y[int(y.shape[0]*0.7):]
    
            print('Training model for {}'.format(a))
            model=self.create_model(X.shape[1:])
            model.compile(optimizer=Adam(0.001),loss='mse',metrics=['mae'])
            model.fit(X_train,y_train,epochs=5,batch_size=8,validation_data=(X_test,y_test))
            self.models[int(a)]=model
            model.save(f'{a}.h5')
    def predict(self,X,asset):
        model=self.models[int(asset)]
        x,p=self.create_samples_no_targets(X,1000)
        drop=x.shape[0]-p
        prediction=(model.predict(x).flatten())
        return prediction
lstm=LSTMtransformer()
