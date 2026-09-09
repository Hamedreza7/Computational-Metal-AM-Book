from pathlib import Path
import numpy as np, pandas as pd, torch
import matplotlib.pyplot as plt

torch.manual_seed(7)
X=torch.tensor([[150.,.6],[150.,1.0],[250.,.6],[250.,1.0]])
y=torch.tensor([[110.],[90.],[150.],[120.]])
xmin=X.min(0).values; xmax=X.max(0).values
Xn=(X-xmin)/(xmax-xmin)
model=torch.nn.Sequential(torch.nn.Linear(2,8),torch.nn.Tanh(),torch.nn.Linear(8,1))
opt=torch.optim.Adam(model.parameters(),lr=0.02)
h=[]
for epoch in range(2500):
    opt.zero_grad(); xin=Xn.clone().requires_grad_(True); pred=model(xin); mse=torch.mean((pred-y)**2)
    grad=torch.autograd.grad(pred.sum(),xin,create_graph=True)[0]
    phys=torch.mean(torch.relu(-grad[:,0])**2)+torch.mean(torch.relu(grad[:,1])**2)
    loss=mse+0.1*phys; loss.backward(); opt.step()
    if epoch%20==0: h.append((epoch,float(mse.detach()),float(phys.detach())))
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True)
pred=model(Xn).detach().numpy().ravel(); pd.DataFrame(h,columns=['epoch','mse','physics_penalty']).to_csv(out/'training_history.csv',index=False)
fig,ax=plt.subplots(figsize=(6,4.5)); ax.scatter(y.numpy().ravel(),pred); lim=[80,160]; ax.plot(lim,lim,'--'); ax.set_xlim(lim); ax.set_ylim(lim); ax.set_xlabel('target width (µm)'); ax.set_ylabel('predicted width (µm)'); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'fit.png',dpi=180); plt.close(fig)
print('Predictions (µm):',np.round(pred,2).tolist())
