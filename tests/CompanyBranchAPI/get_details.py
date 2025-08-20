import asyncio

from PlatformClient import PlatformClient
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)

async def main():
    api = client.GetBranch(Creds.BRANCH_ID).GetAPI(Creds.API_TOKEN_ID)
    api_details = await api.GetDetails()

    print(api_details.status, api_details.read())

asyncio.run(main())