import pandas as pd
import numpy as np

def load_data():
    """Load all country data and combine"""
    try:
        # Load each country's data
        benin = pd.read_csv('data/benin_clean.csv')
        sierra_leone = pd.read_csv('data/sierra_leone_clean.csv')
        togo = pd.read_csv('data/togo_clean.csv')
        
        # Add country labels (handle case where column might already exist)
        if 'Country' not in benin.columns:
            benin['Country'] = 'Benin'
        if 'Country' not in sierra_leone.columns:
            sierra_leone['Country'] = 'Sierra Leone'
        if 'Country' not in togo.columns:
            togo['Country'] = 'Togo'
        
        # Combine all data
        all_data = pd.concat([benin, sierra_leone, togo], ignore_index=True)
        print(f"Loaded data with columns: {all_data.columns.tolist()}")
        return all_data
        
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def get_country_stats(data, metric):
    """Calculate statistics for selected metric"""
    if data.empty or 'Country' not in data.columns:
        return pd.DataFrame()
    
    stats = data.groupby('Country')[metric].agg([
        'mean', 'median', 'std', 'min', 'max', 'count'
    ]).round(2)
    
    stats.columns = ['Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Count']
    return stats