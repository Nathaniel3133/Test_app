# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:30:15 2019

@author: natha
"""

"""
Created on Mon Mar  4 20:15:49 2019

@author: natha
"""
import pandas as pd
from yahoofinancials import YahooFinancials
import numpy as np
pd.set_option('display.float_format', lambda x: '%.0f' % x)
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.dependencies import State
import base64
import json
import dash_table
from datetime import datetime as dt
import dash_auth



#yahoo_financials = YahooFinancials(ticker)

app= dash.Dash()
server = app.server


stocks = ['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 
                'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 
                'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 
                'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'APTV',
                'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BDX', 'BEN',
                'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BKNG', 'BLK', 'BLL', 'BMY', 'BR', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CAG', 'CAH',
                'CAT', 'CB', 'CBOE', 'CBRE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CE', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR',
                'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COO', 'COP', 'COST', 'COTY',
                'CPB', 'CPRI', 'CPRT', 'CRM', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 
                'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLR', 'DLTR', 'DOV', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 
                'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'ES', 
                'ESS', 'ETFC', 'ETN', 'ETR', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV',
                'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FTI', 'FTNT', 'FTV', 
                'GD', 'GE', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS',
                'HBAN', 'HBI', 'HCA', 'HCP', 'HD', 'HES', 'HFC', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 
                'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IPGP', 
                'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JEF', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'JWN', 
                'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH',
                'LIN', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUV', 'LW', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAR', 
                'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 
                'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MXIM', 'MYL', 'NBL', 
                'NCLH', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NKTR', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 
                'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY',
                'PAYX', 'PBCT', 'PCAR', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI',
                'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PXD', 
                'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 
                'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 
                'SLG', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC',
                'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TFX', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TPR', 'TRIP', 'TROW', 
                'TRV', 'TSCO', 'TSN', 'TSS', 'TTWO', 'TWTR', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 
                'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 
                'WBA', 'WCG', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYNN', 
                'XEC', 'XEL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']

stock_picker = []

time = (str(dt.now()))
today_year = time[0:4]
today_day = time[5:7]
today_month = time[8:10] 

for Symbol in stocks:
    stock_picker.append({'label':str(Symbol), 'value': Symbol})


app.layout = html.Div([
             dcc.Dropdown(id='stock_symbol', 
                          options= stock_picker,
                          multi = True,
                          value = ['AAPL'],
                          style={'width':'60%'}),
                          
            dcc.DatePickerRange(id = 'date_picker',
                                 min_date_allowed=dt(2015, 1, 1),
                                 max_date_allowed=dt(int(today_year),int(today_day),int(today_month)),
                                 start_date= dt(int(today_year)-1,int(today_day),int(today_month)),
                                 end_date=dt(int(today_year),int(today_day),int(today_month))),
             html.Button(
                        id='Submit_button',
                        children ='Submit',
                        n_clicks = 0,
                        style={'fontSize':15,
                                'background-color': '#4CAF50',
                                'border': 'none',
                                'color': 'white',
                                'padding': '12px',
                                'text-align': 'center',
                                'vertical-align': 'middle',
                                'text-decoration': 'none',
                                'display': 'inline-block',
                                'font-size': '16px',
                                'border-radius': '12px'}
                            ),
             dcc.Graph(id='graph', figure ='children')
             
                          
        ])
    




@app.callback(Output('graph','figure'),
              [Input('Submit_button','n_clicks')],
              [State('stock_symbol','value'),
               State('date_picker', 'start_date'),
               State('date_picker', 'end_date')])



def update_figure(n_clicks, selected_ticker, start_date, end_date):
    trace1 = []
    
    
    for i in selected_ticker:
        yahoo_financials = YahooFinancials(i)
        stock_price_data = yahoo_financials.get_historical_price_data(start_date, end_date, 'daily')
        df = pd.DataFrame(stock_price_data[i]['prices'][0:])
        df = df[['close','formatted_date']]
        
        
        trace1.append(go.Scatter(x=df['formatted_date'],y=df['close'],
                   mode='lines',name='{}'.format(i)))
    
        
    return {'data': trace1, 
                'layout':go.Layout(title ='S&P 500 Stock Trends',
                                   xaxis={'title':'Date'},
                                  yaxis=dict(title='Price'))}
      
    

if __name__=='__main__':
    app.run_server()














