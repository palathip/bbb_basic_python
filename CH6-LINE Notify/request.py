# -*- coding=utf-8
import requests

def lineNotify():
    show = raw_input("Enter your Massage:")
    url = "https://notify-api.line.me/api/notify"

    payload = "message= %s" %show
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer DozJII5KtXLyajw2iGz3ebKYC0LXY8fVek709idDnTx",
        'cache-control': "no-cache",
        'Postman-Token': "b4c6e079-3401-4919-9a8b-6205e7e524ad"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

lineNotify()