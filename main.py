from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

# 1. Route phục vụ file GIF
@app.get("/mo_phong_clt.gif")
def get_gif():
    return FileResponse("mo_phong_clt.gif", media_type="image/gif")

# 2. Trang chủ HTML
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mô Phỏng Giới Hạn Trung Tâm</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f9f9f9; }
            h1 { color: #333; }
            p { color: #666; }
            img { max-width: 80%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Ứng dụng Mô phỏng Định lý Giới hạn Trung tâm</h1>
        <p>Ứng dụng đã hoạt động thành công trên Render!</p>
        
        <img src="/mo_phong_clt.gif" alt="Mô phỏng Định lý Giới hạn Trung tâm">
    </body>
    </html>
    """
    return html_content
