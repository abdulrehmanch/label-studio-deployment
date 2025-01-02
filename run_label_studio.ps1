# Ensure script execution policy allows running this script
# You may need to run the following command once as an admin:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Change directory to the folder containing this script
Set-Location -Path $PSScriptRoot

# Activate the virtual environment
& .\.venv\Scripts\Activate

#$env:CSRF_TRUSTED_ORIGINS = "https://anno.geosoftsolution.com"
#$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED = true
#$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT = "C:\Users\abdulrehman\PycharmProjects"

#Write-Output "CSRF_TRUSTED_ORIGINS is set to $env:CSRF_TRUSTED_ORIGINS"
label-studio