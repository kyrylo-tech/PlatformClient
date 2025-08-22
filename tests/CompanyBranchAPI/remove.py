import asyncio

from src.PlatformClient import PlatformClient
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    branch = client.GetBranch(Creds.BRANCH_ID)

    new_api = await branch.API.Remove("01987520-df40-7f9d-bf97-dd5e7788216f")

    print(new_api.status, new_api.json())

asyncio.run(main())