import tkinter as tk
from tkinter import ttk

def select_file():
    filetypes = [("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
    initial_dir = r"c:\users\asanuma\Desktop"
    
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir=initial_dir,
        filetypes=filetypes
    )
    
    return file_path

class Callbacks:
    def __init__(self, root, input_entry, output_entry):
        self.root = root
        self.input_entry = input_entry
        self.output_entry = output_entry

    def on_generate(self):
        # Generateボタンがクリックされたときの処理
        input_value = self.input_entry.get()
        output_value = self.output_entry.get()
        print(f"Generating with input: {input_value} and output: {output_value}")

    def on_save(self):
        # Saveボタンがクリックされたときの処理
        output_value = self.output_entry.get()
        print(f"Saving output: {output_value}")

    def on_select_input(self):
        # Inputボタンがクリックされたときの処理
        file_path = select_file()
        print(f"input file : {file_path}")

    def on_select_output(self):
        # Outputボタンがクリックされたときの処理
        file_path = select_file()
        print(f"output file : {file_path}")

    def on_exit(self):
        # Exitボタンがクリックされたときの処理
        print("Exiting application")
        self.root.destroy()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("vEzRapper")

        # 2列目の長さを指定する変数
        self.column_width = 30
        self.bpm_width = 10

        # ウィジェットの作成とレイアウト
        self.create_and_layout_widgets()

        # コールバッククラスのインスタンス化
        self.callbacks = Callbacks(self.root, self.input_entry, self.output_entry)

        # イベントバインディングの設定
        self.bind_events()

        # ウィンドウサイズを全ウィジェットを並べるのに十分かつ最小のサイズに設定
        self.root.update_idletasks()
        self.root.minsize(self.root.winfo_width() + 20, self.root.winfo_height() + 20)

    def create_and_layout_widgets(self):
        # フォームフレームの作成
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=10, pady=5, fill='x')
        form_frame.grid_columnconfigure(0, weight=0)
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(2, weight=0)
        
        # Input vvprojセクション
        tk.Label(form_frame, text="Input vvproj", anchor='e', width=15).grid(row=0, column=0, padx=5)
        self.input_entry = tk.Entry(form_frame, width=self.column_width)
        self.input_entry.insert(0, "zundamon.vvproj")
        self.input_entry.grid(row=0, column=1, padx=5, sticky='w')
        self.input_button = tk.Button(form_frame, text="Select", width=10)
        self.input_button.grid(row=0, column=2)

        # Output vvprojセクション
        tk.Label(form_frame, text="Output vvproj", anchor='e', width=15).grid(row=1, column=0, padx=5)
        self.output_entry = tk.Entry(form_frame, width=self.column_width)
        self.output_entry.insert(0, "zundamon_ezrapper.vvproj")
        self.output_entry.grid(row=1, column=1, padx=5, sticky='w')
        self.output_button = tk.Button(form_frame, text="Select", width=10)
        self.output_button.grid(row=1, column=2)

        # BPMセクション
        tk.Label(form_frame, text="BPM", anchor='e', width=15).grid(row=2, column=0, padx=5)
        self.bpm_entry = tk.Entry(form_frame, width=self.bpm_width)
        self.bpm_entry.insert(0, "120")
        self.bpm_entry.grid(row=2, column=1, padx=5, sticky='w')

        # プログレスバー用フレームの作成
        progress_frame = tk.Frame(self.root)
        progress_frame.pack(padx=10, pady=10, fill='x')
        self.progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(fill='x')

        # 横線
        ttk.Separator(self.root, orient='horizontal').pack(fill='x')

        # ボタンフレームの作成
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20, fill='x')
        self.generate_button = tk.Button(button_frame, text="Generate")
        self.generate_button.pack(side=tk.LEFT, padx=10)
        self.save_button = tk.Button(button_frame, text="Save")
        self.save_button.pack(side=tk.LEFT)
        self.exit_button = tk.Button(button_frame, text="Exit")
        self.exit_button.pack(side=tk.RIGHT, padx=10)

    def bind_events(self):
        # ボタンにコールバックをバインド
        self.generate_button.config(command=self.callbacks.on_generate)
        self.save_button.config(command=self.callbacks.on_save)
        self.input_button.config(command=self.callbacks.on_select_input)
        self.output_button.config(command=self.callbacks.on_select_output)
        self.exit_button.config(command=self.callbacks.on_exit)

    def run(self):
        self.root.mainloop()

# アプリケーションの実行
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()
