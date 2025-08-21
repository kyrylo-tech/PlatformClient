class QueryBuilder:
    """
        {
            "offset": 0,
            "count": 10,
            "filterQuery": [{
                "properties": [
                    {
                        "propertyPath": "name",
                        "compareType": 1,
                        "invertCompare": False,
                        "value": "Alice",
                        "valueNull": False,
                        "valueBlock": None
                    },
                    {
                        "propertyPath": "age",
                        "compareType": 2,
                        "invertCompare": True,
                        "value": 25,
                        "valueNull": False,
                        "valueBlock": None
                    }
                ]
            }],
            "orderQuery": [
                {
                    "properties": [
                        {"propertyPath": "name", "asc": True},
                        {"propertyPath": "created_at", "asc": False}
                    ]
                }
            ]
        }
    """

    def __init__(self):
        self.offset = 0
        self.count = 10
        self.filters = []
        self.orders = []

    def set_offset(self, offset: int):
        self.offset = offset
        return self

    def set_count(self, count: int):
        self.count = count
        return self

    def filter(
        self,
        property_path: str,
        *,
        compare_type: int = 0,
        value=None,
        invert: bool = False,
        value_null: bool = False,
        value_block=None
    ):
        self.filters.append({
            "PropertyPath": property_path,
            "CompareType": compare_type,
            "InvertCompare": invert,
            "Value": value,
            "ValueNull": value_null,
            "ValueBlock": value_block
        })
        return self

    def order(self, property_path: str, asc: bool = True):
        self.orders.append({
            "PropertyPath": property_path,
            "Asc": asc
        })
        return self

    def build(self):
        return {
            "Offset": self.offset,
            "Count": self.count,
            "FilterQuery": [{"Properties": self.filters}] if self.filters else [],
            "OrderQuery": [{"Properties": self.orders}] if self.orders else [],
        }
