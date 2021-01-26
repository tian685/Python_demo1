<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>echarts</title>
    <style type="text/css">
        html,
        body {
            width: 100%;
            height: 100%;
        }

        body {
            margin: 0px;
            padding: 0px
        }

        div {
            float: left;
        }

        #container {
            width: 50%;
            height: 100%;
        }

        #info {
            padding: 10px 20px;
        }
    </style>
</head>

<body>
    <div id="container"></div>
    <div id="info">数据展示：</div>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="{{ url_for('static', filename='t_mysql.js') }}"></script>
	<script type="text/javascript">


	</script>

</body>

</html>