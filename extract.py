import glob
import json

all_file_names = glob.glob('/Users/riff/Downloads/reviews.json/*.json')

select_records = []
sku_list = [9008182, 6238297, 5717547]

count = 0.0

for json_file in all_file_names:
    count += 1.0
    print(count/len(all_file_names))
    with open(json_file) as f:
        all_records = json.load(f)
        for record in all_records:
            if record['sku'] in sku_list:
                select_records.append(record)

with open('data.json', 'w') as outfile:
    json.dump(select_records, outfile, indent=4)
