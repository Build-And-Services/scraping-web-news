import json, csv
import requests

keyword = ['Air Pollution, sport', 'Air Quaility for, event']
with open("output/result.csv", mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file)
  for key in keyword:
      url = "https://www.taipeitimes.com/ajax_search/200/200?section=all&keywords="+key+"&reportrange=December+31%2C+2018+-+November+29%2C+2023"  # Replace with the actual API URL
      response = requests.get(url)
      if response.status_code == 200:
          api_data = response.text
          json_data = json.loads(api_data)
          for news in json_data:
            encoded_text = news['ar_head'].encode('ascii', 'ignore')
            writer.writerow(['https://www.taipeitimes.com/'+news["ar_url"], encoded_text.decode('ascii'), news["ar_pubdate"], "Report"])
      else:
          print("API request failed.")