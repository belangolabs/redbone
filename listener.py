import json
import strawberry

from src.schema import Query


if __name__ == "__main__":

    schema = strawberry.Schema(query=Query)
