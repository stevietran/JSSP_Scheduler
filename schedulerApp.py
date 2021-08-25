import dash
from dash.exceptions import PreventUpdate
from flask import send_file
from gantt import gantt_fig
from layout import layout
import os
from scheduler import jobshop_scheduler
from util import save_file

# Global variables
TEMPLATE_DIR = '/scheduler/template/'
TEMPLATE_NAME = 'template_3job.csv'
SAMPLE_NAME = 'template_28job.csv'
UPLOAD_DIRECTORY = "/scheduler/uploaded_files"

jobs_data = [  # task = (machine_id, processing_time).
    [(0, 3), (1, 2), (2, 2)],  # Job0
    [(0, 2), (2, 1), (1, 4)],  # Job1
    [(1, 4), (2, 3)]  # Job2
]

scheduler_data = []

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = dash.Dash(__name__)

app.layout = layout

# Handle download request
@app.server.route('/download/template')
def download_template():
    return send_file(os.path.join(TEMPLATE_DIR, TEMPLATE_NAME),
                     mimetype='text/csv',
                     attachment_filename='template.csv',
                     as_attachment=True
                     )

@app.server.route('/download/sample1')
def download_sample():
    return send_file(os.path.join(TEMPLATE_DIR, SAMPLE_NAME),
                     mimetype='text/csv',
                     attachment_filename='sample1.csv',
                     as_attachment=True
                     )

# Callback for viewing the gantt chart
@app.callback(
    dash.dependencies.Output('gantt-chart', 'figure'),
    [dash.dependencies.Input('view-gantt', 'n_clicks')]
)
def view_gantt(n):
    if n is None:
        raise PreventUpdate
    else:
        return gantt_fig(scheduler_data)

# Run the scprit when click the button and return the running status and enable view button
@app.callback(
    [
        dash.dependencies.Output('status-run', 'children'),
        dash.dependencies.Output('view-gantt', 'disabled')
    ],
    [dash.dependencies.Input('schedule-run', 'n_clicks')]
)
def run_scheduler(n):
    if n is None:
        return "Click the button to run the scheduler!", True
    else:
        global scheduler_data
        scheduler_data = jobshop_scheduler(jobs_data)
        return "The Gantt is ready for viewing", False

# Callback for uploading file
@app.callback(
    dash.dependencies.Output("status-upload", "children"),
    [
        dash.dependencies.Input("upload-data", "filename"),
        dash.dependencies.Input("upload-data", "contents")
    ],
)
def upload_file(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""
    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            status = save_file(name, data, UPLOAD_DIRECTORY)
        # TODO: Check file
        if status:
            return "Check the format of uploaded file"
        else:
            return "File Uploaded!"
    else:
        return "No File Selected!"

if __name__ == '__main__':
    # Test check_file
    # check_file("/scheduler/template/workordersTemplate.csv")
    app.run_server()
