from tkinter import *# xử lí giao diện 
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk #xử lí ảnh 
import random
import heapq
from collections import deque #dùng cho bfs


BG_MAIN   = "#fdf6f0"   # be sáng
BG_BOARD  = "#f5cda7"   # cam be nhạt
BTN_COLOR = "#e67e22"   # cam đất
BTN_HOVER = "#f39c12"   # cam sáng
TEXT_COLOR = "white"    # chữ trắng
FRAME_BG  = "#1e272e"   # nền đen cho Moves + Original Image


class Puzzle(Tk):
    def __init__(self):
        super().__init__()
        self.title("🧩 Puzzle Game")
        self.config(bg=BG_MAIN)
        self.resizable(0, 0)
        self.move_count = 0
        self.move_label = Label(self, text="Moves: 0", bg=BG_MAIN, fg="black", font=("Arial", 12, "bold"))
        self.move_label.pack(pady=5)
        self.create_state_log()


  

        # ==== Toolbar ====  thanh công cụ  
        toolbar = Frame(self, bg=BG_MAIN)
        toolbar.pack(pady=10)

        self.size_var = IntVar(value=3)
        Label(toolbar, text="Board size:", bg=BG_MAIN, fg="black", font=("Arial", 11, "bold")).pack(side=LEFT, padx=5)
        OptionMenu(toolbar, self.size_var, 3, 4, 5).pack(side=LEFT, padx=5)

        self._make_btn(toolbar, "Load Image", self.load_image).pack(side=LEFT, padx=5)
        self._make_btn(toolbar, "Shuffle", self.lets_go).pack(side=LEFT, padx=5)    
        self._make_btn(toolbar, "Reset", self.reset_game).pack(side=LEFT, padx=5)
        # === Dropdown chọn thuật toán ===
        self.algo_var = StringVar(value="BFS")
        algo_box = ttk.Combobox(toolbar, textvariable=self.algo_var, state="readonly",
                                values=["BFS", "DFS", "IDS", "UCS"])
        algo_box.pack(side=LEFT, padx=5)

        self._make_btn(toolbar, "Solve", self.run_solver).pack(side=LEFT, padx=5)   
        
              # ==== Menu ====
        menubar = Menu(self)
        self.config(menu=menubar)

        solve_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Solve", menu=solve_menu)
        solve_menu.add_command(label="Solve with BFS", command=self.bfs_solve)
        solve_menu.add_command(label="Solve with DFS", command=self.dfs_solve)
        solve_menu.add_command(label="Solve with IDS", command=self.ids_solve)
        solve_menu.add_command(label="Solve with UCS", command=self.ucs_solve)
    
        # ==== Main frames ====
        main_frame = Frame(self, bg=BG_MAIN)
        main_frame.pack(pady=20)

        self.board_frame = Frame(main_frame, bg=BG_BOARD, bd=4, relief=RIDGE) #bàn cờ bên trái
        self.board_frame.grid(row=0, column=0, padx=15)

        self.goal_frame = LabelFrame(main_frame, text="Original Image", bg=BG_MAIN, fg="black", font=("Arial", 12))#bản đích bên phải
        self.goal_frame.grid(row=0, column=1, padx=15)
        self.goal_label = Label(self.goal_frame, bg=BG_MAIN)
        self.goal_label.pack()

        # ==== Variables ====
        self.grid_size = 3 # số ô trên mỗi cạnh
        self.board_px = 420 # kích thước tổng bảng
        self.tile_px = self.board_px // self.grid_size # kích thước 1 ô
        self.tiles = []
        self.photos = [] # mảng lwuu ảnh tải lên
        self.order = [] #trạng thái hiện tại ( mảnh đang đứng vị trí nào trong bảng)
        self.solved_order = [] #trạng thái đích ( đã giải xong )
        self.empty_idx = None #chỉ số ô trong mảng
        self.goal_img = None    
        self.current_img = None




        # ==== Thêm bảng lưu trạng thái ====
    def create_state_log(self):
        # Frame chứa bảng
        self.log_frame = LabelFrame(self, text="Danh sách trạng thái", bg=BG_MAIN, fg="black", font=("Arial", 12))
        self.log_frame.pack(pady=10, fill="both", expand=True)

        # Treeview để hiển thị trạng thái
        self.state_table = ttk.Treeview(self.log_frame, columns=("idx", "state"), show="headings", height=8)
        self.state_table.heading("idx", text="Bước")
        self.state_table.heading("state", text="Trạng thái (order)")
        self.state_table.column("idx", width=60, anchor="center")
        self.state_table.column("state", width=400, anchor="w")
        self.state_table.pack(fill="both", expand=True)

        # Thanh cuộn
        scrollbar = ttk.Scrollbar(self.log_frame, orient="vertical", command=self.state_table.yview)
        self.state_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def log_state(self, idx, state):
        # Hàm thêm trạng thái vào bảng
        self.state_table.insert("", "end", values=(idx, state))



    def _make_btn(self, parent, text, cmd):
        b = Button(parent, text=text, command=cmd,
                   bg=BTN_COLOR, fg="white", font=("Arial", 10, "bold"),
                   activebackground=BTN_HOVER, activeforeground="black",
                   relief=RAISED, bd=2, padx=8, pady=4)
        return b
    def run_solver(self):
        algo = self.algo_var.get()
        if algo == "BFS":
            self.bfs_solve()
        elif algo == "DFS":
            self.dfs_solve()
        elif algo == "IDS":
            self.ids_solve()
        elif algo == "UCS":
            self.ucs_solve()
        else:
            messagebox.showwarning("Error", "Unknown algorithm!")




    def load_image(self):  # mở hộp chọn file , đọc kích thước grid và resize về ảnh 
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if not path: return
        self.grid_size = self.size_var.get() 
        self.tile_px = self.board_px // self.grid_size #resize ảnh về axa
        self.photos = [None] * (self.grid_size**2 + 1)

        img = Image.open(path).resize((self.board_px, self.board_px))
        self.current_img = img
        self.goal_img = ImageTk.PhotoImage(img) # giữ ảnh gốc để tham chiếu goal state k bị biến mất 
        self.goal_label.config(image=self.goal_img)

        for r in range(self.grid_size):
            for c in range(self.grid_size):
                idx = r*self.grid_size + c + 1
                if idx == self.grid_size**2:
                    self.photos[idx] = None   # cắt ảnh từng miếng và lưu vào , riêng ô n^2 là ô trống
                else:
                    crop = img.crop((c*self.tile_px, r*self.tile_px,
                                     (c+1)*self.tile_px, (r+1)*self.tile_px))
                    self.photos[idx] = ImageTk.PhotoImage(crop)

        self.solved_order = list(range(1, self.grid_size**2+1)) 
        self.order = self.solved_order[:]
        self.empty_idx = len(self.order)-1
        self._draw_board()
        self.lets_go()


