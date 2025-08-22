from .types import UserAccessType

t = ""

for d in UserAccessType:
    t += f'\n{d} = "{d}"'

print(t)