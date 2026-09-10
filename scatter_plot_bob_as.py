# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 15:19:56 2026

@author: user
"""

import gsw
import xarray as xr

data1 = "C:/Users/user/Desktop/25CL05014-NMD/lab2_12jan/ORAS5_1deg_SST_1990_2008.nc"
ds_sst = xr.open_dataset(data1)
print(ds_sst)


data2 = "C:/Users/user/Desktop/25CL05014-NMD/lab2_12jan/ORAS5_1deg_SSS_1990_2008.nc"
ds_sss = xr.open_dataset(data2)
print(ds_sss)
'''
[SA,in_ocean] = gsw.SA_from_SP(['SOSALINE'],p,ds_sst['LONN179_181'],ds_sst['LAT'])
'''
ds_sst.data_vars

SST = ds_sst['SOSSTSST']
SSS = ds_sss['SOSALINE']
lon = ds_sst['LONN179_181']
lat = ds_sst['LAT']
time = ds_sst['TIME']
p = [0]
AR_SST = SST.sel(LAT = slice(8,27),LONN179_181 = slice(50,75))
AR_SST.values

AR_SSS = SSS.sel(LAT = slice(8,27),LONN179_181 = slice(50,75))
AR_SSS.values

BOB_SST = SST.sel(LAT = slice(4,24),LONN179_181 = slice(76,100))
BOB_SST.values

BOB_SSS = SSS.sel(LAT = slice(4,24),LONN179_181 = slice(76,100))
BOB_SSS.values

SA_AR = gsw.SA_from_SP(AR_SSS,p,ds_sst['LONN179_181'],ds_sst['LAT'])
SA_BOB = gsw.SA_from_SP(BOB_SSS,p,ds_sst['LONN179_181'],ds_sst['LAT'])

CT_AR = gsw.CT_from_pt(SA_AR,AR_SST)
CT_BOB = gsw.CT_from_pt(SA_BOB,BOB_SST)

sigma0_AR = gsw.sigma0(SA_AR,CT_AR)
sigma0_BOB = gsw.sigma0(SA_BOB,CT_BOB)


'''
Q2
'''

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize = (18,12))
plt.suptitle("Scatter plot of T-S diagram over Arabian sea and Bay of Bengal",fontsize = 24)

plt.subplot(2,1,1)
plt.scatter(AR_SSS,AR_SST)
plt.title('T-S plot over Arabian sea',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g = np.linspace(np.nanmin(SA_AR),np.nanmax(SA_AR),60)
CT_g = np.linspace(np.nanmin(CT_AR),np.nanmax(CT_AR),60)
SA_grid,CT_grid = np.meshgrid(SA_g,CT_g)
sigma_grid = gsw.sigma0(SA_grid,CT_grid)
cs = plt.contour(SA_grid,CT_grid,sigma_grid,colors = "k")
plt.clabel(cs,fontsize = 10)


plt.subplot(2,1,2)
plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S Plot over Bay of Bengal',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g1 = np.linspace(np.nanmin(SA_BOB),np.nanmax(SA_BOB),60)
CT_g1 = np.linspace(np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid2,CT_grid2 = np.meshgrid(SA_g1,CT_g1)
sigma_grid2 = gsw.sigma0(SA_grid2,CT_grid2)
cs1 = plt.contour(SA_grid2,CT_grid2,sigma_grid2,colors = "k")
plt.clabel(cs1,fontsize = 10)



'''
Q3 - 
'''
F1 = gsw.CT_freezing_poly(SA_AR,p,1)
F2 = gsw.CT_freezing_poly(SA_BOB,p,1)

plt.figure(figsize = (18,12))
plt.suptitle("Scatter plot of T-S diagram over Arabian sea and Bay of Bengal",fontsize = 24)

plt.subplot(2,1,1)
plt.scatter(AR_SSS,AR_SST)
plt.title('T-S plot over Arabian sea',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g = np.linspace(np.nanmin(SA_AR),np.nanmax(SA_AR),60)
CT_g = np.linspace(-np.nanmin(CT_AR),np.nanmax(CT_AR),60)
SA_grid,CT_grid = np.meshgrid(SA_g,CT_g)
sigma_grid = gsw.sigma0(SA_grid,CT_grid)
cs = plt.contour(SA_grid,CT_grid,sigma_grid,10,colors = "k")
plt.clabel(cs,fontsize = 10)

SA_g2 = np.linspace(np.nanmin(SA_AR),np.nanmax(SA_AR),60)
CT_1 = gsw.CT_freezing_poly(SA_g2,p,1)
MX_1 = gsw.CT_maxdensity(SA_g2,p)
plt.plot(SA_g2,CT_1,'r--',label= 'Freezing CT')
plt.plot(SA_g2,MX_1,'g--',label= 'Temprature of max density')
plt.legend()
plt.tight_layout()

plt.subplot(2,1,2)
plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S Plot over Bay of Bengal',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g1 = np.linspace(np.nanmin(SA_BOB),np.nanmax(SA_BOB),60)
CT_g1 = np.linspace(-np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid2,CT_grid2 = np.meshgrid(SA_g1,CT_g1)
sigma_grid2 = gsw.sigma0(SA_grid2,CT_grid2)
cs1 = plt.contour(SA_grid2,CT_grid2,sigma_grid2,10,colors = "k")
plt.clabel(cs1,fontsize = 10)

SA_g1 = np.linspace(np.nanmin(SA_BOB),np.nanmax(SA_BOB),60)
CT_2 = gsw.CT_freezing_poly(SA_g1,p,1)
MX_2 = gsw.CT_maxdensity(SA_g1,p)
plt.plot(SA_g1,CT_2,'r--',label= 'Freezing CT')
plt.plot(SA_g1,MX_2,'g--',label= 'Temprature of max density')
plt.legend()
plt.tight_layout()


'''
Q4
'''
import cartopy.crs as cc
import cartopy.feature as cf

SA_1 = gsw.SA_from_SP(SSS,p,ds_sst['LONN179_181'],ds_sst['LAT'])
CT_1 = gsw.CT_from_pt(SA_1,SST)
sigma0_1 = gsw.sigma0(SA_1,CT_1)
TE = gsw.alpha(SA_1,CT_1,p)

sp = TE.mean(dim = 'TIME')
'''
c=sp.plot(add_labels=False)
plt.cmbar(c)
'''
plt.figure(figsize = (18,12))
ax = plt.axes(projection = cc.Mercator())
ax.gridlines(draw_labels = True)
ax.add_feature(cf.COASTLINE)
cp = sp.plot.contourf(transform = cc.PlateCarree(),cmap = 'hot_r',add_colorbar = False,levels = 20,)
ax.add_feature(cf.LAND,color="gray")
plt.title("Thermal expansion coefficient around globe")
plt.colorbar(cp,label = "$^\circ$C$^-1$")
plt.xlabel('Longitude')
plt.ylabel('Latitude')

'''
Q5
'''

'''
P = [10000]
SA_BOB_2 = gsw.SA_from_SP(BOB_SSS,P,ds_sst['LONN179_181'],ds_sst['LAT'])
CT_BOB_2 = gsw.CT_from_pt(SA_BOB_2,BOB_SST)
sigma0_1 = gsw.sigma0(SA_BOB_2,CT_BOB_2)

plt.figure(figsize = (18,12))
plt.suptitle("Scatter plot of T-S diagram over BAY OF BENGAL at surface and 500m depth",fontsize = 24)

plt.subplot(2,1,1)
plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S plot over Bay of Bengal at surface',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g = np.linspace(np.nanmin(SA_BOB),np.nanmax(SA_BOB),60)
CT_g = np.linspace(np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid,CT_grid = np.meshgrid(SA_g,CT_g)
sigma_grid = gsw.sigma0(SA_grid,CT_grid)
cs = plt.contour(SA_grid,CT_grid,sigma_grid,colors = "k")
plt.clabel(cs,fontsize = 10)


plt.subplot(2,1,2)
plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S Plot over Bay of Bengal at 500m depth',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

SA_g1 = np.linspace(np.nanmin(SA_BOB_2),np.nanmax(SA_BOB_2),60)
CT_g1 = np.linspace(np.nanmin(CT_BOB_2),np.nanmax(CT_BOB_2),60)
SA_grid2,CT_grid2 = np.meshgrid(SA_g1,CT_g1)
sigma_grid2 = gsw.sigma0(SA_grid2,CT_grid2)
cs1 = plt.contour(SA_grid2,CT_grid2,sigma_grid2,colors = "k")
plt.clabel(cs1,fontsize = 10)
'''

P = [5000]
SA_BOB_2 = gsw.SA_from_SP(BOB_SSS,P,ds_sst['LONN179_181'],ds_sst['LAT'])
CT_BOB_2 = gsw.CT_from_pt(SA_BOB_2,BOB_SST)
sigma0_1 = gsw.sigma0(SA_BOB_2,CT_BOB_2)



SA_g = np.linspace(np.nanmin(SA_BOB),np.nanmax(SA_BOB),60)
CT_g = np.linspace(np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid,CT_grid = np.meshgrid(SA_g,CT_g)
sigma_grid = gsw.sigma0(SA_grid,CT_grid)
cs = plt.contour(SA_grid,CT_grid,sigma_grid,colors = "Green")
plt.clabel(cs,fontsize = 10)

SA_g1 = np.linspace(np.nanmin(SA_BOB_2),np.nanmax(SA_BOB_2),60)
CT_g1 = np.linspace(np.nanmin(CT_BOB_2),np.nanmax(CT_BOB_2),60)
SA_grid2,CT_grid2 = np.meshgrid(SA_g1,CT_g1)
sigma_grid2 = gsw.sigma0(SA_grid2,CT_grid2)
cs1 = plt.contour(SA_grid2,CT_grid2,sigma_grid2,colors = "Red")
plt.clabel(cs1,fontsize = 10)

plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S plot over Bay of Bengal at surface',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)

'''
plt.scatter(BOB_SSS,BOB_SST)
plt.title('T-S Plot over Bay of Bengal at 500m depth',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)
'''
SA_g1 = np.linspace(np.nanmin(SA_BOB_2),np.nanmax(SA_BOB_2),60)
CT_g1 = np.linspace(np.nanmin(CT_BOB_2),np.nanmax(CT_BOB_2),60)
SA_grid2,CT_grid2 = np.meshgrid(SA_g1,CT_g1)
sigma_grid2 = gsw.sigma0(SA_grid2,CT_grid2)
cs1 = plt.contour(SA_grid2,CT_grid2,sigma_grid2,colors = "k")
plt.clabel(cs1,fontsize = 10)

