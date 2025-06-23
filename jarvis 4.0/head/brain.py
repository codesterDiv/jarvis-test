from google.cloud import discoveryengine_v1 as discoveryengine
from google.api_core.client_options import ClientOptions
import ear
def answer_query(project_id: str, location: str, engine_id: str, query_text: str):
    client_options = ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    client = discoveryengine.ConversationalSearchServiceClient(client_options=client_options)

    serving_config = f"projects/jarvis-ai-463813/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.AnswerQueryRequest.Query(text=query_text)
    )

    response = client.answer_query(request)
    return response.answer_text

# Example usage
project_id = "jarvis-ai-463813"
location = "global"
engine_id = "your_engine_id"
query_text = ear.listen()

answer = answer_query(project_id, location, engine_id, query_text)
print(answer)