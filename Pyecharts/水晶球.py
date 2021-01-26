#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥

from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType

c = (
    Liquid()
    .add("lq", [0.5, 0.5], is_outline_show=False, shape=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-arrow"))
    .render("liquid01_shape_arrow.html")
)

