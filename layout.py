import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    # Header
    html.Div([
        html.Div([
            html.H1('Job Shop Scheduler')
        ], className="nine columns")
    ], style={'color': 'white', 'backgroundColor': 'DarkBlue', "height": "125px"}),

    html.Div([
        html.Div([
            html.H3('Upload a Schedule'),
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    ["Click to select a file to upload."]
                ),
                style={
                    "width": "80%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=True,
            ),
            html.Div(id='status-upload'),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                html.H3('Run the Scheduler'),
                html.Button('Run Scheduler', id='schedule-run', className="button-primary"),
                html.Div(id='status-run'),

                html.Br(),
                html.Br(),

                html.Button('View Gantt', id='view-gantt', className="button-primary", disabled=True),

            ]),
        ], className="three columns"),

        html.Div([
            dcc.Graph(id='gantt-chart'),
        ], className="eight columns"),
    ], className="row"),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.H3('Download Template and Samples'),
    html.A(
        'Template File',
        id='download-link',
        download="template.csv",
        href="/download/template",
        target="_blank"
    ),
    html.Br(),
    html.A(
        'Sample File 1',
        id='sample-link',
        download="sample_1.csv",
        href="/download/sample1",
        target="_blank"
    ),
    html.Div(id='down-status'),

])