#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

example_data = [
    ("黑龙江", [127.9688, 45.368, 100, 100]),
    ("内蒙古", [110.3467, 41.4899, 300, 100]),
    ("吉林", [125.8154, 44.2584, 300, 100]),
    ("辽宁", [123.1238, 42.1216, 300, 100]),
    ("河北", [114.4995, 38.1006, 300, 100]),
    ("天津", [117.4219, 39.4189, 300, 100]),
    ("山西", [112.3352, 37.9413, 300, 100]),
    ("陕西", [109.1162, 34.2004, 300, 200]),
    ("甘肃", [103.5901, 36.3043, 300, 200]),
    ("宁夏", [106.3586, 38.1775, 300, 200]),
    ("青海", [101.4038, 36.8207, 300, 200]),
    ("新疆", [87.9236, 43.5883, 300, 200]),
    ("西藏", [91.11, 29.97, 300, 100]),
    ("四川", [103.9526, 30.7617, 300, 100]),
    ("重庆", [108.384366, 30.439702, 300, 100]),
    ("山东", [117.1582, 36.8701, 300, 100]),
    ("河南", [113.4668, 34.6234, 300, 100]),
    ("江苏", [118.8062, 31.9208, 300, 100]),
    ("安徽", [117.29, 32.0581, 300, 100]),
    ("湖北", [114.3896, 30.6628, 300, 200]),
    ("浙江", [119.5313, 29.8773, 300, 100]),
    ("福建", [119.4543, 25.9222, 300, 100]),
    ("江西", [116.0046, 28.6633, 300, 100]),
    ("湖南", [113.0823, 28.2568, 300, 100]),
    ("贵州", [106.6992, 26.7682, 300, 100]),
    ("广西", [108.479, 23.1152, 300, 200]),
    ("海南", [110.3893, 19.8516, 300, 100]),
    ("上海", [121.4648, 31.2891, 1300, 100]),
]

c = (
    Map3D()
    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,23,11,0)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(
        series_name="bar3D",
        data_pair=example_data,
        type_=ChartType.BAR3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Bar3D"))
    .render("map3d_with_bar3d.html")
)
