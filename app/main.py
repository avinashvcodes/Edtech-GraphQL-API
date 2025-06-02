from fastapi import FastAPI, Depends
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from app.graphql.resolvers.mutations import user_mutation, course_mutation
from app.database import get_db
from fastapi.requests import Request

type_defs = load_schema_from_path("app/graphql/schema.graphql")

schema = make_executable_schema(type_defs, [user_mutation, course_mutation])

app = FastAPI()

# Custom context setup method
def get_context_value(request: Request, _data) -> dict:
    return {
        "request": request,
        "db": request.scope["db"],
    }

# Create GraphQL App instance
graphql_app = GraphQL(
    schema,
    debug=True,
    context_value=get_context_value
)

# Handle GET requests to serve GraphQL explorer
# Handle OPTIONS requests for CORS
@app.get("/graphql/")
@app.options("/graphql/")
async def handle_graphql_explorer(request: Request):
    return await graphql_app.handle_request(request)

# Handle POST requests to execute GraphQL queries
@app.post("/graphql/")
async def handle_graphql_query(
    request: Request,
    db = Depends(get_db)
):
    # Expose database connection to the GraphQL through request's scope
    request.scope["db"] = db
    return await graphql_app.handle_request(request)
