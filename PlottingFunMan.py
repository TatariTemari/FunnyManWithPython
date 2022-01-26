# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:15:10 2022

@author: Dr. Robel Tilaye Geressu
robtilaye@gmail.com
for www.tilaye.com
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy.random import random
from shapely.geometry import Polygon
from numpy.random import random
import pandas as pd
import imageio
import matplotlib.patches as ptc
import time

from matplotlib import font_manager as fm
fprop = fm.FontProperties(fname='nyala.ttf')

coords  = ((-1, 0), (-1, 1), (0, 0.5), (1, 1), (1, 0), (-1, 0))
polygon = Polygon(coords)
polygon.area



if __name__ == "__main__":
    # connections = {0:0,1:0,2:1,9:1,11:9,13:11,3:2,4:2,5:3,6:4,7:5,8:6,10:1,12:10,14:12}
    connections = {0:0,1:0,2:1,3:1,4:2,6:4,5:3,7:5,8:1,9:8,10:8,11:9,12:10,13:11,14:12}
    rdic = {'0:0':0,'1:0':0.1,'2:1':0.1,'3:1':0.1,'4:2':0.5,'6:4':0.5,'5:3':0.5,'7:5':0.5,'8:1':1,'9:8':0.6,'10:8':0.6,'11:9':0.5,'12:10':0.5,'13:11':0.1,'14:12':0.1} 
    # tdic  = {'0:0':0.5,'1:0':0.5,'2:1':1,'3:1':0,'4:2':0.5,'6:4':1.25,'5:3':0.5,'7:5':0.75,'8:1':0.5,'9:8':0.75,'10:8':0.45,'11:9':0.55,'12:10':0.5,'13:11':1,'14:12':1}
    # tdic  = {'0:0':[0.5,0.0],'1:0':[0.5,0.0],'2:1':[1,0.0],'3:1':[0,0.1],
    #          '4:2':[0.5,0.6],'6:4':[1.25,1.3],'5:3':[0.5,0.6],'7:5':[0.75,0.8],
    #          '8:1':[0.5,0.1],'9:8':[0.75,0.1],'10:8':[0.45,0.1],'11:9':[0.55,0.5],'12:10':[0.5,0.5],'13:11':[1,1],'14:12':[1,0.9]}

    tdic  = {'0:0':[0.5,0.0],'1:0':[0.5,0.0],'2:1':[1,0.0],'3:1':[0,0.1],
             '4:2':[0.5,0.2],'6:4':[1.25,0.3],'5:3':[0.5,0.2],'7:5':[0.75,0.2],
             '8:1':[0.5,0.1],'9:8':[0.75,0.1],'10:8':[0.45,-0.4],'11:9':[0.55,0.2],'12:10':[0.5,-0.2],'13:11':[1,1],'14:12':[-1,-0.9]}

    # ab = pd.DataFrame(connections,index = [0])
    colors = {0:'r',1:'g',2:'b',3:'k',
              4:'m',5:'c',6:'y',7:'grey',
              8:'orange',9:'salmon',10:'limegreen',
              11:'gold',12:'darkgrey',13:'y',14:'m'}

    lengthOfMovie = 70
    for k in range(lengthOfMovie):
        # time.sleep(2)
        loc = {}
        loc[0] = [0,0]
        fig,ax= plt.subplots(figsize = (5,5))
        tdic = {pp:jj  for pp,jj in tdic.items() }
        for i,j in connections.items():
                
            x0,x1 = loc[j][0],loc[j][0]+ rdic[str(i)+':'+str(j)]*np.cos(np.pi*(tdic[str(i)+':'+str(j)][0] - tdic[str(i)+':'+str(j)][1]*k/lengthOfMovie))
            y0,y1 = loc[j][1],loc[j][1]+ rdic[str(i)+':'+str(j)]*np.sin(np.pi*(tdic[str(i)+':'+str(j)][0]- tdic[str(i)+':'+str(j)][1]*k/lengthOfMovie))

            circle1 = plt.Circle((loc[0][0], loc[0][1] + 0.05), 0.1, color='grey')
            ax.add_patch(circle1)
            circle2 = ptc.Ellipse((loc[0][0], loc[0][1] + 0.05), 0.2,0.2, color='grey')
            ax.add_patch(circle2)
            
            
            loc[i] = [x1,y1]
            ax .plot([x0,x1],[-y0,-y1],color = colors[i])
            if i > 2:
                ax .text((x0+x1)/2,-(y0+y1)/2,str(i),fontsize = 14) 
            # circle1 = plt.Circle((k*0.2-5, -2), 0.1, color='grey')
            # ax.add_patch(circle1)
            
            # circle1 = plt.Rectangle((k*0.2-3, -2), 0.2,0.1, color='grey')
            # ax.add_patch(circle1)
        
        ax.set_xticklabels('')
        plt.xlim([-2,1])
        plt.xlim([-1.5,0.5])
        # plt.title('ቡና ያልጠጣ ጎበዝ የሂሳብ ተማሪ ፡ ተከስተ',fontproperties=fprop)
        plt.title('ጀማሪ ኮማንዶ  ፥ ተከስተ',fontproperties=fprop)
        # plt.text(-loc[11][0],-loc[11][1],'www.tilaye.com')
        plt.xlabel('get the code for your kids @ www.tilaye.com let them learn and build on it')
        # plt.xlabel('www.tilaye.com')
        fig.savefig(str(k)+'.png')
    # Build GIF
    with imageio.get_writer('funnyMan.gif', mode='I') as writer:
        for filename in [str(k)+'.png' for k in range(20)]:
            image = imageio.imread(filename)
            writer.append_data(image)
