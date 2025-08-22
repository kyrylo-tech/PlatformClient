import asyncio

from src.PlatformClient import PlatformClient
from tests.creds import Credentials as Creds

client = PlatformClient(Creds.API_URL, Creds.API_TOKEN_ID, Creds.API_ACCESS_TOKEN)
client.debug_logs = True

async def main():
    api = client.GetBranch(Creds.BRANCH_ID).GetAPI("0198742f-14f1-7d6a-8579-3d0ee3f5c5d8")

    # change specific variables
    await api.SetVariable("test", "lekkeke")

    # change all variables
    changed = await api.SetVariables([{"name": "test333", "value": "433332"}])
    print("CHANGE ALL", changed.status, changed.json())

    # get all variables
    all_variables = await api.GetVariables()
    print(all_variables.json())



asyncio.run(main())