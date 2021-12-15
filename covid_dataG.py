import pandas as pd
import plotly.express as px

data = pd.read_csv("Copy+of+data+-+data.csv")

g = px.scatter(data, x = 'date', y = 'cases', color='country' )

g.show()