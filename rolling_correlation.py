import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

start_date = ["2018-1-1", "2019-1-1", "2020-1-1", "2021-1-1"]
end_date = ["2018-12-31", "2019-12-31", "2020-12-31", "2021-12-31"]

stocks = ["SPY", "QQQ"]
cryptos = ["BTC-USD", "ETH-USD"]
for crypto in cryptos:
    for year in range(len(start_date)):
        for stock in stocks:
            data1 = yf.download(crypto, start=start_date[year], end=end_date[year], interval = "1d")
            data2 = yf.download(stock, start=start_date[year], end=end_date[year], interval = "1d")

            stock_count = 0
            drop = []
            for btc_count in range(len(data1.index) - 1):
                if data1.index[btc_count] == data2.index[stock_count]:
                    stock_count += 1

                else:
                    drop.append(data1.index[btc_count])

                if stock_count == len(data2.index):
                    break

            data1_ = data1.drop(drop, axis=0)
            data1_new = data1_["Close"]
            data2_new = data2["Close"]

            s1 = pd.Series(data1_new)
            s2 = pd.Series(data2_new)
            corr = s1.rolling(30).corr(s2)


            fig = go.Figure()

            fig.add_trace(
                go.Scatter(x=data1_new.index, y=corr, name="Correlation Coefficient")
            )

            fig.add_trace(go.Candlestick(x=data1_.index,
                            open=data1_['Open'], high=data1_['High'],
                            low=data1_['Low'], close=data1_['Close'], name="BTC Price", yaxis="y2", opacity=.5, increasing_line_color= 'green', decreasing_line_color= 'green')
            )

            fig.add_trace(go.Candlestick(x=data2.index,
                            open=data2['Open'], high=data2['High'],
                            low=data2['Low'], close=data2['Close'], name=stock + " Price", yaxis="y3", opacity=.5, increasing_line_color= 'red', decreasing_line_color= 'red')
            )

            # Create axis objects
            fig.update_layout(
                xaxis=dict(
                    domain=[0, 0.9],
                    tickfont=dict(
                        color="lightblue"
                    )),
                yaxis=dict(
                    title="Correlation Coefficient",
                    titlefont=dict(
                        color="lightblue",
                        size=16
                    ),
                    tickfont=dict(
                        color="lightblue"
                    )
                ),
                yaxis2=dict(
                    title=str(crypto) + " Price",
                    titlefont=dict(
                        color="red"
                    ),
                    tickfont=dict(
                        color="red",
                        size= 16
                    ),
                    anchor="x",
                    overlaying="y",
                    side="right",
                ),
                yaxis3=dict(
                    title=str(stock) + " Price",
                    titlefont=dict(
                        color="green"
                    ),
                    tickfont=dict(
                        color="green",
                        size= 16
                    ),
                    anchor="free",
                    overlaying="y",
                    side="right",
                    position=.98
                ),
                legend=dict(bgcolor="white",
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="left",
                    x=0
                ),
                paper_bgcolor = "#180c0c",
                plot_bgcolor = "white"
            )

            fig.update_layout(xaxis_rangeslider_visible=False)

            fig.write_image(str(crypto) + "vs. " + str(stock) + "-" + str(start_date[year]) + ".png", width=1.5*800, height=0.75*800, scale=3)
