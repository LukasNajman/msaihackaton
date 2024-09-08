from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

from configuration import get_configuration

config = get_configuration()

_di_client = DocumentIntelligenceClient(
    endpoint=config.adi_endpoint,
    credential=AzureKeyCredential(config.adi_key)
)

def get_document_intelligence_client() -> DocumentIntelligenceClient:
    return _di_client