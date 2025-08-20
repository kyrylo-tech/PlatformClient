import asyncio

from PlatformClient import PlatformClient
from PlatformClient.query_builder import QueryBuilder
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, "01983c93-7660-7eb7-9381-6cc9e8dd6eab", "51052b3d9b2147778b6767f4534ee34b311c9acdc1a64d72b75e1d24cc8198a0")
client.debug_logs = True

async def main():
    branch = client.GetBranch("0938cb91-f780-401a-b18c-f88f34f3fa80")

    content_query = QueryBuilder().filter(
        property_path="UserId",
        value="01989eae-e516-74cb-8d7f-5320cc274de3",
        compare_type=0,
        invert=False,
        value_null=False
    )

    content = await branch.MemberContent.GetAccessGrants("Course", content_query)

    print(content.status, content.read())

asyncio.run(main())