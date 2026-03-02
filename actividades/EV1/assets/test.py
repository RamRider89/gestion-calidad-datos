# Libraries
import numpy as np
import pandas as pd
import janitor

# Sample Data curated for this example
company_sales = {
    'SalesMonth': ['Jan', 'Feb', 'Mar', 'April'],
    'Company1': [150.0, 200.0, 300.0, 400.0],
    'Company2': [180.0, 250.0, np.nan, 500.0],
    'Company3': [400.0, 500.0, 600.0, 675.0]
}