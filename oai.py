from openai import AzureOpenAI
from configuration import get_configuration

config = get_configuration()

_chat_client = AzureOpenAI(
    azure_endpoint=config.oai_azure_endpoint,
    azure_deployment=config.oai_azure_deployment_chat,
    api_version=config.oai_api_version,
    api_key=config.oai_api_key,
)

_embedding_client = AzureOpenAI(
    azure_endpoint=config.oai_azure_endpoint,
    azure_deployment=config.oai_azure_deployment_embedding,
    api_version=config.oai_api_version,
    api_key=config.oai_api_key,
)


def get_chat_client():
    return _chat_client


def get_embedding_client():
    return _embedding_client
