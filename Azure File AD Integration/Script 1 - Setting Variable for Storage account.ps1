# Import AzFilesHybrid module
Import-Module -Name AzFilesHybrid

#Connect to Azure Subecription 
Connect-AzAccount

#Define parameters
$SubscriptionId = "<your-subscription-id-here>"
$ResourceGroupName = "<resource-group-name-here>"
$StorageAccountName = "<storage-account-name-here>"
$DomainAccountType = "ComputerAccount" 
$OuDistinguishedName = "<ou-distinguishedname-here>"
$EncryptionType = "<AES256|RC4|AES256,RC4>"
