import asyncio

from PlatformClient import PlatformClient
from PlatformClient.types import UserAccess
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    branch = client.GetBranch(Creds.BRANCH_ID)

    new_api = await branch.MemberContent.GetAccessGrants("Course", "test new", [UserAccess.CreateTests])

    print(new_api.status, new_api.read())

asyncio.run(main())