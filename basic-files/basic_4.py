# Dash core components demo

# Import libraries here
import dash
import dash_core_components as dcc
import dash_html_components as html

# Start app
app = dash.Dash()

# Instaniciate app layout
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label':'New York City',
                           'value':'NYC'},
                           {'label':'San Francisco',
                            'value':'SF'}],
                value='SF'),
    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step = 0.5, value = 0),
    html.Label('Some Radio Items'),
    dcc.RadioItems(options=[{'label':'New York City',
                             'value':'NYC'},
                             {'label': 'San Francisco',
                              'value':'SF'}],
                value = 'SF')
])

# Start server
if __name__ == '__main__':
    app.run_server()
