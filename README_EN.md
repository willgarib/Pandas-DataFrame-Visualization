# Pandas DataFrame Visualization

![Screenshot of the App](/screenshot.png)

GUI made in python based on the ```tkinter``` library with the [**Azure**](https://github.com/rdbende/Azure-ttk-theme) theme developed by [@rdbende](https://github.com/rdbende).

The application code is an adaptation of the example provided by *@rdbende* [here](https://github.com/rdbende/Azure-ttk-theme/blob/main/example.py).

The GUI (Graphical User Interface) is able to more nicely display a ```pandas``` DataFrame or DataFrameGroupBy.

To use the theme, it must be installed on your computer and you must configure the *path* variable in line *149* of the [*App.py*](/App.py) module with the path where you saved the file *azure.tcl*, as well as passing the ```theme=True``` argument of the *initialize* method.

To start the GUI it is necessary to create a list of dictionaries with the settings as in the example below:

> The path you will probably use is
>
> *C:\\Users\user_name\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\tkinter\\themes\\Azure-ttk-theme- main\\azure.tcl*

## Code Example
```python
from App import App
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
```
