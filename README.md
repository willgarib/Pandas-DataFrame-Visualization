# Visualização de DataFrames - Pandas

![Screenshot of the App](/screenshot.png)

GUI feita em python com base na biblioteca ```tkinter``` com o tema [**Azure**](https://github.com/rdbende/Azure-ttk-theme) desenvolvido por [@rdbende](https://github.com/rdbende).

O código da aplicação é uma adaptação do exemplo que o prório [@rdbende](https://github.com/rdbende) disponibiliza [aqui](https://github.com/rdbende/Azure-ttk-theme/blob/main/example.py).

A GUI (Interface Gráfica de Usuário) consegue mostrar de maneira mais agradável um DataFrame ou DataFrameGroupBy do ```pandas```.

Para utilizar o tema é preciso que ele esteja instalado em seu computador e que você configure a variável *path* na linha *149* do módulo [*App.py*](/App.py) com o caminho onde voçê salvou o arquivo *azure.tcl*, além de passar o argumento ```theme=True``` do método *inicialize*.

Para iniciar a GUI é necessário criar uma lista de dicionários com as configurações como no exemplo abaixo:

> O caminho (path) que voçê utilizará provavelmente é
> 
> *C:\\Users\user_name\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\tkinter\\themes\\Azure-ttk-theme-main\\azure.tcl*

## Exemplo de Código
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
App.initialize(List, win_size=(1000, 450), theme=True)
```

> [See this text in english](/README_EN.md)
