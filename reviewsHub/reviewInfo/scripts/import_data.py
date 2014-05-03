import json
import os

from reviewInfo.models import ReviewInfo

REPO_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
FILE_NAME = os.path.join(REPO_DIR,'data.json')

count = 0.0

with open(FILE_NAME) as f:
    records = json.load(f)
    for record in records:
        
        count += 1.0
        print(count/len(records))

        sku = record['sku']
        rating = record['rating']
        title = record['title']
        comment = record['comment']
        time = record['submissionTime']
        reviewer = record['reviewer'][0]['name']
        r = ReviewInfo(sku=sku, rating=rating, title=title, comment=comment,
            submissionTime=time, reviewer=reviewer)
        r.save()


