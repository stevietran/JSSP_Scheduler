import numpy as np
import pandas as pd
import plotly.figure_factory as ff

def gantt_fig(data):
    # Generate random color for each job
    df = pd.DataFrame(data)
    all_jobs = df['Job'].unique()
    colors = []
    for job in all_jobs:
        colors.append((job, 'rgb' + str(tuple(np.random.choice(range(256), size=3)))))

    colors = dict(colors)
    # print(colors)

    fig = ff.create_gantt(data, colors=colors, index_col='Job',
                          group_tasks=True, show_colorbar=True,
                          showgrid_x=True, title='Gantt Chart')
    # fig.show()
    fig['layout'].update(margin=dict(l=310))
    return fig