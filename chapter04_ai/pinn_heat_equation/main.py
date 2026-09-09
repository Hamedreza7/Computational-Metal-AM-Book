from pathlib import Path
import numpy as np, pandas as pd, torch
import matplotlib.pyplot as plt

torch.manual_seed(4); ALPHA=0.1
net=torch.nn.Sequential(torch.nn.Linear(2,24),torch.nn.Tanh(),torch.nn.Linear(24,24),torch.nn.Tanh(),torch.nn.Linear(24,1))
def trial(x,t):
    z=torch.cat([x,t],1); return (1-t)*torch.sin(torch.pi*x)+x*(1-x)*t*net(z)
def residual(x,t):
    x=x.requires_grad_(True); t=t.requires_grad_(True); T=trial(x,t)
    Tt=torch.autograd.grad(T,t,torch.ones_like(T),create_graph=True)[0]
    Tx=torch.autograd.grad(T,x,torch.ones_like(T),create_graph=True)[0]
    Txx=torch.autograd.grad(Tx,x,torch.ones_like(Tx),create_graph=True)[0]
    return Tt-ALPHA*Txx
opt=torch.optim.Adam(net.parameters(),lr=0.004); hist=[]
for e in range(1200):
    opt.zero_grad(); x=torch.rand(256,1); t=torch.rand(256,1); r=residual(x,t); loss=(r*r).mean(); loss.backward(); opt.step()
    if e%20==0: hist.append((e,float(loss.detach())))
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame(hist,columns=['epoch','physics_loss']).to_csv(out/'training_history.csv',index=False)
xv=np.linspace(0,1,201); tv=.5; xt=torch.tensor(xv[:,None],dtype=torch.float32); tt=torch.full_like(xt,tv)
with torch.no_grad(): yp=trial(xt,tt).numpy().ravel()
ye=np.exp(-ALPHA*np.pi**2*tv)*np.sin(np.pi*xv)
fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(xv,ye,label='exact'); ax.plot(xv,yp,'--',label='PINN'); ax.set_xlabel('x'); ax.set_ylabel('T'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'pinn_vs_exact.png',dpi=180); plt.close(fig)
print(f'Max abs error at t={tv}: {np.max(np.abs(yp-ye)):.4e}')
