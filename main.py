import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route('/images')
def images():
    return f'''<!doctype html>
                    <html lang="ru">
                    <head>
                        <!-- Required meta tags -->
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">

                        <!-- Bootstrap CSS -->
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <!-- Google fonts -->
                        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" rel="stylesheet">
                        <link href='static/css/style.css' rel='stylesheet'>

                        <title>Пейзажи Марса</title>
                    </head>
                    <body>
                    <h1>Пейзажи Марса</h1>
                        <!-- Carousel in a container -->
                    <div class="container">
                            <div id="carousel-basic" class="carousel slide" data-ride="carousel">
                                <!-- Indicators -->
                                <ol class="carousel-indicators">
                                    <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                                    <li data-target="carousel-basic" data-slide-to="1"></li>
                                    <li data-target="carousel-basic" data-slide-to="2"></li>
                                </ol>

                                <!-- Wrapper -->
                                <div class="carousel-inner" role="listbox">
                                    <div class="carousel-item active">
                                        <img src="https://images.wallpaperscraft.ru/image/single/zvezdy_mlechnyj_put_prostranstvo_kosmos_116893_1280x720.jpg" alt="" class="img-fluid">
                                    </div>
                                    <div class="carousel-item">
                                        <img src="https://images.wallpaperscraft.ru/image/single/zvezdy_kosmos_nebo_blesk_116409_1280x720.jpg" alt="" class="img-fluid">
                                    </div>
                                    <div class="carousel-item">
                                        <img src="https://images.wallpaperscraft.ru/image/single/zvezdy_mlechnyj_put_zvezdnoe_nebo_119836_1280x720.jpg" alt="" class="img-fluid">
                                    </div>
                                </div>

                                <!-- Controls -->
                                <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span class="sr-only">Назад</span>
                                </a>
                                <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span class="sr-only">Вперед</span>
                                </a>
                            </div>

                            <!-- Content -->

                        </div>

                        <!-- Optional JavaScript -->
                        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    </body>
                    </html>'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
