
    import pandas as pd
    from yahoofinancials import YahooFinancials
    import numpy as np
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    import numpy as np
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





    df = pd.read_csv('mpg.csv')
    df2 = pd.read_csv('2010YumaAZ.csv')
    df3 = pd.read_csv('2010SitkaAK.csv')
    features = df.columns

    stocks = pd.read_csv('Symbol.csv')

    stock_picker = []

    time = (str(dt.now()))
    today_year = time[0:4]
    today_day = time[5:7]
    today_month = time[8:10] 

    for Symbol in stocks['Symbol']:
    stock_picker.append({'label':str(Symbol), 'value': Symbol})


    app.layout = html.Div([
             
             html.H1('Python Driven BI Chart Samples',
                     style = {'font-family': 'Calibri',
                             'text-align': 'center',
                              'text-transform': 'uppercase'
                              }),
            html.H5('Comming Soon: Financial Statment Comparison Web Ap',
                    style = {'text-align': 'center',
                             'font-family': 'Calibri'}),
            html.H6('Nathaniel Gibson',
                    style = {'text-align': 'center',
                             'font-family': 'Calibri'
                              }),
             
             
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
             dcc.Graph(id='graph', figure ='children'),
             
             html.Div([
                 html.Div([
                         html.Div('X-Axis'),
                     dcc.Dropdown(id='xaxis',
                                  options=[{'label':i,'value':i} for i in features],
                                  value = 'mpg',)
                     ], style={'width':'20%', 'display':'inline-block'}),
                 html.Div([
                         html.Div('Y-Axis'),
                     dcc.Dropdown(id='yaxis',
                                  options=[{'label': i, 'value':i} for i in features],
                                  value = 'horsepower')
                     ], style={'width':'20%', 'display':'inline-block'}),
                 dcc.Graph(id='feature_graphic')
             
        
        ], style={'padding': 20}),
                     
        html.Div([html.H3('Arizona vs Alaska Tempature Matrix',
                     style = {'text-align': 'center',
                              'font-family': 'Calibri',
                              'text-transform': 'uppercase'
                              }),
                
                dcc.Graph(id='heatmap1',
                                 figure = {'data':[go.Heatmap(x=df3['DAY'],
                                                              y=df3['LST_TIME'],
                                                              z=df3['T_HR_AVG'].values.tolist(),
                                                              colorscale = 'Jet', 
                                                              zmin=5,
                                                              zmax=40)],
                                  'layout':go.Layout(title='(Sitka, Alaska) °C',
                                                     yaxis = dict(title = 'Time'),
                                                     xaxis = {'title': 'Day of the Week'},)
                                  }),
                       
                        dcc.Graph(id='heatmap2',
                                 figure = {'data':[go.Heatmap(x=df2['DAY'],
                                                              y=df2['LST_TIME'],
                                                              z=df2['T_HR_AVG'].values.tolist(),
                                                              colorscale = 'Jet', 
                                                              zmin=5,
                                                              zmax=40)],
                                  'layout':go.Layout(title='(Yuma,Arizona) °C',
                                                     yaxis = dict(title = 'Time'),
                                                     xaxis = {'title': 'Day of the Week'})})
    ])
             
                          
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
                'layout':go.Layout(title ='S&P 500 Closing Prices (Daily)',
                                   xaxis={'title':'Date'},
                                  yaxis=dict(title='Price'))}
            
                     
    @app.callback(Output('feature_graphic', 'figure'),
              [Input('xaxis','value'),
               Input ('yaxis','value')]) 

                   
    def update_graph(xaxis_name, yaxis_name):
    return{'data':[go.Scatter(x=df[xaxis_name], 
                              y=df[yaxis_name],
                              text=df['name'],
                              mode = 'markers',
                              marker={'size':15,
                                      'opacity':0.5,
                                      'line':{'width':0.5,'color':'white'}})],
            'layout':go.Layout(title = 'Car Relational Attribute Chart',
                               xaxis=dict(title = xaxis_name ),
                               yaxis=dict(title = yaxis_name ),
                               hovermode='closest')}
            
    if __name__=='__main__':
    app.run_server()
