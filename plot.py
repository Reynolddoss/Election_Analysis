import numpy as np
import matplotlib.pyplot as plt

#extracting results from file 
text=open("result.txt","r")
lines=text.readlines()
#for bjp
bjp_pos=lines[0]
bjp_neg=lines[1]
bjp_neu=lines[2]
#for sp+cong
spcong_pos=lines[3]
spcong_neg=lines[4]
spcong_neu=lines[5]
#for bsp
bsp_pos=lines[6]
bsp_neg=lines[7]
bsp_neu=lines[8]
#for others
others_pos=lines[9]
others_neg=lines[10]
others_neu=lines[11]





N = 4



positive= (bjp_pos,spcong_pos,bsp_pos,others_pos)
negative =(bjp_neg,spcong_neg,bsp_neg,others_neg)
neutral=(bjp_neu,spcong_neu,bsp_neu,others_neu)
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind,positive, width, color='green')

rects2 = ax.bar(ind + width,negative, width, color='red')

rects3=ax.bar(ind+width+width,neutral,width,color='yellow')

# add some text for labels, title and axes ticks
ax.set_ylabel('Percentage')
ax.set_title('Sentimental analysis of UP election 2017')
ax.set_xticks(ind + width / 3)
ax.set_xticklabels(('BJP', 'SP+CONG', 'BSP', 'OTHERS'))

ax.legend((rects1[0], rects2[0],rects3[0]), ('Positive', 'Negative','Neutral'))


def autolabel(rects):
    """
   Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/3., 1.00001*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
