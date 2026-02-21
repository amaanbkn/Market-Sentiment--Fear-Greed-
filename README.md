# Trader Performance vs. Market Sentiment Analysis

This project analyzes the relationship between Bitcoin Market Sentiment (Fear & Greed Index) and trader behavior on the Hyperliquid exchange. The goal is to uncover behavioral patterns and propose actionable "Rules of Thumb" for trading strategies.

## 📊 Project Overview
The analysis explores how different categories of traders (Whales vs. Retail) react to market cycles. Key metrics include Daily PnL, Win Rate, Trade Frequency, and Side Bias.

## 🚀 Setup & Installation

###  Prerequisites
Ensure you have Python 3.8+ installed. You will need the following libraries:

pip install pandas numpy matplotlib seaborn scikit-learn



### 🧠 Methodology

Data Cleaning: Standardized IST timestamps to daily dates and handled missing values.

Alignment: Merged trading data with sentiment data using an inner join on the date.

Segmentation: Traders were categorized into Whale (Top 25% by daily volume) and Retail to compare behavioral archetypes.

Strategy Testing: Implemented a logic-based "Strategy Signal" column to evaluate hypothetical risk-mitigation rules.

### 📈 Key Insights
Retail Vulnerability: Retail traders show a significant drop in PnL during "Extreme Fear," often indicating panic-selling behavior.

Whale Stability: Whale accounts maintain higher win rates during high-volatility "Fear" periods, suggesting they provide liquidity to the market.

FOMO Effect: Trading frequency for retail accounts spikes during "Extreme Greed," usually coinciding with sub-optimal entry prices.

### 🛠️ Strategy Recommendations (Rules of Thumb)
Rule 1 (The Defense): Reduce position sizes for Retail-tier accounts by 50% when the Fear & Greed Index is below 20.

Rule 2 (The Follower): In "Greed" regimes, only enter Long positions if the Whale segment's side-bias is positive (Buy Ratio > 0.5).


