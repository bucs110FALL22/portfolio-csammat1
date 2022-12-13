from Crypto import CryptoAPI
from Currency import CurrencyAPI

def getCurrency():
  '''
  collects desired currency from user
  args: none
  return: (str) desired currency
  '''  
  loop = True
  user_input = ""
    
  while(loop): 
        
    user_input = input('What is the id of your desired currency?\n(Type HELP for a list of supported currencies)\n\n')
    
    if(user_input.lower() == "help"):
      CurrencyAPI.print_supported_currency()  
                  
    else:
      loop = False
            
  return user_input
    
def getCrypto():
  '''
  collects desired crypto from user
  args: none
  return: (str) desired crypto
  '''    
  loop = True
  user_input = ""
    
  while(loop): 
        
    user_input = input('What is the id of your desired cryptocurrency?\n(Type HELP for a list of supported currencies)\n\n')
    
    if(user_input.lower() == "help"):
      CryptoAPI.print_supported_crypto()
                
    else:
      loop = False
            
  return user_input


def main():       
  try:
    currency = getCurrency()
    crypto = getCrypto()
    currencyAPI = CurrencyAPI(currency)
    exchange_rate = currencyAPI.get()
    cryptoAPI = CryptoAPI(crypto)
    crypto_price = cryptoAPI.get()
    final_price = crypto_price*exchange_rate
    print(str(final_price)+' '+ str(currency))
  except:
    print('Uh oh, check spelling an try again. Use help if you need a list of acceptable currancies and cryptos.\n')
    main()
main()
