window.onload = function () {
    document.getElementById("url").value = '';
    document.getElementById('textcontent').value = ''
    draw([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
}

function draw(shuju) {
    console.log('****************')
    var graph = echarts.init(document.getElementById('chart'));
    var option = {
        title: {
            text: '分类结果-如图所示:',
            x: 'left',
            y: 'top',
            textStyle: {fontSize: 15,}

        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'line'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        legend: {
            data: ['概率'],
            x: 'right',
            y: 'top',

        },

        xAxis: [{
            type: 'category',
            data: ['科技', '体育', '健康', '军事', '招聘', '教育', '文化', '旅游', '汽车', '经济'],
            axisTick: {
                alignWithLabel: true
            }

        }],
        yAxis: [
            {
                type: 'value'
            }
        ],
        color: ['#882888'],
        series: [
            {
                name: '概率',
                type: 'bar',
                label: {
                    normal: {
                        show: true,
                        position: 'top'
                    }
                },
                data: shuju,

            }
        ],

    };

    graph.setOption(option);
    window.onresize = function () {
        graph.resize();
    }
}

function url() {
    rurl = document.getElementById("url").value
    console.log(rurl)
    if (rurl == '') {
        return alert('链接不能为空！！');
    }
    $.ajax({
        type: 'POST',
        url: '/newscontent',
        data: JSON.stringify({text: rurl}),
        contentType: 'application/json',
        dataType: 'json',
        success: function (result) {
            if (result['news'] == 'False') {
                alert("链接输入有误")
            }
            else {
                document.getElementById('textcontent').value = result['news'];
                console.log(result['news']);
            }
        },
        error: function (result) {
            alert("访问接口失败");
            console.log(result);
        }
    });
}

function api() {
    textcontent = document.getElementById("textcontent").value
    if(textcontent=='') {
        return alert('输入文本内容不能为空！！！');
    }
    // console.log(textcontent)
    $.ajax({
        type: 'POST',
        url: '/functionapi',
        data: JSON.stringify({text: textcontent}),
        contentType: 'application/json',
        dataType: 'json',
        success: function (result) {
            draw(result['shuju']);
            console.log(result['shuju']);
            // var pre = document.getElementById('t_result');
            // pre.innerHTML = '<h3>推荐类别：' + res['pre'] + '</h3>'
        },
        error: function (result) {
            alert("访问接口失败");
            console.log(result);
        }
    });
}


//点击导入按钮,使files触发点击事件,然后完成读取文件的操作
function setchange() {
    $("#files").click();
}

function fileImport() {
    //获取读取文件的File对象
    var selectedFile = document.getElementById('files').files[0];
    var reader = new FileReader();//这是核心,读取操作就是由它完成.
    reader.readAsText(selectedFile, 'Gbk');//读取文件的内容,也可以读取文件的URL
    reader.onload = function () {
        //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
        document.getElementById('textcontent').value = this.result;
        // console.log(this.result);
    }
}
function tip() {
    alert("测试文本三种输入方式:\n 1. 手动输入测试文本。\n 2. 打开本机特定文本。\n 3. 输入特定新闻链接。")
}
