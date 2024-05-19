# Div demo

# Import Libraries
import dash
import dash_html_components as html

# Start the app
app = dash.Dash()

# Create the app layout
app.layout = html.Div(['This is the outermost div!',
                        html.Div(['This is an inner div!'],
                            style = {'color':'red'}),
                        html.Div(['Another inner div!'],
                                 style={'color':'blue','border':'3px blue solid'})],
                      style = {'color': 'green', 'border':'2px green solid'})

# Run the server
if __name__ == '__main__':
    app.run_server()