from azure_document_inteligence import get_document_intelligence_client

if __name__ == '__main__':

    di = get_document_intelligence_client()

    with open("../resources/report.pdf", "rb") as pdf_file:
        poller = di.begin_analyze_document(
            "prebuilt-layout",
            pdf_file,
            content_type="application/octet-stream",
            output_content_format="markdown",
        )
        content = poller.result().content
        print(content)
