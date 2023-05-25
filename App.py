import tkinter as tk
from tkinter import ttk
from typing import Union, List, Dict

from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy


class App(ttk.Frame):
    def __init__(self, parent, config: List[Dict]):
        ttk.Frame.__init__(self)

        # Make the app responsive
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=0)
        self.rowconfigure(index=1, weight=1)

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=0)
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets(config)

    def load_tree(self, data: Union[DataFrame, DataFrameGroupBy], title: str):
        def insert_group(item_id: int, title, values):
            self.treeview.insert(parent='', index='end', iid=item_id, text=title, values=values)
            self.treeview.item(item_id, open=False)
    
        def insert_line(item_id: int, values: list, group=''):            
            self.treeview.insert(parent=group, index='end', iid=item_id, text=values[0], values=values[1:])

        # Get information about DataFrame
        # -------------------------------
        # Type
        tipo = type(data)

        # Number of Columns
        if tipo == DataFrame: n_columns: int = data.shape[1] + 1
        else: n_columns: int = data.get_group(list(data.groups.keys())[0]).shape[1] + 1

        # Columns Names
        if tipo == DataFrame: columns = data.columns
        else: columns = data.get_group(list(data.groups.keys())[0]).columns
        # -------------------------------

        # Clear TreeView if exist
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Set the number of columns in the TreeView
        self.treeview.config(columns=tuple(range(1, n_columns)))

        # Treeview columns and headings
        self.treeview.column('#0', anchor='center', width=100)
        self.treeview.heading('#0', text="ID", anchor='center')
        for i in range(1, n_columns):
            self.treeview.column(i, anchor='w', width=120)
            self.treeview.heading(i, text=columns[i-1], anchor='center')

        # Insert TreeView data
        item_id = 1
        if tipo == DataFrame:
            # Add Lines
            for record in data.itertuples():
                record = list(record)
                insert_line(item_id, record)
                item_id += 1
                
        elif tipo == DataFrameGroupBy:
            for group in data.groups.keys():
                data_group = data.get_group(group)
                
                # Add Group
                insert_group(item_id, group, ['-~-' for i in range(n_columns - 1)])
                group_id = item_id
                item_id += 1
                
                # Add Lines
                for record in data_group.itertuples():
                    record = list(record)
                    insert_line(item_id, record, group_id)
                    item_id += 1
        
        # Update the Title
        self.label.config(text = title)

    def setup_widgets(self, config: List[Dict]):
        # Frame for Title
        self.title = tk.Frame(self)
        self.title.grid(row=0, column=0, sticky=tk.NW, padx=19, pady=(10,1))

        # Label
        self.label = tk.Label(self.title, text='Select a DataFrame', font=('Segoe UI Black', 11))
        self.label.grid()

        # Panedwindow
        self.paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            height=15
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Radio Buttons, pane #2
        self.pane_2 = ttk.LabelFrame(self.paned, padding=5, text=" Query Options ")
        self.paned.add(self.pane_2, weight=0)

        # Function RadioButtons
        update_tree_function = lambda: self.load_tree(
            config[self.var_3.get()-1]['DataFrame'], config[self.var_3.get()-1]['name']
        )

        # Radiobuttons
        for i in range(len(config)):
            option = config[i]
            self.radio_1 = ttk.Radiobutton(
                self.pane_2, text=option['name'], variable=self.var_3, value=i+1, command=update_tree_function
            )
            self.radio_1.grid(row=i, column=0, padx=15, pady=10, sticky="nsew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

    @staticmethod
    def initialize(config: List[Dict], win_size: tuple=None, theme: bool = False):
        root = tk.Tk()
        root.title("Pandas Data Visualization")

        # Simply set the theme
        if theme:
            path = "C:\\Users\\user_name\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\tkinter\\themes\\Azure-ttk-theme-main\\azure.tcl"
            root.tk.call("source", path)
            root.tk.call("set_theme", "dark")

        app = App(root, config)
        app.pack(fill="both", expand=True)

        # Set a minsize for the window, and place it in the middle
        root.update()
        if not win_size:
            h_size = root.winfo_width()
            v_size = root.winfo_height()
        else:
            h_size = win_size[0]
            v_size = win_size[1]
        # end if

        root.minsize(h_size, v_size)
        x_cordinate = int((root.winfo_screenwidth() / 2) - (h_size / 2))
        y_cordinate = int((root.winfo_screenheight() / 2) - (v_size / 2) - 50)
        root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

        root.mainloop()

if __name__ == '__main__':
    import pandas as pd

    # Load sample Data and Create a Column
    df = pd.util.testing.makeDataFrame()
    df.loc[df.A >= 0, 'div'] = 'div1'
    df.loc[df.A < 0, 'div'] = 'div2'
    df_group = df.groupby('div')

    # List of Settings
    df = {'name': 'df', "DataFrame": df}
    df_groupby = {'name': 'df GroupBy Div Column', "DataFrame": df_group}
    List = [df, df_groupby]

    # Initialization
    App.initialize(List, win_size=(1000, 450), theme=False)
