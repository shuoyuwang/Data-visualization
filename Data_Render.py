import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.charts import Bar, Map, Line, Pie, Funnel, Scatter, Radar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import plotly.graph_objects as go

pd.set_option('mode.chained_assignment', None)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sheet0 = pd.read_excel(r'./data.xlsx', sheet_name=0)


# 1 散点图：北京，上海，广东，天津，现有确诊量
citylist = ['北京', '上海', '广东', '天津']
scatt = Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, renderer='png'))
scatt.add_xaxis(citylist)
scatt.add_yaxis('现有确诊数量', [int(sheet0[sheet0.省份 == c].iloc[0].现有确诊) for c in citylist])
scatt.set_global_opts(
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津 现有确诊量"),
    yaxis_opts=opts.AxisOpts(name='人数', splitline_opts=opts.SplitLineOpts(is_show=True)),
    xaxis_opts=opts.AxisOpts(name='城市',
                             splitline_opts=opts.SplitLineOpts(is_show=True)),
    visualmap_opts=opts.VisualMapOpts(max_=130, is_show=False),
)
# scatt.render_notebook()
# scatt.render('1.html')
make_snapshot(snapshot, scatt.render(), "1.png")

# In[39]:


# 2 折线图：北京，上海，广东，天津，现有确诊量
line = Line(init_opts=opts.InitOpts(renderer='png'))
line.add_xaxis(citylist)
line.add_yaxis('现有确诊数量', [int(sheet0[sheet0.省份 == c].iloc[0].现有确诊) for c in citylist])
line.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津 现有确诊量", pos_left='30%'),
    yaxis_opts=opts.AxisOpts(name='人数', splitline_opts=opts.SplitLineOpts(is_show=True)),
    xaxis_opts=opts.AxisOpts(name='城市'),
)
# line.render_notebook()
# line.render('2.png')
make_snapshot(snapshot, line.render(), "2.png")

# In[80]:


# 3 直方图：北京，上海，广东，天津，现有确诊量
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, renderer='png'))
bar.add_xaxis(citylist)
bar.add_yaxis('累计确诊数量', [int(sheet0[sheet0.省份 == c].iloc[0].累计确诊) for c in citylist])
bar.reversal_axis()
bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
bar.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津 累计确诊数量", pos_left='30%'),
    yaxis_opts=opts.AxisOpts(name='城市', splitline_opts=opts.SplitLineOpts(is_show=True)),
    xaxis_opts=opts.AxisOpts(name='人数'),
)
# bar.render_notebook()
# bar.render('3.png')
make_snapshot(snapshot, bar.render(), "3.png")

# In[60]:


# 4 北京，上海，广东，天津，现有确诊量和现有确诊增量
bar = Bar(init_opts=opts.InitOpts(renderer='png'))
bar.add_xaxis(citylist)
bar.add_yaxis('现有确诊数量',
              [int(sheet0[sheet0.省份 == c].iloc[0].现有确诊) for c in citylist],
              label_opts=opts.LabelOpts(position="top"))
bar.add_yaxis('现有确诊增量',
              [int(sheet0[sheet0.省份 == c].iloc[0].现有确诊增量) for c in citylist],
              label_opts=opts.LabelOpts(position="bottom")
              )
# bar.reversal_axis()
bar.set_global_opts(
    legend_opts=opts.LegendOpts(pos_right='15%'),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津 现有确诊量及增量", pos_left='16%'),
    yaxis_opts=opts.AxisOpts(name='人数', splitline_opts=opts.SplitLineOpts(is_show=True)),
    xaxis_opts=opts.AxisOpts(name='城市'),
)
# bar.render_notebook()
# bar.render('4.png')
make_snapshot(snapshot, bar.render(), "4.png")

# In[77]:


# 5 亚洲，欧洲，非洲，大洋洲，北美洲，南美洲累计确诊量
sheet_asia = pd.read_excel(r'./data.xlsx', sheet_name=1)
sheet_euro = pd.read_excel(r'./data.xlsx', sheet_name=2)
sheet_afri = pd.read_excel(r'./data.xlsx', sheet_name=3)
sheet_ocea = pd.read_excel(r'./data.xlsx', sheet_name=4)
sheet_nort = pd.read_excel(r'./data.xlsx', sheet_name=5)
sheet_sour = pd.read_excel(r'./data.xlsx', sheet_name=6)

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, renderer='png'))
bar.add_xaxis(['亚洲', '欧洲', '非洲', '大洋洲', '北美洲', '南美洲'])
bar.add_yaxis('累计确诊',
              [
                  int(sheet_asia.累计确诊.sum()),
                  int(sheet_euro.累计确诊.sum()),
                  int(sheet_afri.累计确诊.sum()),
                  int(sheet_ocea.累计确诊.sum()),
                  int(sheet_nort.累计确诊.sum()),
                  int(sheet_sour.累计确诊.sum()),
              ]
              )
