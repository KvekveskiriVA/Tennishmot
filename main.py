import requ
ests
sess = requests.Session()
sess.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
resp = sess.get('https://httpbin.org/cookies')
print(resp.text)
sadsa