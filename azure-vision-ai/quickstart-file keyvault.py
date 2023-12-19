from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from decouple import config
'''
Authenticate
Authenticates your credentials and creates a client.
'''
"""
subscription_key = os.getenv('VISION_KEY')
#os.environ["VISION_KEY"]
endpoint = os.getenv('VISION_ENDPOINT')
#os.environ["VISION_ENDPOINT"]
"""
# create credential object

tenant_id = config('AZURE_TENT_ID')
client_id = config('AZURE_CLT_ID')
client_secret = config('AZURE_CLT_SEC')
vault_url = config('AZURE_VAULT_URL')
vision_key = config('VISION_KEY')
vision_endpoint = config('VISION_ENDPOINT')

credentials = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
    )

# create a secret client object
secret_client = SecretClient(vault_url=vault_url, credential=credentials)

# get secret value
subscription_key = secret_client.get_secret(vision_key).value
endpoint = secret_client.get_secret(vision_endpoint).value

print(subscription_key)
print(endpoint)



computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text
read_image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(read_image_url,  raw=True)

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()
'''
END - Read File - remote
'''

print("End of Computer Vision quickstart.")