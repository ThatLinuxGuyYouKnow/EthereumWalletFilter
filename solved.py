import pandas as pd

# Load the CSV file
csv_file_path = '/home/alabi-ayobami/Downloads/accounts.csv'
df_wallets = pd.read_csv(csv_file_path)

# Extract wallet addresses from the 'ContractAddress' column
wallet_addresses = df_wallets['Address'].tolist()

# Display the first few wallet addresses to verify extraction
print(wallet_addresses[:5])
import requests
import json
from datetime import datetime, timedelta

# Zerion API key
api_key = "Basic emtfZGV2XzRlMTI1ZWQ2ZDg4NzQ2MTA5ZGFjNTY1OTc0NDE2ZWVkOg=="
headers = {
    'Authorization': api_key
}

# Function to get transaction history
def get_transaction_history(wallet_address):
    url = f"https://api.zerion.io/v1/wallets/{wallet_address}/transactions"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to filter wallets based on the criteria
def filter_wallets(wallet_addresses):
    approved_wallets = []
    now = datetime.utcnow()
    one_day_ago = now - timedelta(days=1)
    
    for wallet in wallet_addresses:
        history = get_transaction_history(wallet)
        if not history:
            continue
        
        transactions = history['data']
        
        # Criteria 1: New Wallets
        creation_time = datetime.strptime(transactions[0]['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        if creation_time < one_day_ago:
            continue
        
        # Criteria 2: Transaction Amount
        received_eth = [tx for tx in transactions if tx['value'] and 0 <= float(tx['value']) <= 5]
        if not received_eth:
            continue
        
        # Criteria 3: Transaction Source
        source_addresses = ['binance', 'bybit', 'mexc']  # Add more sources if needed
        from_exchange = any(source in tx['from_address'] for tx in transactions for source in source_addresses)
        if not from_exchange:
            continue
        
        # Criteria 4 & 5: Outgoing Transactions
        sent_transactions = [tx for tx in transactions if tx['from_address'] == wallet]
        if len(sent_transactions) < 2:
            continue
        
        receiving_wallets = [tx['to_address'] for tx in sent_transactions]
        if any(tx['from_address'] == wallet for tx in transactions if tx['to_address'] in receiving_wallets):
            continue
        
        approved_wallets.append({
            'wallet': wallet,
            'last_transaction_date': transactions[0]['timestamp'],
            'zerion_link': f"https://app.zerion.io/{wallet}/overview",
            'last_transaction_value_eur': received_eth[0]['value']
        })
    
    return approved_wallets

# Filter wallets and save to JSON
approved_wallets = filter_wallets(wallet_addresses)
with open('approved_wallets.json', 'w') as f:
    json.dump(approved_wallets, f, indent=4)

print(f"Approved wallets saved to 'approved_wallets.json'")
