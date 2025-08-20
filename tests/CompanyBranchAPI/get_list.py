import asyncio

from PlatformClient import PlatformClient
from PlatformClient.query_builder import QueryBuilder
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    query = (
        QueryBuilder()
        .filter("Name", value="test", compare_type=1)
        .set_count(1)
    )

    api_list = await client.Branch.API.GetList(
        branch_id=Creds.BRANCH_ID,
        filter_query=query
    )

    print(api_list.status, api_list.read())

asyncio.run(main())