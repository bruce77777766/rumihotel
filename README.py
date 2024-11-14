from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Гостиница в Душанбе</title>
    <style>
        /* Сброс стилей */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Основной фон с изображением */
        body {
            font-family: 'Arial', sans-serif;
            background: url('https://cdn-img.readytotrip.com/t/1024x768/extranet/30/88/3088b1d46b50b3552f0f65108f6b1804d0f6d7f6.jpeg') no-repeat center center fixed;
            background-size: cover;
            position: relative;
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
            line-height: 1.6;
            overflow: hidden;
        }

        /* Размытие фона */
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: inherit;
            filter: blur(8px);
            z-index: -1;
        }

        /* Стиль заголовков */
        h1.title {
            font-size: 4rem;
            margin-bottom: 20px;
            color: #fff;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.6);
            animation: fadeIn 2s ease-in-out, bounce 1s ease infinite;
        }

        p.subtitle {
            font-size: 1.5rem;
            color: #fff;
            margin-bottom: 30px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
            animation: fadeIn 2.5s ease-in-out;
        }

        /* Описание гостиницы */
        .description {
            font-size: 1.2rem;
            color: #f8f8f8;
            margin-bottom: 40px;
            max-width: 800px;
            line-height: 1.8;
            animation: fadeIn 3s ease-in-out;
            text-align: justify;
            margin: 0 20px;
            padding: 15px;
            background: rgba(0, 0, 0, 0.6); /* Прозрачный фон для улучшения читаемости */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease-in-out;
        }

        /* Стили для кнопки */
        .button {
            padding: 15px 30px;
            font-size: 1.5rem;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            margin-top: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            text-decoration: none;
            outline: none;
        }

        /* Эффект наведения на кнопку */
        .button:hover {
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        }

        .button:active {
            transform: scale(0.98);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        }

        .button:focus {
            outline: none;
        }

        .footer {
            position: fixed;
            bottom: 20px;
            font-size: 1rem;
            animation: fadeIn 3.5s ease-in-out;
            color: #dcdcdc;
        }

        /* Анимации */
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Анимация для прыжка заголовка */
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        /* Эффект подсветки текста при прокрутке */
        .fade-up {
            opacity: 0;
            transform: translateY(50px);
            animation: fadeUp 1s ease-out forwards;
        }

        @keyframes fadeUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Респонсивные стили для мобильных устройств */
        @media (max-width: 768px) {
            h1.title {
                font-size: 3rem;
            }

            p.subtitle {
                font-size: 1.2rem;
            }

            .description {
                font-size: 1rem;
                padding: 10px;
            }

            .button {
                font-size: 1.2rem;
                padding: 12px 24px;
            }
        }

        /* Эффект на описание гостиницы */
        .description p {
            opacity: 0;
            animation: slideIn 2s ease forwards;
        }

        /* Анимация появления текста */
        @keyframes slideIn {
            0% {
                opacity: 0;
                transform: translateX(-50px);
            }
            100% {
                opacity: 1;
                transform: translateX(0);
            }
        }

        /* Эффект при наведении на блоки */
        .description:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
        }

        /* Улучшение расположения контента */
        .content-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 1200px;
            z-index: 1;
        }

        .description-left {
            flex: 1;
            margin-right: 20px;
        }

        .description-right {
            flex: 1;
            margin-left: 20px;
        }

        /* Новый стиль для текста */
        .new-text-style {
            font-family: 'Verdana', sans-serif;
            font-size: 1.3rem;
            color: #fff;
            line-height: 1.8;
            text-align: left;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        }

    </style>
</head>
<body>
    <div class="content-wrapper">
        <div class="description-left fade-up">
            <h1 class="title">Гостиница в Душанбе</h1>
            <p class="subtitle">Уют и комфорт в самом сердце Душанбе</p>
            <div class="description">
                <p>Наша гостиница предоставляет вам комфорт и высококлассное обслуживание в самом центре города Душанбе. Мы гордимся тем, что можем предложить вам все необходимые удобства для вашего отдыха и работы.</p>
                <p>Наши номера оснащены всем необходимым для комфортного пребывания, а из окон открывается потрясающий вид на город. В гостинице есть рестораны, кафе, спа-салоны и конференц-залы — все, что нужно для отличного времяпрепровождения.</p>
                <p>Гостиница в Душанбе — это идеальное место для отдыха, бизнеса и мероприятий!</p>
            </div>
        </div>

        <div class="description-right fade-up">
            <div class="new-text-style">
                <p>Наши удобства:</p>
                <ul>
                    <li>Конференц-залы</li>
                    <li>Рестораны и кафе</li>
                    <li>Спа-салон</li>
                    <li>Прекрасные виды на город</li>
                </ul>
            </div>
            <a href="https://www.booking.com/hotel/tj/the-rumi-amp-residences.ru.html?aid=318615&label=New_Russian_RU_5226417865-_w6v8ikKQ6LuVL2ha1XdIwS217246872153%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg&sid=c43f48125437eded06d7aaebfce8d6d2&dest_id=900052907&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&hpos=1&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&srepoch=1731610360&srpvid=ab3084a72298057b&type=total&ucfs=1&activeTab=main#tab-main" class="button">Забронировать номер</a>
        </div>
    </div>

    <div class="footer fade-up">
        <p>© 2024 Гостиница в Душанбе. Все права защищены.</p>
    </div>
</body>
</html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
