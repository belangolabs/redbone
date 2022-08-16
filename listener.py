import strawberry

from redbone.schema import Query


if __name__ == "__main__":

    schema = strawberry.Schema(query=Query)
