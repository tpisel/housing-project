import keyring

def get_secret(secret):
    match secret:
        case 'planningalerts':
            return keyring.get_password('planning_alerts', 'api_key')
        case 'postgres':
            return keyring.get_password('postgresql', 'postgres')
        case _:
            raise Exception("key not found")


