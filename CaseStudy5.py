import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# FILE INPUT & OUTPUT

INPUT_FILE = 'CASE STUDY 5.csv'
SAVED_FILE = 'CS5-fixed.png'
GRAPH_TITLE = 'Case Study 5: Similar December 2023 Precipitation Events (Xmm/24hrs), Different Responses'
FIG_SIZE = [17.5,10]

# VISUAL PARAMETERS

LINEWIDTH = 1.5
BARWIDTH = 0.03

Y_LIM_PRECIP = [0,18]
Y_LIM_WL = [0.20,1.5]
Y_LIM_SC = [80,230]

LABEL_FONTSIZE = 15

SC_COLOUR_WOLF = '#9900ff'
SC_COLOUR_STREAM = '#b4a7d6'

WL_COLOUR_WOLF = '#38761d'
WL_COLOUR_STREAM = '#b6d7a8'

PRECIP_COLOUR_1 = '#e5e5ff'
PRECIP_COLOUR_2 = '#9999ff'
PRECIP_COLOUR_3 = '#4c4cff'




# CODE

df = pd.read_csv(INPUT_FILE)

df['Date'] = pd.to_datetime(df['Date'])
df = df[(df['Date']) > '2023-12-13 13:00:00']

x = mdates.date2num(df['Date'])
y1 = df['Mesachie II Station Rainfall (mm)']
y2a = df['Wolf Creek Water Level (m)']
y2b = df['Stream Cave Water Level (m)']
y3a = df['Wolf Creek Specific Conductance (um/cm)']
y3b = df['Stream Cave Specific Conductance (um/cm)']
y4 = df['San Juan Station Rainfall (mm)']
y5 = df['Summit Station Rainfall (mm)']

plt.rcParams['figure.figsize'] = FIG_SIZE
fig, ax1 = plt.subplots()


ax1.set_xlabel('Date')
ax1.set_ylabel('Precipitation (mm)')
ax1.set_ylim(Y_LIM_PRECIP)
ax1.xaxis.set_major_locator(mdates.DayLocator())


# set major ticks format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%h %d'))

ax1.bar(x, y1, color=PRECIP_COLOUR_1, width=BARWIDTH,edgecolor='white', label='Mesachie II Station Rainfall (mm)')
ax1.bar(x+BARWIDTH, y4, color=PRECIP_COLOUR_2, width=BARWIDTH, edgecolor='white', label='San Juan Station Rainfall (mm)')
ax1.bar(x-BARWIDTH, y5, color=PRECIP_COLOUR_3, width=BARWIDTH, edgecolor='white', label='Summit Station Rainfall (mm)')
ax1.set_ylabel('Precipitation (mm)', color=PRECIP_COLOUR_3, fontsize=LABEL_FONTSIZE)


ax2 = ax1.twinx()
ax2.set_ylabel('Water Level (m)', color=WL_COLOUR_WOLF, fontsize=LABEL_FONTSIZE)
ax2.set_ylim(Y_LIM_WL)
lns3 = ax2.plot(x, y2a, color=WL_COLOUR_WOLF, linewidth=LINEWIDTH, label='Wolf Creek Water Level (m)')
lns1 = ax2.plot(x, y2b, color=WL_COLOUR_STREAM, linestyle='dashed', linewidth=LINEWIDTH,label='Stream Cave Water Level (m)')
ax2.grid()


ax3 = ax1.twinx()
lns4 = ax3.plot(x, y3a, color=SC_COLOUR_WOLF, linewidth=LINEWIDTH, label='Wolf Creek Specific Conductance (μm/cm)')
lns2 = ax3.plot(x, y3b, color=SC_COLOUR_STREAM, linestyle='dashed', linewidth=LINEWIDTH, label='Stream Cave Specific Conductance (μm/cm)')
ax3.spines['right'].set_position(('outward', 50))
ax3.set_ylabel('Specific Conductance (μm/cm)', color=SC_COLOUR_WOLF, fontsize=LABEL_FONTSIZE)
ax3.set_ylim(Y_LIM_SC)

# legend combining
lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=0)
ax1.legend()


plt.title(GRAPH_TITLE)
plt.savefig(SAVED_FILE)
plt.show()
