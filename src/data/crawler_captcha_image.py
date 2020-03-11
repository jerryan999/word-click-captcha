import requests
import time
import re

headers = {
    'Referer': 'https://xueqiu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

def _reset_challenge(oldchallenge):
  now = int(time.time()*1000)
  url = "https://api.geetest.com/reset.php?gt=b68f7c51ff1ee91cad5ece5b8a1c9a56&challenge={}&lang=zh-cn&w=rA91v3nX8WBfgHBTSk3xWGIzM00Wsd8KYtdNI1Q(MHtyOKRdTt64gXGRysk35IJpW0uDW(O8z3DJ(b5MvU1J7D4ZKgefXjCVRcvpX4ivcgrbrTUArJK2dDRAHQWgFSO)VjdKkM06x8csermEiukhxWVZpGYYM4(fMaBV5cTHF5UID8Kyy2FwQRPBJ5nciNqRMvoFVmMG1ZqUMObRpIxaplzjc(6bX2c8oRWOBafzEzQ8nROk(CJJZ5xn6FI6fkkolm(ueMG5XSVcr(mtBcrtulda5CFLzNsDnxTjgoMiqZ5wHWUOte3XvyUQIiAYQQG8R2J7vllqUmqfMPOI0iVlO29ZINGlp5pvhJsw842T43xAr6X7BA56KaGsD8AK6fSTaw(Q6UeQCT60Rw965caCKdGrKb6S(f0QI)oMhnAIoZuBm9dahDE12X)kZg2JfyaONhuN0Bj9rvWtNk19wALIl07hK6M2ZiKliPJahzxE83ZM92IUTwtpiYi1LAP8KbIbSaEPSL(x)cBtFxOo2mhBBztdGZlzBgAn6K2qeyCe)9oLWE7yEeKtr9K70dlKfMPMyEYr7uxE6AyWaDLljiOJn(9sdIfQwNguTCXzkh3bIWUlDvoLmWwxXOkh33w41OfdRkWPi1(UcYIVF5qnlJ8d0uLYgepQcNO2FP8sDHy35NqPsgENYcxcnU3c74cvfneCtY70NFB1axwGZIuiQ2DMmbJKom9rGWT3Mybou1DA4c7PTeXrfZwp993vQW4O1ZDtvPihB6GHNzcye4wgJ7i5WsfsAlTHhA4twHWT72xUmHFiLWROTjb1TdnFrmGwdw0PdFXGPDx26T8RDdPuf62ar2U8OQK4z0aMQ3oOV)btRBzBiwS9ezMOqx0VxcWYuiMiOlAQs32)5vRXk0QkypWs6cFOyE5Ae7lq(I5L18kUGa5z))FlYBz0yFkDsto98p9osS)8lYDV96jHBKySRLO(WJF7ZOm8lr(ub4fVcIYgi5IiyDin5gDEbPozTtDyWf4M7x0hdacsT9auNWocQJbMXx4Iy)1jOVhr8(uVLs6e)oKlcdgFkv)GamJ9cwGjlPmPiOK7x0nVR46Gkz85XswoayMzMr3V(ZY8HWpyy5KVVoReHlL5NxW6dvTd631kuLx9uzuMM5UoGTD1X3vATb7)WAvcpoL5dCYL4NA7(hRVrICBMXlIh5a)49)Q)EbsRnmEJuPb2g)bxlWqOW3vwxVvRjoRp1idxGqNkmiQ7yPogFhWluVYo(MhquFqBVHiO6OGurNzoxEx4lHCR8GljF(6Pd4tz(NhvdZstX24uYBynMj4NjzYH5cmMBJJJLibBOFe39ac4df76d3344a79b172d01ffee994ab3184f4fdc4dda7fdbc95234384162ec3829e5e6609ea130a7b852de1873e77282ad34ffef5bb40b2ae8411134f7b4514cc9b5ae83a23d84dd3a2f2b9a8e2aa50ed67dec68f7e34825d613f5c9c793ebf3f9ee307f901c13bb3bcf30e2fc71f34c6dcdabb52e4cec186e3e792238795e&pt=0&callback=geetest_{}".format(oldchallenge,now)
  
  response = requests.get(url, headers=headers)

  c = re.search(r'"challenge": "(.+?)"',response.text).group(1)
  print(response.text) 

  return c

def fill_in_challenge():
  global challenge
  if not challenge or challenge.get('quoto')<=1:
    challenge['challenge'] = _reset_challenge(challenge.get('challenge'))
    challenge['quoto'] = 7
  challenge['quoto']-=1
  print(challenge)
  return challenge

def refresh_get_img_url(challenge):
  now = int(time.time()*1000)
  params = (
      ('gt', 'b68f7c51ff1ee91cad5ece5b8a1c9a56'),
      ('challenge',challenge),
      ('lang', 'zh-cn'),
      ('type', 'click'),
      ('callback', 'geetest_{}'.format(now)),
  )
  response = requests.get('https://api.geetest.com/refresh.php', headers=headers, params=params)
  print(response.text)

  r = re.search(r'pic": "(.+?)"',response.text)
  if r:
    url = "https://resources.geetest.com" +r.group(1)
    return url

def download_img(url):
  if not url:
    return 
  response = requests.get(url)
  if response.status_code == 200:
    name = url.split('/')[-1]
    with open("../images/{}".format(name), 'wb') as f:
      f.write(response.content)

if __name__ == '__main__':
  challenge = {'challenge':'fec9b1177c4dd07a74f3f7cd07b9f2c9',
              'quoto':7}
  for i in range(7):
    challenge = fill_in_challenge()
    img_url = refresh_get_img_url(challenge['challenge'])
    download_img(img_url)
    


