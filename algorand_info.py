from algosdk.v2client import algod

# Connect to a public Algorand node (e.g., AlgoExplorer or similar free API if available, 
# but for this example, we'll just show the setup for a local or specified node).
# Using a common public Testnet node for demonstration.
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

def get_node_status():
    try:
        algod_client = algod.AlgodClient(algod_token, algod_address)
        status = algod_client.status()
        print("Algorand Node Status:")
        print(f"Last Round: {status['last-round']}")
        print(f"Time Since Last Round: {status['time-since-last-round']}")
        print(f"Catchup Time: {status['catchup-time']}")
        print(f"Next Version: {status['next-version']}")
    except Exception as e:
        print(f"Failed to connect to Algorand node: {e}")

if __name__ == "__main__":
    get_node_status()
