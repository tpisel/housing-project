# securely persists the credentials for later access so we don't need to ask again

import os
import keyring

# retrieve keys exported from the bash script
PLANNINGALERTSKEY = os.environ['PLANNINGALERTSKEY']
PGPASSWORD = os.environ['PGPASSWORD']

print('\nSaving credentials on the local keychain')

keyring.set_password('planning_alerts', 'api_key', PLANNINGALERTSKEY)
keyring.set_password('postgresql', 'postgres', PGPASSWORD)
