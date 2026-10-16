"""Bounded provider error details for one existing movie task; no new POST."""
import argparse,re
from seedance_transport import Client,ROOT,read_json
ap=argparse.ArgumentParser();ap.add_argument('--chapter',required=True);args=ap.parse_args()
t=read_json(ROOT/'exports/task-journal.json')['takes'][args.chapter]
client=Client();client.resolve()
result=client.task(task_id=t['task_id'])
error=result.get('error',{})
message=re.sub(r'https?://\S+','[URL]',str(error.get('message','')))[:600]
print({'chapter':args.chapter,'status':result.get('status'),'code':error.get('code'),'message':message})
