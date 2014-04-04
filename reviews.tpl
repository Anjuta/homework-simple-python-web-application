<html>
    <head>
        <title>Service reviews</title>
        <link href="http://localhost:8080/static/style.css" rel="stylesheet" type='text/css' />
    </head>
    <body>
        <div class='content'>
            <div class='header'>{{header}}</div>
            <div class='reviews'>
                %if int(num_page) < len(reviews) / 10:
                    %count = 10
                %else:
                    %count = len(reviews) % 10
                %end
                %for i in range(count):
                    %review = reviews[i + int(num_page) * 10]
                    <div class='review'>{{review}}</div>
                %end
            </div>
            <form action='/reviews/{{header}}/add' class='text'>
                <textarea name='review' type='text' rows='5' autofocus required></textarea>
                <br>
                <input class='input_button' name='send_comment' type='submit' value='Send'>
            </form>
            <a href='/'>Home</a>
            <div class='pages' align='center'>
                %count = len(reviews) / 10
                %if len(reviews) % 10 > 0:
                %   count += 1
                %end
                %for i in range(count):
                    <a href='/reviews/{{header}}/{{i}}'>{{i}}</a>
                %end
            </div>
        </div>
    </body>
</html>