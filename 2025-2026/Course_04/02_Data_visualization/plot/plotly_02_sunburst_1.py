import plotly.express as px 
import pandas as pd

data = pd.DataFrame({
    "category": ["Electronics", "Electronics", "Clothing", "Clothing"], 
    "subcategory": ["Mobiles", "Laptops", "Men", "Women"], 
    "value": [40, 30, 20, 10]
})

fig = px.sunburst( 
                data, 
                path=['category', 'subcategory' ], 
                values='value',
                title= "Sales Distribution by Category"
)

fig.show()