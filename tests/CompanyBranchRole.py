import asyncio

from src.PlatformClient import PlatformClient
from src.PlatformClient.query_builder import QueryBuilder
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, "01983c93-7660-7eb7-9381-6cc9e8dd6eab", "51052b3d9b2147778b6767f4534ee34b311c9acdc1a64d72b75e1d24cc8198a0")
client.debug_logs = True

async def main():
    branch = client.GetBranch("0938cb91-f780-401a-b18c-f88f34f3fa80")

    query = QueryBuilder().filter(
        property_path="Name",
        value="Технічний",
        compare_type=1
    )

    content = await branch.Roles.GetList(query)

    print(content.status, content.json())

asyncio.run(main())