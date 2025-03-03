from os import times_result

from discord.ext import commands

from tokens import get_token
import requests
import json
import discord
import os

TOKEN = get_token()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

def get_time(zone, capital):
    time_url = f"https://www.timeapi.io/api/time/current/zone?timeZone={zone}%2F{capital}"
    request = requests.get(time_url).json()
    return ("Anul: " + str(request["year"]) + '\n'+
           "Luna: " + str(request["month"]) + '\n' +
           "Ziua: " + str(request["day"]) + '\n' +
           "Ora: " + str(request["hour"]) + '\n' +
           "Minutul: " + str(request["minute"]) + '\n' +
           "Secunda: " + str(request["seconds"]) + '\n' +
           "Data: " + str(request["date"]) + '\n' +
           "Ziua saptamanii: " + str(request["dayOfWeek"]))

def get_weather(city):
    API_KEY = "d86849ece05b82df5630755bcde58762"
    weather_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
    weather = dict(requests.get(weather_url).json())
    list_weather = [(k, v) for k, v in weather.items()]
    return list_weather


@client.event
async def on_ready():
    print(f"We are now logged in {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        await message.channel.send("Hello!")

    elif message.content.startswith('!time'):
        parts = message.content.split('-')

        time_result = "U need to tell the zone and captial"

        if len(parts) >= 3:
            param1 = parts[1]
            param2 = parts[2]
            time_result = get_time(param1, param2)

        await message.channel.send(time_result)

    elif message.content.startswith('!weather'):
        parts = message.content.split('-')

        dict_weather = "U need to tell the city"

        if len(parts) >= 2:
            param = parts[1]
            dict_weather = f"```\n{dict(get_weather(param))}\n```"

        await message.channel.send(dict_weather)

client.run(TOKEN)
