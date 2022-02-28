import requests
import asyncio
import datetime


async def word():
    start = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    url = "https://random-words5.p.rapidapi.com/getRandom"

    headers = {
        'x-rapidapi-host': "random-words5.p.rapidapi.com",
        'x-rapidapi-key': "e676ce5050mshb8e981df8fbaad7p1f125ajsn973a146e2e9e"
    }

    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        finish = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
        data = {"start": start, "finish": finish, "quote": response.text}
        return data


async def quote():
    start = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    url = "https://quotel-quotes.p.rapidapi.com/quotes/random"

    payload = "{}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "quotel-quotes.p.rapidapi.com",
        'x-rapidapi-key': "e676ce5050mshb8e981df8fbaad7p1f125ajsn973a146e2e9e"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        finish = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
        data = {"start": start, "finish": finish, "quote": response.json()['quote']}
        return data


async def kanye():
    start = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    url = "https://api.kanye.rest/"

    headers = {
        'content-type': "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        finish = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
        data = {"start": start, "finish": finish, "quote": response.json()['quote']}
        return data


async def multiple_tasks():
    input_coroutines = [kanye(), word(), quote()]
    res = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return res
