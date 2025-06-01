from fastapi import FastAPI
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from app.graphql.resolvers import mutation_courses

type_defs = load_schema_from_path("app/graphql/schema.graphql")

schema = make_executable_schema(type_defs, mutation_courses)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
