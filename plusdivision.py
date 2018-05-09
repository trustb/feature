def interaction_features(train,test,x,y,profix):
    train["inter_{}*".format(profix)]=train[x]*train[y]
    train['inter_{}/'.format(profix)]=train[x]/train[y]
    test['inter_{}*'.format(profix)]=test[x]*test[y]
    test['inter_{}/'.format(profix)]=test[x]/test[y]
    return train,test
for e,(x,y) in enumerate(combinations(['ps_car_13', 'ps_ind_03', 'ps_reg_03', 'ps_ind_15', 'ps_reg_01', 'ps_ind_01'], 2)):
    train,test=interaction_features(train,test,x,y,e)
