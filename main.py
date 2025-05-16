import os
import requests
from prettytable import PrettyTable

# Create folders for each blockchain
folders = {
    'eth': "[01] Ethereum",
    'arb': "[02] Arbitrum",
    'base': "[03] Base",
    'op': "[04] Optimism",
    'bsc': "[05] Binance Smart Chain",
    'uni': "[06] Unichain",
    'sone': "[07] Sonenium",
    'ink': "[08] Ink",
    'pol': "[09] Polygon",
    'abs': "[10] Abstract"
}

for folder in folders.keys():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Blockchain information
blockchains = {
    '1': {
        'name': "Ethereum",
        'explorer': "https://etherscan.io/",
        'api_url': "https://api.etherscan.io/api",
        'api_key': "YourApiKeyToken"  # Replace with actual API key
    },
    '2': {
        'name': "Arbitrum",
        'explorer': "https://arbiscan.io/",
        'api_url': "https://api.arbiscan.io/api",
        'api_key': "YourApiKeyToken"
    },
    # other
}

def display_menu():
    table = PrettyTable()
    table.title = "=====[ TxTracker ]====="
    table.field_names = ["Option", "Blockchain", "Option", "Blockchain"]
    
    # Add rows in two columns
    table.add_row(["[01]", "Ethereum", "[06]", "Unichain"])
    table.add_row(["[02]", "Arbitrum", "[07]", "Sonenium"])
    table.add_row(["[03]", "Base", "[08]", "Ink"])
    table.add_row(["[04]", "Optimism", "[09]", "Polygon"])
    table.add_row(["[05]", "Binance Smart Chain", "[10]", "Abstract"])
    
    print(table)

def get_transaction_count(address, blockchain):
    # This is a mock function - in a real implementation, you'd use the blockchain's API
    # For demonstration, we'll return random numbers
    import random
    total_tx = random.randint(100, 500)
    total_gas = random.uniform(0.1, 10.0)
    total_volume = random.uniform(1.0, 1000.0)
    
    return total_tx, total_gas, total_volume

def main():
    display_menu()
    
    while True:
        choice = input("Choose : ").strip().lower()
        
        # Handle both "01" and "1" format inputs
        if choice in ['01', '1']:
            blockchain = blockchains.get('1')
            folder = 'eth'
        elif choice in ['02', '2']:
            blockchain = blockchains.get('2')
            folder = 'arb'
        elif choice in ['03', '3']:
            blockchain = blockchains.get('3')
            folder = 'base'
        elif choice in ['04', '4']:
            blockchain = blockchains.get('4')
            folder = 'op'
        elif choice in ['05', '5']:
            blockchain = blockchains.get('5')
            folder = 'bsc'
        elif choice in ['06', '6']:
            blockchain = blockchains.get('6')
            folder = 'uni'
        elif choice in ['07', '7']:
            blockchain = blockchains.get('7')
            folder = 'sone'
        elif choice in ['08', '8']:
            blockchain = blockchains.get('8')
            folder = 'ink'
        elif choice in ['09', '9']:
            blockchain = blockchains.get('9')
            folder = 'pol'
        elif choice in ['10', '0']:
            blockchain = blockchains.get('10')
            folder = 'abs'
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if blockchain:
            address = input("Address : ").strip()
            if address:
                total_tx, total_gas, total_volume = get_transaction_count(address, blockchain)
                
                print(f"""
Jumlah tx anda pada jaringan {blockchain['name']} sebanyak {total_tx} tx
Jumlah gas fee yang anda gunakan pada jaringan {blockchain['name']} sebanyak {total_gas:.6f} ETH
Jumlah volume anda pada jaringan {blockchain['name']} sebanyak {total_volume:.6f} ETH
                """)
                
                # Save to the corresponding folder
                with open(f"{folder}/transactions.txt", "a") as f:
                    f.write(f"Address: {address}\n")
                    f.write(f"Transactions: {total_tx}\n")
                    f.write(f"Gas Fee: {total_gas:.6f} ETH\n")
                    f.write(f"Volume: {total_volume:.6f} ETH\n\n")
            else:
                print("Address cannot be empty.")
        else:
            print("Blockchain not supported yet.")

if __name__ == "__main__":
    main()
