import asyncio

from src.PlatformClient import PlatformClient
from src.PlatformClient import UserAccess
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    test_api_id = "019874f7-b62b-7c04-ab59-5abba8118e3d"

    await client.Branch.API.Edit(
        branch_id=Creds.BRANCH_ID,
        api_id=test_api_id,
        new_name="тест  testestset etestst",
        new_access=[UserAccess.ViewTests, UserAccess.CreateTests]
    )

    api_details = await client.Branch.API.GetDetails(
        branch_id=Creds.BRANCH_ID,
        api_id=test_api_id
    )

    print(api_details.status, api_details.read())

asyncio.run(main())