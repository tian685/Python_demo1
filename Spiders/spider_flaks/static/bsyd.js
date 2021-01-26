  // 基于准备好的dom，初始化echarts实例
var myChart1 = echarts.init(document.getElementById('chart_box'));


function mychart1(time){
    if(time=='year1'){
        var renShu = [ 80.00, 79.10, 81.45, 90.20, 89.30, 91.20, 88.30, 91.30, 90.65, 91.20, 90.30, 89.20, 87.30, 91.30, 90.65];
    }else if(time=='year2'){
        var renShu = [ 50.00, 90.00, 61.45, 78, 59.30, 95.00, 88.30, 61.30, 43.00, 51.20, 92.00, 69.20, 78.00, 91.30, 94.00];
    }else{
        //请求时间段数据
        //模拟时间段数据
        alert(time);
        var renShu = [80.00, 79.10, 81.45, 90.20, 89.30, 91.20, 88.30, 91.30, 90.65, 91.20, 90.30, 89.20, 87.30, 91.30, 90.65];

    };
        //配置及数据
        optionyear = {
            title: {
                text : "标室月度使用率",
                padding: [10, 100, 10, 500] , // 标题位置
                subtext : ""
            },
            tooltip: {
                formatter: '{c}%',
                trigger: 'axis',    //提示触发类型      'item':数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
                                                //'axis':坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                                                //'none':什么都不触发。
                show:true,     //是否显示提示框组件 默认为true
                axisPointer: {
                    type: 'cross',
                    crossStyle: {
                        color: '#999'
                    }
                }
            },
            legend: {
                data:['']
            },
            xAxis: [
                {
                    type: 'category',
                    data: ["201","202","203","601","602","603","604","605","606","701","702","703","704","705","706"],
                    axisPointer: {
                        type: 'shadow'
                    }
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '',
                    min:0,
                    max:92.00,
                    splitNumber:10,
                    axisLabel: {
                        formatter: '{value}%',
                    }
                },
            ],
            series: [
                {
                    name:'',
                    type:'bar',         //bar表示柱状图
                    barWidth:20,
                    data:renShu,//数据
                    itemStyle: {    //更多柱状图样式搜索API：series-bar.itemStyle
　　　　　　　　　　　　　　　　　　normal: {
    　　　　　　　　　　　　　　　　　　　　color: '#1E90FF',//改变柱状的颜色
                                       label: {
                                        show: true, //开启显示
                                        position: 'top', //在上方显示
                                        formatter: '{c}%'  ,   //百分比显示
                                        textStyle: { //数值样式
                                            color: 'black',    //柱上数据颜色
                                            fontSize: 16
                                        }
                                    }
    　　　　　　　　　　　　　　　　　　}
    　　　　　　　　　　　　　　　　},
                },
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart1.setOption(optionyear);
}
