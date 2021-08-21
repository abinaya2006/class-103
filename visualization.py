import pandas as pd
import plotly.express as px
# df=pd.read_csv("line_chart.csv")

df=pd.read_csv("data.csv")
# fig=px.line(df,x="Year",y="Per capita income",color="Country",title="Per capita income")--line chart.csv
# fig=px.bar(df,x="Country",y="InternetUsers",title="Internet Users")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=30,hover_name="Country",hover_data=["Country","Percentage"])
fig.show()



