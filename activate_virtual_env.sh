python3 -m venv .venv
source .venv/bin/activate

echo "Starting mkdocs serve"
echo "Don't forget to deploy GitHub"
echo "mkdocs serve -a 127.0.0.1:8001"
cd python-cheatsheet
mkdocs serve -a 127.0.0.1:8001