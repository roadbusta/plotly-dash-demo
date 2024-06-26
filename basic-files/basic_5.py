import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Instanciate the app object
app = dash.Dash()

# Set up dash layout
app.layout = html.Div([
    dcc.Input(id='my-id', value='Initial Text', type = 'text'),
    html.Div(id='my-div', style={'border':'2px blue solid'} )
])

# Create a callback
@app.callback(Output(component_id = 'my-div', component_property = 'children'),
              [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value):
    return "You entered: {}".format(input_value)

if __name__ == '__main__':
    app.run_server()