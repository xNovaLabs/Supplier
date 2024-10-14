from typing import Optional
import discord
from discord import app_commands
from dotenv import load_dotenv
import json

import os
import random

load_dotenv()


MY_GUILD = discord.Object(id=os.getenv("DISCORD_GUILD_ID"))  


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


class LinkPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=os.getenv("DISCORD_BUTTON_NAME"), style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        present = False
        x = False
        with open('data.json', "r") as f:
            data = json.load(f)

        with open("links.txt", "r") as f:
            links = f.readlines()

        link = random.choice(links)

        for entry in data:
            if entry['id'] == interaction.user.id:
                present = True
                if entry['requests'] != 0:
                    entry['requests'] -= 1
                    embedx = discord.Embed(title="Link Delivery",
                      description="Your requested link is below.",
                      colour=0x165bfe)

                    embedx.set_author(name=os.getenv("DISCORD_BOT_NAME"),
                                    url=os.getenv("DISCORD_BOT_URL"),
                                    icon_url=os.getenv("DISCORD_ICON_URL"))

                    embedx.add_field(name="Link",
                                    value=link,
                                    inline=False)
                    embedx.add_field(name="Requests Remaining",
                                    value=entry['requests'],
                                    inline=False)
                    await interaction.user.send(embed=embedx)
                    with open('data.json', "w") as f:
                        json.dump(data, f)
                    x = True
                    await interaction.response.send_message('Link delivered. Check your DMs.', ephemeral=True)


        if not present:
            new = {
                "id": interaction.user.id,
                "requests": 3
            }
            data.append(new)


            for entry in data:
                if entry['id'] == interaction.user.id:
                    present = True
                    if entry['requests'] != 0:
                        entry['requests'] -= 1
                        embedx = discord.Embed(title="Link Delivery",
                        description="Your requested link is below.",
                        colour=0x165bfe)

                        embedx.set_author(name=os.getenv("DISCORD_BOT_NAME"),
                                        url=os.getenv("DISCORD_BOT_URL"),
                                        icon_url=os.getenv("DISCORD_ICON_URL"))

                        embedx.add_field(name="Link",
                                        value=link,
                                        inline=False)
                        embedx.add_field(name="Requests Remaining",
                                        value=entry['requests'],
                                        inline=False)
                        await interaction.user.send(embed=embedx)
                        with open('data.json', "w") as f:
                            json.dump(data, f)
                        x = True
                        await interaction.response.send_message('Link delivered. Check your DMs.', ephemeral=True)
            

        if not x:
            await interaction.response.send_message('You are out of requests.', ephemeral=True)


    @discord.ui.button(label="Lucid (Subdomains)", style=discord.ButtonStyle.gray, custom_id='persistent_view:gray')
    async def gray(self, interaction: discord.Interaction, button: discord.ui.Button):
        present = False
        x = False
        with open('freednsdata.json', "r") as f:
            data = json.load(f)

        with open("freednslinks.txt", "r") as f:
            links = f.readlines()

        link = random.choice(links)

        for entry in data:
            if entry['id'] == interaction.user.id:
                present = True
                if entry['requests'] != 0:
                    entry['requests'] -= 1
                    embedx = discord.Embed(title="Link Delivery",
                      description="Your requested link is below.",
                      colour=0x165bfe)

                    embedx.set_author(name=os.getenv("DISCORD_BOT_NAME"),
                                    url=os.getenv("DISCORD_BOT_URL"),
                                    icon_url=os.getenv("DISCORD_ICON_URL"))

                    embedx.add_field(name="Link",
                                    value=link,
                                    inline=False)
                    embedx.add_field(name="Requests Remaining",
                                    value=entry['requests'],
                                    inline=False)
                    await interaction.user.send(embed=embedx)
                    with open('freednsdata.json', "w") as f:
                        json.dump(data, f)
                    x = True
                    await interaction.response.send_message('Link delivered. Check your DMs.', ephemeral=True)


        if not present:
            new = {
                "id": interaction.user.id,
                "requests": 6
            }
            data.append(new)


            for entry in data:
                if entry['id'] == interaction.user.id:
                    present = True
                    if entry['requests'] != 0:
                        entry['requests'] -= 1
                        embedx = discord.Embed(title="Link Delivery",
                        description="Your requested link is below.",
                        colour=0x165bfe)

                        embedx.set_author(name=os.getenv("DISCORD_BOT_NAME"),
                                        url=os.getenv("DISCORD_BOT_URL"),
                                        icon_url=os.getenv("DISCORD_ICON_URL"))

                        embedx.add_field(name="Link",
                                        value=link,
                                        inline=False)
                        embedx.add_field(name="Requests Remaining",
                                        value=entry['requests'],
                                        inline=False)
                        await interaction.user.send(embed=embedx)
                        with open('freednsdata.json', "w") as f:
                            json.dump(data, f)
                        x = True
                        await interaction.response.send_message('Link delivered. Check your DMs.', ephemeral=True)
            

        if not x:
            await interaction.response.send_message('You are out of requests.', ephemeral=True)
        

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print("a nova labs project.")
    print("for support. make an issue on github. https://github.com/xNovaLabs")
    print('------')

@client.tree.command()
async def panel(interaction: discord.Interaction):
    embed = discord.Embed(title="Link Panel",
                      description="This is the official NovaLabs link panel. Here you can receive up to 3 standalone links per month & 6 subdomain links per month. To receive additional link requests, please boost the server or become a donator. Please have your DMs turned on to recieve the links, otherwise you will not recieve any. Please make a ticket if you have any bugs.",
                      colour=0x165bfe)

    embed.set_author(name=os.getenv("DISCORD_BOT_NAME"),
                    url=os.getenv("DISCORD_BOT_URL"),
                    icon_url=os.getenv("DISCORD_ICON_URL"))
    await interaction.response.send_message(embed=embed, view=LinkPanel())

client.run(os.getenv("DISCORD_TOKEN"))