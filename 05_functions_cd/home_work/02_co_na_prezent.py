import random
gifts = {'gitara': 'sklep muzyczny', 'skok': 'lotnisko', 'rower': 'sklep rowerowy'}
gift_id = random.randint(0,len(gifts) - 1)
print(gift_id)
list_gifts = list(gifts.keys())
gift = list_gifts[gift_id]
print(f"Prezent: {gift} możesz ją kupić w {gifts[gift]}")