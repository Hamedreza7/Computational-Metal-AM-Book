from pathlib import Path
import numpy as np, pandas as pd
x=np.array([0.,1.]); W=np.array([[.2,.4],[-.3,.2]]); b=np.array([-.1,.1]); v=np.array([20.,15.]); c=5.; y=90.; lr=.001
sig=lambda z:1/(1+np.exp(-z)); a=W@x+b; h=sig(a); pred=v@h+c; e=pred-y; loss=.5*e*e; gv=e*h; gc=e; vn=v-lr*gv; cn=c-lr*gc; predn=vn@h+cn; en=predn-y
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'quantity':['h1','h2','prediction_before','error_before','loss_before','v1_new','v2_new','c_new','prediction_after','error_after'],'value':[h[0],h[1],pred,e,loss,vn[0],vn[1],cn,predn,en]}).to_csv(out/'manual_update.csv',index=False)
print(f'Prediction before: {pred:.3f} µm'); print(f'Prediction after: {predn:.3f} µm')
