import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# FILE INPUT & OUTPUT

INPUT_FILE = 'CASE STUDY 1.csv'
SAVED_FILE = 'CS1.png'
GRAPH_TITLE = 'Case Study 1: July Rainfall Event during Dry Conditions'

# VISUAL PARAMETERS

LINEWIDTH = 2
BARWIDTH = 0.025
FONTSIZE = 14

Y_LIM_PRECIP = [0,18]
Y_LIM_WL = [0.45,0.68]
Y_LIM_SC = [170,200]

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

x = mdates.date2num(df['Date'])

y2a = df['Wolf Creek Water Level (m)']
y3a = df['Wolf Creek Specific Conductance (um/cm)']
y4 = df['San Juan Station Rainfall (mm)']

plt.rcParams['figure.figsize'] = [14,8]
plt.rcParams["font.family"] = "Times New Roman"
fig, ax1 = plt.subplots()

ax1.set_xlabel('Date', fontsize=FONTSIZE)
ax1.set_ylabel('Precipitation (mm)', fontsize=FONTSIZE)
ax1.tick_params(labelsize=FONTSIZE)
ax1.set_ylim(Y_LIM_PRECIP)
ax1.xaxis.set_major_locator(mdates.DayLocator())

#set major ticks format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%h %d'))

ax1.bar(x, y4, color=PRECIP_COLOUR_2, width=BARWIDTH,edgecolor='white', label='San Juan Station Rainfall (mm)')
ax1.set_ylabel('Precipitation (mm)', color=PRECIP_COLOUR_3, fontsize=FONTSIZE)

ax2 = ax1.twinx()
ax2.set_ylabel('Water Level (m)', color=WL_COLOUR_WOLF, fontsize=FONTSIZE)
ax2.tick_params(labelsize=FONTSIZE)
ax2.set_ylim(Y_LIM_WL)
lns2 = ax2.plot(x, y2a, color=WL_COLOUR_WOLF, linewidth=LINEWIDTH, label='Wolf Creek Water Level (m)')

ax2.grid()

# make Stream cave lines dotted
ax3 = ax1.twinx()
lns3 = ax3.plot(x, y3a, color=SC_COLOUR_WOLF, linewidth=LINEWIDTH, label='Wolf Creek Specific Conductance (μm/cm)')
ax3.spines['right'].set_position(('outward', 55))
ax3.tick_params(labelsize=FONTSIZE)
ax3.set_ylabel('Specific Conductance (μm/cm)', color=SC_COLOUR_WOLF, fontsize=FONTSIZE)
ax3.set_ylim(Y_LIM_SC)

# legend combining
lns = lns2+lns3
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=0, fontsize=FONTSIZE)
ax1.legend(loc=2, fontsize=FONTSIZE)

plt.title(GRAPH_TITLE, fontsize=24)
plt.savefig(SAVED_FILE)
plt.show()