bar.set_global_opts(
    legend_opts=opts.LegendOpts(pos_right='15%'),
    title_opts=opts.TitleOpts(title="亚洲，欧洲，非洲，大洋洲，北美洲，南美洲累计确诊量", pos_left='16%'),
    yaxis_opts=opts.AxisOpts(name='人数', splitline_opts=opts.SplitLineOpts(is_show=True)),
    xaxis_opts=opts.AxisOpts(name='城市'),
)
# bar.render('5.png')
make_snapshot(snapshot, bar.render(), "5.png")

# In[93]:


# 6 北京，上海，广东，天津，累计确诊量 饼图
fig = go.Figure(data=[
    go.Pie(
        labels=citylist,
        hole=.4,
        textinfo='percent+label',
        values=[int(sheet0[sheet0.省份 == c].iloc[0].累计确诊) for c in citylist],
        pull=[0.2, 0, 0, 0]
    )])
fig.update_layout(
    title="北京，上海，广东，天津，累计确诊量",
    legend_title="城市",
)
# fig.show()
fig.write_image('6.png')

# In[97]:


# 7 亚洲，欧洲，非洲，大洋洲，北美洲，南美洲累计确诊量
fig = go.Figure(data=[
    go.Pie(
        labels=['亚洲', '欧洲', '非洲', '大洋洲', '北美洲', '南美洲'],
        textinfo='percent+label',
        values=[
            int(sheet_asia.累计确诊.sum()),
            int(sheet_euro.累计确诊.sum()),
            int(sheet_afri.累计确诊.sum()),
            int(sheet_ocea.累计确诊.sum()),
            int(sheet_nort.累计确诊.sum()),
            int(sheet_sour.累计确诊.sum()),
        ],
        pull=[0.1, 0, 0, 0]
    )])
fig.update_layout(
    title="亚洲，欧洲，非洲，大洋洲，北美洲，南美洲累计确诊量",
)
# fig.show()
fig.write_image('7.png')

# In[131]:


# 8 北京，上海，广东，天津，累计确诊量和现有确诊量 饼图
[int(sheet0[sheet0.省份 == c].iloc[0].累计确诊) for c in citylist]
pie = Pie(init_opts=opts.InitOpts(width="800px", height="400px", theme=ThemeType.ROMA, renderer='png'))
t = 20
for c in citylist:
    pie.add(c,
            [list(z) for z in zip(['累计确诊', '现有确诊'],
                                  [int(sheet0[sheet0.省份 == c].iloc[0].累计确诊),
                                   int(sheet0[sheet0.省份 == c].iloc[0].现有确诊)])],
            radius=[20, 30],
            center=['{}%'.format(t), '50%']
            )
    t = t + 20
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{a}\n{b}: {c}\n{d}%"))
pie.set_global_opts(
    legend_opts=opts.LegendOpts(pos_right='40%', pos_top='10%'),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津 现有确诊量及增量", pos_left='26%'),
)
# pie.render_notebook()
# pie.render('8.png')
make_snapshot(snapshot, pie.render(), "8.png")

# In[139]:


# 9 北京，上海，广东，天津，累计确诊量 雷达图
rad = Radar(init_opts=opts.InitOpts(width="800px", height="400px", theme=ThemeType.ROMA, renderer='png'))
rad.add_schema(
    schema=[
        opts.RadarIndicatorItem(name="北京", max_=10000),
        opts.RadarIndicatorItem(name="上海", max_=70000),
        opts.RadarIndicatorItem(name="广东", max_=10000),
        opts.RadarIndicatorItem(name="天津", max_=10000),
    ]
)
rad.add("累计确诊量", [[int(sheet0[sheet0.省份 == c].iloc[0].累计确诊) for c in citylist]])
rad.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
rad.set_global_opts(
    legend_opts=opts.LegendOpts(selected_mode="single"),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津，累计确诊量"),
)
# rad.render_notebook()
# rad.render('9.png')
make_snapshot(snapshot, rad.render(), "9.png")

# In[147]:


# 9 北京，上海，广东，天津，现有确诊量及增量 雷达图
rad = Radar(init_opts=opts.InitOpts(width="800px", height="500px", renderer='png'))
rad.add_schema(
    schema=[
        opts.RadarIndicatorItem(name="北京", max_=130),
        opts.RadarIndicatorItem(name="上海", max_=130),
        opts.RadarIndicatorItem(name="广东", max_=130),
        opts.RadarIndicatorItem(name="天津", max_=130),
    ]
)
rad.add("现有确诊量", [[int(sheet0[sheet0.省份 == c].iloc[0].现有确诊) for c in citylist]], color='black')
rad.add("现有确诊量增量", [[int(sheet0[sheet0.省份 == c].iloc[0].现有确诊增量) for c in citylist]])
rad.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
rad.set_global_opts(
    legend_opts=opts.LegendOpts(pos_right='80%', pos_top='10%'),
    title_opts=opts.TitleOpts(title="北京，上海，广东，天津，现有确诊量及增量"),
)
# rad.render_notebook()
# rad.render('10.png')
make_snapshot(snapshot, rad.render(), "10.png")
