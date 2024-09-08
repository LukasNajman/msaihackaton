import dataclasses
import os
from dotenv import load_dotenv

load_dotenv()


@dataclasses.dataclass
class Configuration:
    oai_azure_endpoint = os.environ["OAI_AZURE_ENDPOINT"]
    oai_azure_deployment_chat = os.environ["OAI_AZURE_DEPLOYMENT_CHAT"]
    oai_azure_deployment_embedding = os.environ["OAI_AZURE_DEPLOYMENT_EMBEDDING"]
    oai_api_version = os.environ["OAI_API_VERSION"]
    oai_api_key = os.environ["OAI_API_KEY"]

    adi_endpoint = os.environ["ADI_ENDPOINT"]
    adi_key = os.environ["ADI_KEY"]

    pg_host = os.environ["PG_HOST"]
    pg_port = int(os.environ["PG_PORT"])
    pg_user = os.environ["PG_USER"]
    pg_password = os.environ["PG_PASSWORD"]
    pg_database = os.environ["PG_DATABASE"]


_configuration = Configuration()


def get_configuration():
    return _configuration
