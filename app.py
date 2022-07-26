import dash
import dash_auth
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go


# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'Mickey': 'Mouse', 'Donald': 'Duck'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='auth example'
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in [1, 2, 3, 4, 5]],
        value=1
    ),

    html.Div(id='graph-title'),
    dcc.Graph(id='graph'),
    html.A('Code on Github', href='https://github.com/austinlasseter/dash-auth-example'),
    html.Br(),
    html.A("Data Source", href='https://dash.plotly.com/authentication'),
], className='container')

@app.callback(
    Output('graph-title', 'children'),
    Output('graph', 'figure'),
    Input('dropdown', 'value'),
    )
def update_graph(dropdown_value):

    x_values = [-3,-2,-1,0,1,2,3]
    y_values = [x**dropdown_value for x in x_values]
    colors=['black','red','green','blue','orange','purple']
    graph_title='Graph of {}'.format(str(dropdown_value))


    trace0 = go.Scatter(
        x = x_values,
        y = y_values,
        mode = 'lines',
        marker = {'color': colors[dropdown_value]},
    )

    # assign traces to data
    data = [trace0]
    layout = go.Layout(
        title = graph_title
    )

    # Generate the figure dictionary
    fig = go.Figure(data=data,layout=layout)

    return graph_title, fig


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
