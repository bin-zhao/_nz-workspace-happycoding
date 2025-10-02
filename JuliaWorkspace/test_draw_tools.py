#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
目前看，主要有两种：plot和浏览器版本。而且，无论哪种方法都远远赶不上游戏引擎。
    游戏引擎还有巨大的潜力。目前还没有一个图形引擎是作为平台被使用的。浏览器是个强劲对手，但是浏览器面对海量数据，还是差很远。
    在显示方面，图形引擎是最强的。术业有专攻，体会又多了一些。

现在无所谓，凑合着用。
'''

#网页版。
if False:
    import plotly.express as px

    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    fig.show()

#没显示，没报错。
if False:
    from bokeh.plotting import figure, show
    from bokeh.io import output_notebook

    output_notebook()

    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Temp.", line_width=2)
    show(p)

#它基于plot，未必更高效。
if False:
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.show()

#没显示，疑似报错：alt.Chart(...)
if False:
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    chart = alt.Chart(source).mark_circle(size=60).encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
        tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    chart.show()

#没显示，没报错。
if False:
    import holoviews as hv
    from holoviews import opts
    import numpy as np

    hv.extension('bokeh')

    xs = np.linspace(0, np.pi*2, 100)
    ys = np.sin(xs)

    hv.Curve((xs, ys)).opts(width=600, height=400)

#基于plot。
if False:
    from plotnine import ggplot, aes, geom_line
    import pandas as pd

    df = pd.DataFrame({
        'x': range(10),
        'y': [x**2 for x in range(10)]
    })

    p = (ggplot(df, aes('x', 'y')) + geom_line())
    print(p)

