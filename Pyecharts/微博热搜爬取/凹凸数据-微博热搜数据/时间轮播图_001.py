from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType, CurrentConfig


CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'
tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK))
for i in range(2015, 2020):
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), label_opts=opts.LabelOpts(position="right"))
        .add_yaxis("商家B", Faker.values(), label_opts=opts.LabelOpts(position="right"))
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts("Timeline-Bar-Reversal (时间: {} 年)".format(i))
        )
    )
    tl.add(bar, "{}年".format(i))
tl.render("timeline_bar_reversal.html")
