from preswald import query,table,text,plotly
import plotly.express as px

sql_query="""
    SELECT
        Random,
        COUNT(*) as record_count
    FROM 'data/green.csv'
    GROUP BY Random
"""
count=query(sql_query,'data/green.csv')

text("# RANDOM COUNT TABLE")
table(count)

text("# PLOT")
fig=px.bar(count,x='Random',y='record_count')
plotly(fig)