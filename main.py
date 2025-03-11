from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.types import InputPeerNotifySettings, ChatForbidden
import asyncio

# Your Telegram API credentials
api_id = 28935550  # Your own api_id
api_hash = '00000000000'  # Your own api_hash
phone_number = '+0000000'  # Your phone number write your country code for example (+44)11111111

client = TelegramClient('session_name', api_id, api_hash)


async def disable_notifications_for_channels():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        chat = dialog.entity

        # Skip groups/channels where access is forbidden
        if isinstance(chat, ChatForbidden):
            print(f"[❌] No access: {chat.title}")
            continue

        # Target only channels and supergroups
        if getattr(chat, 'megagroup', False) or getattr(chat, 'broadcast', False):
            print(f"[🔕] Muting notifications: {chat.title}")
            try:
                await client(UpdateNotifySettingsRequest(
                    peer=chat,
                    settings=InputPeerNotifySettings(
                        mute_until=2**31 - 1  # Mute indefinitely
                    )
                ))
                await asyncio.sleep(1)  # Wait 1 second to avoid flood limits
            except Exception as e:
                print(f"[⚠️] Error: {chat.title} -> {e}")


async def main():
    print("[✔️] Logging in...")
    await disable_notifications_for_channels()
    print("[✅] All applicable groups/channels have been muted.")


with client:
    client.loop.run_until_complete(main())
