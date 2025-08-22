import asyncio

from src.PlatformClient import PlatformClient
from src.PlatformClient import UserAccess
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    branch = client.GetBranch(Creds.BRANCH_ID)

    new_api = await branch.API.Create("test new", [UserAccess.CreateTests])

    print(new_api.status, new_api.json())

asyncio.run(main())