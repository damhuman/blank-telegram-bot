import asyncio
import logging

logger = logging.getLogger(__name__)


async def custom_logic_execution():
    pass

loop = asyncio.get_event_loop()
loop.run_until_complete(custom_logic_execution())

