from flask import Flask, request
import json
import run_command

app = Flask(__name__)
f = open('settings.json')
settings = json.load(f)

@app.route('/', methods=['POST'])
def main():
   data = request.json
   dataGeneral = parseData(data)
   if dataGeneral == 0:
      print("Something is wrong!")
      print(data)
      return ('failed', 500)

   print("data from ", dataGeneral['platform'])
   print("data : ", dataGeneral)

   for v in settings:
      if dataGeneral['nominal'] >= v['min_amount']:
         for cmd in v['allowedCommand']:
            if cmd.lower() in dataGeneral['message'].lower():
               print("Menjalankan command : ", cmd)
               run_command.runCmd(cmd)
   return ('success', 200)

def parseData(data):
   result = {}
   if 'supporter_name' in data and data['type'] == 'tip':
      result['platform'] = 'trakteer'
      result['nominal'] = data['quantity'] * data['price']
      result['message'] = data['supporter_message']
   elif 'donator_name' in data and data['type'] == 'donation':
      result['platform'] = 'saweria'
      result['nominal'] = data['amount_raw']
      result['message'] = data['message']
   elif 'supporter' in data and 'email_supporter' in data:
      result['platform'] = 'Sociabuzzz'
      result['nominal'] = data['amount']
      result['message'] = data['message']
   else:
      return 0
   return result


app.run(host='localhost', port='8080')