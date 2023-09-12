from config import endpoints
import keyring
import os

PLANNINGALERTSKEY = os.environ['PLANNINGALERTSKEY']
PGPASSWORD = os.environ['PGPASSWORD']

print(PGPASSWORD)
print(PLANNINGALERTSKEY)

# add transforms etc