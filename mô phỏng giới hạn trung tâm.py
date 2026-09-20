import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML

# 1. Khởi tạo tham số
num_samples = 10000
sample_sizes = [1, 2, 5, 10, 20, 30, 50, 100]

fig, ax = plt.subplots(figsize=(8, 5))


# 2. Hàm vẽ từng frame
def update(frame):
    ax.clear()
    n = sample_sizes[frame]

    # Lấy mẫu ngẫu nhiên từ phân phối đều Uniform(0, 1)
    samples = np.random.uniform(0, 1, size=(num_samples, n))
    x_bar = np.mean(samples, axis=1)

    # Vẽ Bảng ghép lớp (Histogram)
    ax.hist(
        x_bar,
        bins=50,
        density=True,
        edgecolor="black",
        alpha=0.7,
        color="skyblue",
    )

    # Tiêu đề và nhãn
    ax.set_title(
        f"Mô phỏng Định lý Giới hạn Trung tâm (n = {n})",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel(r"Trung bình mẫu $\overline{X}$", fontsize=12)
    ax.set_ylabel("Mật độ tần suất", fontsize=12)
    ax.set_xlim(0, 1)
    ax.grid(True, linestyle="--", alpha=0.5)

    # Vẽ đường phân phối chuẩn lý thuyết
    if n > 1:
        mu = 0.5
        sigma = np.sqrt(1 / 12) / np.sqrt(n)
        x = np.linspace(0, 1, 500)
        p = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((x - mu) / sigma) ** 2
        )
        ax.plot(x, p, "r-", linewidth=2, label="Phân phối chuẩn lý thuyết")
        ax.legend(loc="upper right")


# 3. Tạo Animation
ani = animation.FuncAnimation(
    fig, update, frames=len(sample_sizes), interval=1000, repeat=True
)

# Đóng figure mặc định của matplotlib để không bị hiện hình tĩnh thừa
plt.close(fig)

# 4. Phát VIDEO CHUYỂN ĐỘNG trực tiếp trên Notebook
HTML(ani.to_jshtml())
