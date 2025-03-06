import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

# โหลด environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ตั้งค่า intents
intents = discord.Intents.default()
intents.message_content = True  # เปิดให้บอทอ่านข้อความจากแชท

bot = commands.Bot(command_prefix="!", intents=intents)

# รายชื่อที่ใช้สุ่ม
names = [
    "Alter", "Ash", "Ballistic", "Bangalore", "Catalyst", "Caustic", "Conduit",
    "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie",
    "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer",
    "Valkyrie", "Vantage", "Wattson", "Wraith"
]

namesvalo = [
    "Brimstone", "Phoenix", "Breach", "Cypher", "Jett", "Omen", "Phoenix",
    "Raze", "Sage", "Sova", "Viper", "Reyna", "Killjoy", "Skye",
    "Yoru", "Astra", "KAY/O", "Chamber", "Neon", "Harbor", "Gekko",
    "Deadlock", "Iso", "Waylay", "Tejo"
]

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_ready():
    activity = discord.CustomActivity(name="สุ่มApex => !ranapex | สุ่มValorant => !ranvalo")  # Custom Status
    await bot.change_presence(activity=activity)
    print(f"✅ Logged in as {bot.user}")


@bot.command()
async def ranapex(ctx):
    name = random.choice(names)
    await ctx.send(f"🎲  **{name}**")

@bot.command()
async def ranvalo(ctx):
    namevalo = random.choice(namesvalo)
    await ctx.send(f"🎲  **{namevalo}**")

# ตรวจสอบว่ามี Token หรือไม่ก่อนรัน
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERROR: DISCORD_TOKEN not found. Please check your .env file.")
