"""
Primetrade.ai Data Science Assignment
Author: [Your Name]
Description: Analysis of Hyperliquid trader performance against Bitcoin Market Sentiment.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- SECTION 1: DATA CLEANING & ALIGNMENT ---
def load_and_clean():
    print("Loading datasets...")
    fg = pd.read_csv('fear_greed_index.csv')
    hist = pd.read_csv('historical_data.csv')
    
    # Standardize dates
    fg['date'] = pd.to_datetime(fg['date']).dt.date
    hist['date'] = pd.to_datetime(hist['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce').dt.date
    
    # Daily aggregation
    daily = hist.groupby(['Account', 'date']).agg(
        daily_pnl=('Closed PnL', 'sum'),
        vol=('Size USD', 'sum'),
        trades=('Trade ID', 'count'),
        bias=('Side', lambda x: x.map({'BUY': 1, 'SELL': -1}).mean())
    ).reset_index()
    
    # Calculate Win Rate
    win_rate = hist.groupby(['Account', 'date']).apply(
        lambda x: (x['Closed PnL'] > 0).sum() / len(x[x['Closed PnL'] != 0]) if len(x[x['Closed PnL'] != 0]) > 0 else 0
    ).reset_index(name='win_rate')
    
    df = pd.merge(daily, win_rate, on=['Account', 'date'])
    df = pd.merge(df, fg[['date', 'classification', 'value']], on='date')
    
    # Segmentation (Part B)
    q3_vol = df['vol'].quantile(0.75)
    df['segment'] = np.where(df['vol'] > q3_vol, 'Whale', 'Retail')
    
    return df

# --- SECTION 2: STRATEGY & RULES OF THUMB ---
def apply_rules_of_thumb(df):
    # Rule 1: Extreme Fear Mitigation for Retail
    df['strategy_signal'] = 'HOLD'
    df.loc[(df['segment'] == 'Retail') & (df['classification'] == 'Extreme Fear'), 'strategy_signal'] = 'REDUCE_SIZE'
    
    # Rule 2: Whale Momentum following in Fear
    df.loc[(df['segment'] == 'Whale') & (df['classification'] == 'Fear'), 'strategy_signal'] = 'ACCUMULATE'
    return df

# --- SECTION 3: EXECUTION & VISUALIZATION ---
if __name__ == "__main__":
    final_df = load_and_clean()
    final_df = apply_rules_of_thumb(final_df)
    
    # Save the final table for the recruiter
    final_df.to_csv('processed_results.csv', index=False)
    
    # Create the mandatory plots
    plt.figure(figsize=(10, 5))
    sns.barplot(data=final_df, x='classification', y='daily_pnl', hue='segment', 
                order=['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed'])
    plt.title('PnL Performance vs Market Sentiment')
    plt.savefig('sentiment_pnl_chart.png')
    
    print("Project executed successfully. Files 'processed_results.csv' and 'sentiment_pnl_chart.png' created.")