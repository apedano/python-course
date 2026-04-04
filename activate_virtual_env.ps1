py -m venv .venv
.\.venv\Scripts\activate
$env:NO_MKDOCS_2_WARNING = 1
Write-Host "Starting mkdocs serve"
Write-Host "Don't forget to deploy GitHub"
Write-Host "mkdocs serve -a 127.0.0.1:8001"
cd python-science
mkdocs serve -a 127.0.0.1:8001