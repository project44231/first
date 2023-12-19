import os
#KEYVAULT SERVICE PRINCIPAL
os.environ["AZURE_CLT_ID"] = "e284ef73-1755-42b3-bca5-fa66d7b6ae39"
os.environ["AZURE_TENT_ID"] = "bf783e90-46a3-4656-baf8-86badf306424"
os.environ["AZURE_CLT_SEC"] = "k-r8Q~9Iv.S7VOGTfs4ZYoMzJbr2UTo3rGxzndia"

#KEYVAULT URL
os.environ["AZURE_VAULT_URL"] = "https://keyvalult-44231.vault.azure.net/"

#KEYVAULT SECRETS
os.environ["VISION_KEY"] = "ai-vision-key"
os.environ["VISION_ENDPOINT"] = "ai-vision-endpoint"

print(os.environ["AZURE_CLT_ID"])
print(os.environ["AZURE_TENT_ID"])
print(os.environ["AZURE_CLT_SEC"])

print(os.environ["AZURE_VAULT_URL"])
print(os.environ["VISION_KEY"])
print(os.environ["VISION_ENDPOINT"])
