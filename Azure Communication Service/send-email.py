import os
from azure.communication.email import EmailClient,EmailContent,EmailAddress,EmailRecipients,EmailMessage

try:
    # Create the EmailClient object that you use to send Email messages.
    email_client =EmailClient.from_connection_string("endpoint=<ENDPOINT URL>;accesskey=<ACCESS KEY>")
    content = EmailContent(subject="Welcome to Azure Communication Services Email",plain_text="This email message is sent from Azure Communication Services Email using the Python SDK.",)

    address = EmailAddress(email="<TO Email ID>")
    recipient = EmailRecipients(to=[address])

    message = EmailMessage(
                sender="<FROM ID>",
                content=content,
                recipients=recipient
            )

    response = email_client.send(message)

# Quickstart code goes here.
except Exception as ex:
    print('Exception:')
    print(ex)