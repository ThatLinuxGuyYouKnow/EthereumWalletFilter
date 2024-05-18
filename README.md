# Wallet Screening with Zerion API

This project was originally developed for a Replit bounty that was cancelled. The goal of this project is to read wallet addresses from a CSV file, screen them using the Zerion API, and apply specific filtering criteria to identify relevant wallets.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Filtering Criteria](#filtering-criteria)
- [Output](#output)
- [License](#license)

## Introduction
This script reads wallet addresses from a CSV file and screens them using the Zerion API. The wallets are filtered based on criteria such as creation time, transaction amount, transaction source, outgoing transactions, and the status of receiving wallets. The filtered results are saved into a JSON file.

## Features
- Extracts wallet addresses from a CSV file.
- Uses Zerion API to retrieve transaction history.
- Applies specific filtering criteria to identify relevant wallets.
- Saves approved wallets into a JSON file with detailed information.

## Prerequisites
- Python 3.6 or higher
- pandas
- requests

## Installation
1. Clone the repository:
    ```bash
    git clone [https://github.com/ThatLinuxGuyYouKnow/EthereumWalletFilter](https://github.com/ThatLinuxGuyYouKnow/EthereumWalletFilter).git
    cd wallet-screening
    ```

2. Install the required Python packages:
    ```bash
    pip install pandas requests
    ```

## Usage
1. Place your CSV file containing wallet addresses in the project directory.
2. Update the `csv_file_path` variable in the script to point to your CSV file.
3. Run the script:
    ```bash
    python wallet_screening.py
    ```

## Filtering Criteria
1. **New Wallets:** Newly created wallets, less than 24 hours old.
2. **Transaction Amount:** Wallets that have received an Ethereum transaction ranging from 0 to 5 ETH.
3. **Transaction Source:** Transactions originating from another wallet or centralized exchanges like Binance, Bybit, MEXC, etc.
4. **Outgoing Transactions:** Monitored wallets should have sent two or more transactions of the same amount to two or more newly created wallets, either manually or through dispersing apps like disperse.app.
5. **No Outgoing Transactions Yet:** The receiving wallets mentioned in point 4 should not have sent any transactions yet; they should have only received Ethereum.

## Output
The script will save the approved wallets into a JSON file named `approved_wallets.json`, containing the following information:
- Wallet address
- Last transaction date and time
- Zerion link
- Last transaction value in EUR

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
