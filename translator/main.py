import asyncio
from googletrans import Translator 

async def translate_text():
    async with Translator() as tr:
        s = "Hello, how are you?"
        t = await tr.translate(text = s, src = "en", dest = "ja")
        print(s, t)
        t = await tr.translate(text = s, src = "en", dest = "it")
        print(s, t)

asyncio.run(translate_text())
