# TG-UserBot - A modular Telegram UserBot script for Python.
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.


from io import BytesIO
from typing import Union

from telethon.tl.types import Message


async def limit_exceeded(
    event: Message,
    message: str,
    reply: bool = False
) -> Union[Message, None]:
    output = BytesIO(message.strip().encode())
    output.name = "output.txt"
    if reply:
        sent = await event.client.send_file(
            event.chat.id, file=output, reply_to=event
        )
    else:
        sent = await event.client.send_file(
            event.chat.id, file=output
        )
    output.close()
    return sent
