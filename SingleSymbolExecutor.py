import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
def execute(symbol): 
    symbol=str(symbol)
    data = yf.Ticker(symbol).history(period="4y")
    data['diff'] = data['Close'].diff()
    data['gain'] = data['diff'].apply(lambda x: x if x > 0 else 0)
    data['loss'] = data['diff'].apply(lambda x: abs(x) if x < 0 else 0)
    data['avg_gain'] = data['gain'].rolling(14).mean()
    data['avg_loss'] = data['loss'].rolling(14).mean()
    data['rs'] = data['avg_gain'] / data['avg_loss']
    data['rsi'] = 100 - (100 / (1 + data['rs']))
    data['ma50'] = data['Close'].rolling(window=50).mean()
    data['ma200'] = data['Close'].rolling(window=200).mean()
    data = data.tail(365)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    a=float(data['ma50'].tail(1))
    b=float(data['ma200'].tail(1))
    diff=a-b
    plt.title(str(symbol)+' '+str(diff))
    ax1.plot(data['Close'], label='Close')
    ax1.plot(data['ma50'], label='50-day MA')
    ax1.plot(data['ma200'], label='200-day MA')
    ax1.legend()
    plt.xticks(rotation=15)
    plt.gcf().set_facecolor('gray')
    ax2.plot(data['rsi'], label='RSI')
    plt.axhline(y=30, color='green')
    plt.axhline(y=70, color='red')
    ax1.grid()
    ax2.grid()
    plt.savefig('C:\\Charts\\'+symbol+'.png')
    plt.cla()
    plt.close()
    return('C:\\Charts\\'+symbol+'.png')
    Path=('C:\\Charts\\'+symbol+'.png')
    os.remove(Path)
execute('AAPL')