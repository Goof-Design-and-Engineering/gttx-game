from pocketbase import PocketBase
address = 'https://api.gttx.app'
#connect
try:
    unauthed = PocketBase(address)
    authed = PocketBase(address)
    fac = PocketBase(address)
    print("Connected to PocketBase at " + address + ".")
except:
    print("Unable to connect to Pocketbase at " + address + ".")
    exit()

skip_unauthed = False
skip_authed = False
skip_fac = False

#authed
try:
    authed_data = authed.collection("users").auth_with_password("unittestp@gttx.app", "unittestppass")
    print("Authenticated as participant.")
except:
    print("Unable to authenticate as participant. Skipping unit tests for account.")
    skip_authed = True

#fac
try:
    fac_data = fac.collection("users").auth_with_password("unittestf@gttx.app", "unittestfpass")
    print("Authenticated as facilitator.")
except:
    print("Unable to authenticate as facilitator. Skipping unit tests for account.")
    skip_fac = True

if (not skip_unauthed):
    pass

if (not skip_authed):
    pass

if (not skip_fac):
    pass
