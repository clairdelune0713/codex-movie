from seedance_transport import Client,ApiFailure
import json,sys
try:
    print(json.dumps(Client().resolve()),flush=True)
except ApiFailure as e:
    print(str(e),file=sys.stderr);sys.exit(1)
except Exception as e:
    print(type(e).__name__+': provider preflight did not complete; no generation submitted',file=sys.stderr);sys.exit(1)
