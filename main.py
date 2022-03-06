import asyncio
from pytgcalls import idle
from config import call_py
from KaalMusic.quote import arq


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @ADI_XD |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
