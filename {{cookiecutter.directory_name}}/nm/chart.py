import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def waterfall(x: list, y: list) -> plt:

    data_tuples = list(zip(x, y))
    df = pd.DataFrame(data_tuples, columns= ['x', 'y'])

    # calculate running totals
    df['tot'] = df['y'].cumsum()
    df['tot1']=df['tot'].shift(1).fillna(0)

    # lower and upper points for the bar charts
    lower = df[['tot','tot1']].min(axis=1)
    upper = df[['tot','tot1']].max(axis=1)

    # mid-point for label position
    mid = (lower + upper)/2

    # positive number shows green, negative number shows red
    df.loc[df['y'] >= 0, 'color'] = 'green'
    df.loc[df['y'] < 0, 'color'] = 'red'

    # calculate connection points
    connect= df['tot1'].repeat(3).shift(-1)
    connect.iloc[1::3] = np.nan

    fig,ax = plt.subplots()

    # plot first bar with colors
    bars = ax.bar(x=df['x'],height=upper, color =df['color'])

    # plot second bar - invisible
    plt.bar(x=df['x'], height=lower,color='white')

    # plot connectors
    plt.plot(connect.index,connect.values, 'k' )

    # plot bar labels
    for i, v in enumerate(upper):
        plt.text(i-.15, mid[i], f"{df['y'][i]:,.0f}")

    plt.xticks(rotation=90)