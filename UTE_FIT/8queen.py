import random
import tkinter as tk
from tkinter import messagebox

# ========================
# HÀM HỖ TRỢ
# ========================
def compute_conflicts(state):
    """Tổng số cặp hậu xung đột (global heuristic)."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def conflicts_for_col_state(state, col):
    """Số xung đột liên quan tới hậu ở cột `col` cho state truyền vào."""
    n = len(state)
    cnt = 0
    for c in range(n):
        if c == col:
            continue
        if state[c] == state[col] or abs(state[c] - state[col]) == abs(c - col):
            cnt += 1
    return cnt

# ========================
# GUI + MIN-CONFLICTS (phiên bản ổn định)
# ========================
class NQueensGUI:
    def __init__(self, n=8, size=60):
        self.n = n
        self.size = size
        self.state = [random.randrange(n) for _ in range(n)]

        self.window = tk.Tk()
        self.window.title(f"{n}-Queens - Min-Conflicts (stable)")

        self.canvas = tk.Canvas(self.window, width=n * size, height=n * size)
        self.canvas.pack(pady=10)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack()
        self.solve_btn = tk.Button(btn_frame, text="Solve", command=self.start_solve, bg="#4CAF50", fg="white", width=10)
        self.solve_btn.grid(row=0, column=0, padx=5)
        self.restart_btn = tk.Button(btn_frame, text="Restart", command=self.restart, bg="#2196F3", fg="white", width=10)
        self.restart_btn.grid(row=0, column=1, padx=5)

        self.draw_board(self.state)

        # trạng thái solve
        self._solving = False
        self.steps = 0
        self.restarts = 0
        self.max_steps_before_restart = 1000  # nếu quá nhiều bước thì random restart
        self.max_restarts = 50               # nếu đã restart quá nhiều lần -> dừng và báo

    def draw_board(self, state=None):
        self.canvas.delete("all")
        for r in range(self.n):
            for c in range(self.n):
                x1, y1 = c * self.size, r * self.size
                x2, y2 = x1 + self.size, y1 + self.size
                color = "#EEEED2" if (r + c) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

        if state:
            for c in range(self.n):
                r = state[c]
                x = c * self.size + self.size / 2
                y = r * self.size + self.size / 2
                self.canvas.create_text(x, y, text="♛", font=("Arial", int(self.size * 0.6), "bold"), fill="gold")
        self.window.update_idletasks()

    def start_solve(self):
        if self._solving:
            return
        self._solving = True
        self.solve_btn.config(state="disabled")
        self.restart_btn.config(state="disabled")
        self.steps = 0
        self.restarts = 0
        self.min_conflicts_step()

    def min_conflicts_step(self):
        """Một bước của min-conflicts (chạy trên event-loop bằng after)."""
        # kiểm tra nghiệm
        if compute_conflicts(self.state) == 0:
            self._solving = False
            self.solve_btn.config(state="normal")
            self.restart_btn.config(state="normal")
            messagebox.showinfo("Hoàn tất", "Đã tìm được nghiệm (h = 0).")
            return

        # danh sách cột đang xung đột
        conflicted = [c for c in range(self.n) if conflicts_for_col_state(self.state, c) > 0]
        if not conflicted:
            # không còn cột xung đột => nghiệm
            self._solving = False
            self.solve_btn.config(state="normal")
            self.restart_btn.config(state="normal")
            messagebox.showinfo("Hoàn tất", "Đã tìm được nghiệm (không cột xung đột).")
            return

        col = random.choice(conflicted)

        # thử tất cả hàng cho cột `col` bằng temp_state (không thay đổi self.state trực tiếp)
        best_rows = []
        best_h = None
        for r in range(self.n):
            temp = list(self.state)
            temp[col] = r
            h = conflicts_for_col_state(temp, col)
            if best_h is None or h < best_h:
                best_h = h
                best_rows = [r]
            elif h == best_h:
                best_rows.append(r)

        # chọn ngẫu nhiên 1 hàng tốt nhất (bao gồm khả năng giữ nguyên hàng)
        if best_rows:
            self.state[col] = random.choice(best_rows)
        else:
            self.state[col] = random.randrange(self.n)

        self.draw_board(self.state)
        self.steps += 1

        # nếu chạy quá nhiều bước -> random restart
        if self.steps > self.max_steps_before_restart:
            self.restarts += 1
            if self.restarts > self.max_restarts:
                # dừng và báo người dùng
                self._solving = False
                self.solve_btn.config(state="normal")
                self.restart_btn.config(state="normal")
                messagebox.showwarning("Dừng lại", f"Đã thử restart {self.restarts} lần nhưng chưa tìm được nghiệm. Thử lại hoặc tăng giới hạn.")
                return
            # thực hiện restart
            self.state = [random.randrange(self.n) for _ in range(self.n)]
            self.steps = 0
            self.draw_board(self.state)

        # schedule bước tiếp theo (50 ms)
        self.window.after(50, self.min_conflicts_step)

    def restart(self):
        if self._solving:
            return
        self.state = [random.randrange(self.n) for _ in range(self.n)]
        self.draw_board(self.state)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = NQueensGUI(n=8, size=70)
    gui.run()
