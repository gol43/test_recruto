from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

GITHUB_LINK = "https://github.com/gol43"

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    name = request.query_params.get("name", "").strip()
    message = request.query_params.get("message", "").strip()
    
    footer_html = f'<footer style="margin-top:40px; font-size:0.9em; color:#fff;">GitHub: <a href="{GITHUB_LINK}" target="_blank" style="color:#ffd700;">gol43</a></footer>'
    
    # Если параметры есть, показываем результат
    if name and message:
        return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Recruto Test Service</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background: linear-gradient(135deg, #6e8efb, #a777e3);
                    color: #fff;
                    margin: 0;
                    text-align: center;
                }}
                h2 {{
                    background: rgba(0,0,0,0.3);
                    padding: 20px 40px;
                    border-radius: 12px;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                }}
                a.back {{
                    margin-top: 20px;
                    text-decoration: none;
                    color: #ffd700;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h2>Hello {name}! {message}!</h2>
            <a class="back" href="/">Вернуться назад</a>
            {footer_html}
        </body>
        </html>
        """
    else:
        # Форма, если параметры пустые
        return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Recruto Test Service</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background: linear-gradient(135deg, #6e8efb, #a777e3);
                    color: #fff;
                    margin: 0;
                }}
                form {{
                    display: flex;
                    flex-direction: column;
                    background: rgba(0,0,0,0.3);
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                }}
                input {{
                    margin: 10px 0;
                    padding: 12px 15px;
                    border-radius: 8px;
                    border: none;
                    font-size: 1em;
                }}
                button {{
                    padding: 12px;
                    border-radius: 8px;
                    border: none;
                    background-color: #ffd700;
                    font-weight: bold;
                    cursor: pointer;
                    transition: 0.3s;
                }}
                button:hover {{
                    background-color: #e6c200;
                }}
                h1 {{
                    margin-bottom: 30px;
                }}
                a.github {{
                    margin-top: 20px;
                    font-size: 0.9em;
                    color: #ffd700;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <h1>Recruto Test Service</h1>
            <form method="get">
                <input name="name" placeholder="Введите имя" value="Recruto"/>
                <input name="message" placeholder="Введите сообщение" value="Давай дружить"/>
                <button type="submit">Отправить</button>
            </form>
            {footer_html}
        </body>
        </html>
        """
