
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





    app= dash.Dash()
    server = app.server


    stocks = []

    stock_picker = []

    time = (str(dt.now()))
    today_year = time[0:4]
    today_day = time[5:7]
    today_month = time[8:10] 

    for Symbol in stocks['Symbol']:
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
