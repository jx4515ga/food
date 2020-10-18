import requests
import os
from pprint import pprint

key = os.environ.get('DRINK_KEY')

url = 'https://api.edamam.com/api/drink/v2/parser?' #ingr=pepsi&
#app_id=2272dc20&app_key=bb5307a190c08e54fe63612f874be4f3


def main():
    drink = get_drink()
    drink_query = get_drink_query(drink)
    drink_info = get_drink_info(drink_query)
    print(f'The drink you just saved: {drink_info} ')

def get_drink():
    drink_search = ''.strip()
    while len(drink_search) == 0 or not drink_search.isalpha():
        drink_search = input('Please enter the name of the drink you wanna see: ')
    return drink_search

#https://api.edamam.com/api/food-database/v2/parser?ingr=pepsi&app_id=2272dc20&app_key=bb5307a190c08e54fe63612f874be4f3

def get_drink_query(drink):
    try:
        query = {'ingr': drink, 'Nutrients': 'CHOCDF', 'ENERC_KCAL': 0, 'FAT': 0, 'apiKey': key}
        response = requests.get(url, params=query).json()
        data = response['results']
        pprint(data)
        return data
    except:
        print('Error with your query. ')

def get_drink_info(drink_data):
    try:
        results = drink_data['nutrients']['edemamSourceUrl']
        return results
    except:
        print('This data is not in the format expected')
        return'Unknown'

if __name__ == '__main__':
    main()

# In addition I've trying to use this following code
#and this what I was asking for. I was using it in an another file


#import requests
#from pprint import pprint

#url = 'https://api.edamam.com/api/food-database/v2/parser?ingr=COLA&app_id=2272dc20&app_key=bb5307a190c08e54fe63612f874be4f3'

#data = requests.get(url).json()

#pprint(data)

#fat = data['parsed']['nutrients']['fat']
#print(f'The cutrients are {fat}')















# drinks (?)

# talk to to the api, return drink info

#def get_drink(search_term):
    #return 'coke'