import requests
import random
import string
import time

URLSEQUENCE = [ 'https://acesso-app-online.tk/cl/bb/pessoa-fisica/session.php', 
                'https://acesso-app-online.tk/cl/bb/pessoa-fisica/session_II.php',
                'https://acesso-app-online.tk/cl/bb/pessoa-fisica/envio.php',
                'https://acesso-app-online.tk/cl/bb/pessoa-fisica/envio_dois.php']

def sendPost(url, payload, cookies):
    r = requests.post(url, data=payload, cookies=cookies)
    return r.status_code

def getSessionId():
    r = requests.get('https://acesso-app-online.tk/cl/bb/pessoa-fisica/')
    return r.cookies['PHPSESSID']

def getRandomPwd():
    return ''.join(random.choice(string.ascii_uppercase) for x in range(2))

def generateData():
    data = {}
    data['agencia'] = random.randint(10000, 99999)
    data['conta'] = str(random.randint(1000,9999999)) + '-' + str(random.randint(0,9))
    data['senha'] = random.randint(1000000,9999999)
    data['btt'] = ''
    data['telefone'] = '(' + str(random.randint(10,99)) + ') ' + str(random.randint(30000, 99999)) + '-' + str(random.randint(1000, 9999))
    data['senhac'] = random.randint(100000, 999999)
    data['cvv'] = random.randint(100,999)
    data['senha1'] = getRandomPwd()
    data['senha2'] = getRandomPwd()
    data['senha3'] = getRandomPwd()

    return data

def startPayloads(data):
    payload1 = {'xmxexlxaxoxaxgx': data['agencia'], 'xmxexlxaxoxcxtx': data['conta'], 'xmxexlxaxoxsx8x': data['senha'], 'btt': data['btt']}
    payload2 = {'xmxexlxaxoxcxlx': data['telefone'], 'xmxexlxaxoxsx6x': data['senhac']}
    payload2.update(payload1)
    payload3 = {'cvv': data['cvv'], 'senha1': '', 'senha2': '', 'senha3': ''}
    payload3.update(payload2)
    payload4 = {'senha1': data['senha1'], 'senha2': data['senha2'], 'senha3': data['senha3'], 'btt': '', 'xmxexlxaxoxaxgx': '', 'xmxexlxaxoxcxtx': '', 'xmxexlxaxoxsx8x': '', 'xmxexlxaxoxcxlx': '', 'xmxexlxaxoxsx6x': ''}

    payloads = [payload1, payload2, payload3, payload4]
    return payloads


def main():
    amount = 500
    count = 0
    while(count < amount):
        sessionId = getSessionId()
        cookies = {'PHPSESSIONID': sessionId}
        data = generateData()
        payloads = startPayloads(data)
        c = 0
        for i in range(0,4):
            c += sendPost(URLSEQUENCE[i], payloads[i], cookies)
        if c < 800:
            print('One of the requests failed. Payload: ')
            print(payloads[i])
        else:
            count += 1
            print('Request completed: [' + str(count) + '/' + str(amount) + ']' )
    print(str(count) + ' Requests completed out of ' + str(amount))

if __name__ == "__main__":
    main()