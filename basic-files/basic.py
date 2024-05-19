import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = { 'background' : '#111111', 'text':'#7FDBFF'}


app.layout = html.Div(children = [
                html.H1('Hello Dash!', style = {'textAlign' : 'centre', 'color' : colors['text']})
                ,html.Div('Dash: Web Dashboards with Python')
                ,dcc.Graph(id = 'example'
                           ,figure = {'data': [
                                          {'x':[1,2,3] ,'y':[4,1,2],'type':'bar','name':'SF'}
                                          ,{'x':[1,2,3] ,'y':[4,1,2],'type':'bar','name':'SF'}
                                        ]
                                        , 'layout' : {
                                            'plot_bgcolor':colors['background']
                                            ,'paper_bgcolor':colors['background']
                                            ,'font':{'color':colors['text']}
                                            ,'title':'BAR PLOTS!'
                                        }
                                    }
                            )
], style={'backgroundColor':colors['background']}
)

if __name__ == '__main__':
    app.run_server()