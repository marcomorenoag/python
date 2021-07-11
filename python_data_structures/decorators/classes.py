import requests

class LimitQuery:
  def __init__(self, func) -> None:
    self.func = func
    self.count = 0

  def __call__(self, *args, **kwargs):
      self.limit = args[0]
      if self.count < self.limit:
        self.count += 1
        return self.func(*args, **kwargs)
      else:
        print(f'No queries left. All {self.count} queries used.')
        return

if __name__ == '__main__':
  @LimitQuery
  def get_coun_price(limit):
    '''View the Bitcoin Price Index (BPI)'''
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if url.status_code == 200:
      text = url.json()
      return f"${float(text['bpi']['USD']['rate_float']):.2f}"

  print(get_coun_price(5))
  print(get_coun_price(5))
  print(get_coun_price(5))
  print(get_coun_price(5))
  print(get_coun_price(5))
  print(get_coun_price(5))