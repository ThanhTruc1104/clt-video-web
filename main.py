from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import matplotlib.pyplot as plt
import io
import base64

# 1. Khởi tạo ứng dụng FastAPI (Render sẽ tìm biến 'app' này)
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Trang chủ hiển thị thông điệp hoặc giao diện web
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Mô Phỏng Giới Hạn Trung Tâm</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
                h1 { color: #333; }
                p { color: #666; }
            </style>
        </head>
        <body>
            <h1>Ứng dụng Mô phỏng Định lý Giới hạn Trung tâm</h1>
            <p>Ứng dụng đã hoạt động thành công trên Render!</p>
            <img src="data:mo_phong_clt.gif;base64,{gif_base64}" alt="Mô phỏng CLT">
        </body>
    </html>
    """
    return html_content
