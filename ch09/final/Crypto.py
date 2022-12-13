import requests

class CryptoAPI:
  def __init__(self, coin_id = 'bitcoin'):
    '''
    sets up crypto api class
    args: self: current instance 
          currency: desired currency
    
    '''
    self.api_url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'

  def get(self):
    r = requests.get(self.api_url)
    response = r.json()
    
    if(response["market_data"]["current_price"]["usd"]):
       return response["market_data"]["current_price"]["usd"]
    
    else:
        return None
    

  def print_supported_crypto():
    '''
    prints list of supported crypto and their corresponding IDs
    args: None
    returns: None
    '''
    print("THESE ARE THE SUPPORTED USER INPUTS:\n")
    print("\nCoin Name:               ID:")
    print("\nBitcoin:                 bitcoin")
    print("\nEtherium:                etherium")
    print("\nTether:                  tether")
    print("\nUSD Coin:                usd-coin")
    print("\nXRP:                     ripple")
    print("\nCardano:                 cardano")
    print("\nSolana:                  solana")
    print("\nPolkadot:                polkadot\n\n\n")
  def __str__(self):
    '''
    create a string representation of the class
    args: self: current instance
    return: (str) of API url
    '''
    return self.api_url