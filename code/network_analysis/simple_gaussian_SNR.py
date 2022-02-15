import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})
#%%
nt = 1000
nplot = min(nt,2000)

s_x = .5
s_y = 5
s_u = 1

w_ux = 2
w_uy = 2


def g(nt=nt):
    return np.random.randn(nt,)
def gu(nt=nt):
    p = 10
    t = np.arange(0,nt)
    #random square wave:
    wave = np.mod(np.cumsum(np.random.rand(nt)<.1),2)+g(nt)/10
    #gaussian noise:
    # wave = g(nt)
    #saw-tooth:
    # wave = np.mod(range(0,nt),p)/p
    #sine:
    # wave = np.sin(t/p)
    wave = (wave-np.mean(wave))/np.std(wave)
    return wave.T
def cov(a,b):
    COV = np.cov(a.T,b.T)
    return COV[0,1]
def corr(a,b):
    CORR = np.corrcoef(a.T,b.T)
    return CORR[0,1]
def pythag(a,b):
    return np.sqrt(a**2+b**2)
#%% markdown
y←u→x

#%%
def sim_dag(w_ux=w_ux, w_uy=w_uy, S=[s_u,s_x,s_y], g=g):
    [s_u,s_x,s_y]=S
    u = gu()*s_u
    x = g()*s_x + w_ux*u
    y = g()*s_y + w_uy*u
    return {'u':u,'x':x,'y':y}

#%%
gu().shape
g().shape
res = sim_dag()
u,x,y=res.values() #bad!
u.shape
x.shape


#%%
#%%
er_xy = corr(x,y)

pcov_xy = (w_ux*s_u)*(w_uy*s_u)
cov_str = f' cov {cov(x,y):.2f}, pred {pcov_xy:.2f}'

pso_x = pythag(s_x, w_ux*s_u)
pso_y = pythag(s_y, w_uy*s_u)
pr_xy = pcov_xy / (pso_x * pso_y)
r2_str = f' r^2 {er_xy:.2f}, pred {pr_xy:.2f}'

psnr_xy = pcov_xy / (s_x * s_y)
esnr_xy = cov(x,y)/ (np.std(x-w_ux*u) * np.std(y-w_uy*u))
snr_str = f' SNR* {esnr_xy:.2f}, pred {psnr_xy:.2f}'

#%%
fig,ax = plt.subplots(1,3,figsize=(12,5),sharey=True,sharex=False)
ax[0].plot(u[:nplot],x[:nplot],'k.',markersize=1)
ax[1].plot(u[:nplot],y[:nplot],'k.',markersize=1)
ax[2].plot(x[:nplot],y[:nplot],'k.',markersize=1)
# ax.plot(x[:,:nplot],g(nplot),'b.',markersize=.5)

# ax[1].set
# [_ax.axis('equal') for _ax in ax]
ax[0].set_xlabel('u')
ax[1].set_xlabel('u')
ax[2].set_xlabel('x')


ax[0].set_ylabel('x')
ax[1].set_ylabel('y')
ax[2].set_ylabel('y')
ax[1].set_title('x ← u → y')
ax[2].set_title(f'{cov_str}\n{r2_str}\n{snr_str}')
#%%

#%%
fig,ax = plt.subplots(3,1,figsize=(10,3))
ax[0].plot(u);
ax[0].set_ylabel('u');
ax[1].plot(x);
ax[1].set_ylabel('x');
ax[2].plot(y);
ax[2].set_ylabel('y');
#%%
def xcorr(x,y):
    xc=np.correlate(x/np.std(x),y/np.std(y),mode='same')
    return xc/len(xc)
xx_xcorr = xcorr(x,x)
xy_xcorr = xcorr(x,y)
yy_xcorr = xcorr(y,y)

fig,ax= plt.subplots()
# ax.plot(xx_xcorr-1,'k');
# ax.plot(yy_xcorr-1,color='grey');
ax.plot(xy_xcorr,'k');


noise_std = np.std(xy_xcorr[nt//2+1:])
ax.plot(nt//2, pr_xy,'rx')
ax.plot([0,nt], [noise_std,noise_std],'b--')
ax.plot([0,nt], [-noise_std,-noise_std],'b--')

xy_xcorr[nt//2]

esnr_xcorr_xy = xy_xcorr[nt//2]/noise_std
print(xy_xcorr[nt//2]) # should be R2
print(np.std(xy_xcorr[nt//2+1:])) # has to do with autocorr!
print(np.std(xx_xcorr[nt//2+1:])) # has to do with autocorr!
print(np.std(yy_xcorr[nt//2+1:])) # has to do with autocorr!
print(esnr_xcorr_xy) # what we're measuring for analysis later

# peaksnr_xy = 2*xy_xcorr[nt//2] / (xx_xcorr[nt//2]+yy_xcorr[nt//2])
# print(peaksnr_xy)




#%%

#%%
 #= w_ux
# cov(x,y) #= w_ux * w_uy



#%%