#tạo lưới và blind click , khi click vào 1 ô thì gọi hàm try_move để di chuyển 
    def _draw_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()
        self.tiles.clear()

        idx = 0
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                canvas = Canvas(self.board_frame, width=self.tile_px, height=self.tile_px,
                                bg=BG_BOARD, highlightthickness=0)
                canvas.grid(row=i, column=j, padx=1, pady=1)
                canvas.bind("<Button-1>", lambda e, pos=idx: self.try_move(pos)) #blind click 
                self.tiles.append(canvas)
                idx += 1
        self._apply_order()

    def _apply_order(self): # duyệt từng vị trí pos, lấy id của mảnh title id  , nếu k phải ô trống thì tải ảnh lên 
        for pos, tile_id in enumerate(self.order):
            canvas = self.tiles[pos]
            canvas.delete("all")
            if tile_id != self.grid_size**2:
                canvas.create_image(0, 0, anchor=NW, image=self.photos[tile_id])
                canvas.create_rectangle(0, 0, self.tile_px, self.tile_px, outline="white", width=2)

    def lets_go(self): #xào trộn an toàn từ trạng thái đích ,chọn ngẫu nhiên 1 hàng xóm  random 200 lần
        if not self.photos: return
        self.order = self.solved_order[:]
        self.empty_idx = len(self.order)-1
        last = None # không đi ngược lại ngay lặp tức
        for _ in range(200):
            neighbors = self._neighbors(self.empty_idx)
            if last in neighbors and len(neighbors) > 1:
                neighbors.remove(last)
            move = random.choice(neighbors)
            self.order[self.empty_idx], self.order[move] = self.order[move], self.order[self.empty_idx]
            last, self.empty_idx = self.empty_idx, move
            self.move_count = 0
        self.move_label.config(text="Moves: 0")

        self._apply_order()

    def reset_game(self):
        if self.current_img:    
            self.order = self.solved_order[:]
            self.empty_idx = len(self.order)-1
            self._apply_order()

    def try_move(self, idx): #click vào idx, nếu idx kề empty_idx thì hoán đổi nó trong order,cập nhật lại empty_idx và tăng move count
        if not self._adjacent(idx, self.empty_idx): return
        self.order[self.empty_idx], self.order[idx] = self.order[idx], self.order[self.empty_idx]
        self.empty_idx = idx
        self._apply_order() 
        if self.order == self.solved_order:
            messagebox.showinfo("🎉 WIN", "You solved the puzzle!")
        self.move_count += 1
        self.move_label.config(text=f"Moves: {self.move_count}")
        

        #bấm vào ô liền kê , đổi chỗ , khi trạng thái hiện tại = trạng thái đích thông báo đã xong 


    def _neighbors(self, idx):
        r, c = divmod(idx, self.grid_size)
        nbs = []
        if r > 0: nbs.append(idx - self.grid_size)
        if r < self.grid_size-1: nbs.append(idx + self.grid_size)
        if c > 0: nbs.append(idx - 1)
        if c < self.grid_size-1: nbs.append(idx + 1)
        return nbs

    def _adjacent(self, a, b):
        ra, ca = divmod(a, self.grid_size)
        rb, cb = divmod(b, self.grid_size)
        return abs(ra-rb) + abs(ca-cb) == 1

    # === BFS ===
    def bfs_solve(self): # tìm chuỗi ngắn nhất từ start -> goal , state ở đây là các tuple chứa title)id
        start = tuple(self.order)
        goal = tuple(self.solved_order) 
        # dùng deque để có thể dùng hàm popleft
        queue = deque([(start, [])]) # path là danh sách lưu các vị trí mà ta đã di chuyển (mỗi phần tử là nb , vị trí mà ô trống đi đến )
        visited = set() # tránh lặp lại trạng thái đã duyệt 

        while queue:
            state, path = queue.popleft()
            if state == goal:
                messagebox.showinfo("BFS Done", f"Số bước dịch chuyển: {len(path)}")
                self.animate(path) # mỗi trạng thái lưu path bước đi , khi tìm thấy gọi animate(path)
                return
            if state in visited: continue
            visited.add(state)

            empty = state.index(self.grid_size**2) # nếu chưa thăm tìm vị trí của ô trống state ,với mỗi nb của embty tạo trạng thái mới newstate bằng cách đổi chổ empty với nb
            for nb in self._neighbors(empty):
                new_state = list(state)
                new_state[empty], new_state[nb] = new_state[nb], new_state[empty]
                if tuple(new_state) not in visited:
                    self.log_state(len(path)+1, new_state)
                    queue.append((tuple(new_state), path+[nb])) # đưa này vào hàng đợi 

    # === DFS ===
    def dfs_solve(self):
        start = tuple(self.order)
        goal = tuple(self.solved_order)

        stack = [(start, [])]
        visited = set()

        while stack:
            state, path = stack.pop() #k có leftpop
            if state == goal:
                messagebox.showinfo("DFS Done", f"Số bước dịch chuyển: {len(path)}")
                self.animate(path)
                return
            if state in visited: continue
            visited.add(state)

            empty = state.index(self.grid_size**2)
            for nb in self._neighbors(empty):
                new_state = list(state)
                new_state[empty], new_state[nb] = new_state[nb], new_state[empty]
                if tuple(new_state) not in visited:
                    stack.append((tuple(new_state), path+[nb]))

                    
    def ids_solve(self):
        start = tuple(self.order)
        goal = tuple(self.solved_order)

        def dls(state, path, depth, visited):
            if state == goal:
                return path # nếu đạt thì trả về chuỗi bước đi 
            if depth == 0:
                return None #nếu đạt giới hạn độ sâu thì dừng 
            empty = state.index(self.grid_size**2) # vị trí ô trống
            for nb in self._neighbors(empty): #xét các ô liền kề 
                new_state = list(state) # copy trạng thái hiện tại 
                new_state[empty], new_state[nb] = new_state[nb], new_state[empty]
                new_state = tuple(new_state)
                if new_state not in visited: # tránh lặp lại 
                    visited.add(new_state)
                    res = dls(new_state, path+[nb], depth-1, visited) # gọi đệ quy dfs
                    if res: 
                        return res
            return None

        # Lặp tăng depth dần
        for depth in range(1, 50):  # giới hạn max depth 50 (có thể tăng)
            visited = set([start]) #reset visited  mỗi lăng tăng depth
            result = dls(start, [], depth, visited)
            if result: # tìm thấy lời giải
                messagebox.showinfo("IDS Done", f"Số bước dịch chuyển: {len(result)} (depth={depth})")
                self.animate(result)
                return
        messagebox.showwarning("IDS", "Không tìm thấy lời giải trong depth limit!")

    

    def ucs_solve(self):
        start = tuple(self.order)
        goal = tuple(self.solved_order)

        pq = [(0, start, [])]  # (cost, state, path) hàng đợi ưu tiên 
        visited = {} # để lưu trạng thái -> cost nhỏ nhất

        while pq:
            cost, state, path = heapq.heappop(pq) # lấy state có cost thấp nhất
            if state == goal:
                messagebox.showinfo("UCS Done", f"Số bước dịch chuyển: {len(path)}, cost={cost}")
                self.animate(path)
                return
            if state in visited and visited[state] <= cost: # nếu đã thăm state và cost nhỏ hơn thì bỏ qua
                continue
            visited[state] = cost

            empty = state.index(self.grid_size**2) # sinh trạng thái mới ,với mỗi nb kề, tạo trạng thái mới  và đưa vào hàng đợi ưu tiên với cost + 1
            for nb in self._neighbors(empty):
                new_state = list(state)
                new_state[empty], new_state[nb] = new_state[nb], new_state[empty]
                new_state = tuple(new_state)
                heapq.heappush(pq, (cost+1, new_state, path+[nb]))



    # Animate solution
    def animate(self, path, i=0, delay=200):
        if i >= len(path):
            return
        self.try_move(path[i])
        self.after(delay, lambda: self.animate(path, i+1, delay))
 

if __name__ == "__main__":
    app = Puzzle()
    app.mainloop()
