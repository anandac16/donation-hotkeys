import json

data1 = {'created_at': '2024-09-01T09:41:27+07:00', 'transaction_id': 'test-xxxxxxxx-xxxx-xxxxxxx-xxxxxxxxx', 'type': 'tip', 'supporter_name': '[ Stream Test ]', 'supporter_avatar': 'https://trakteer.id/images/v2/stats-1.png', 'supporter_message': 'Selalu Berkarya', 'media': None, 'unit': 'Milku', 'unit_icon': 'https://trakteer.id/storage/images/units/uic-Vdn9iToeaIKY08iSFPEdUaqOj8paG8z21621508460.png', 'quantity': 1, 'price': 1000, 'net_amount': 950}
data2 = {'version': '2022.01', 'created_at': '2021-01-01T12:00:00+00:00', 'id': '00000000-0000-0000-0000-000000000000', 'type': 'donation', 'amount_raw': 69420, 'cut': 3471, 'donator_name': 'Someguy', 'donator_email': 'someguy@example.com', 'donator_is_user': False, 'message': 'THIS IS A FAKE MESSAGE! HAVE A GOOD ONE', 'etc': {'amount_to_display': 69420}}
data3 = {'id': '9798887788', 'amount': 10000, 'currency': 'IDR', 'amount_settled': 10000, 'currency_settled': 'IDR', 'media_type': '', 'media_url': '', 'supporter': 'Jessica', 'email_supporter': 'jessica@example.com', 'message': 'Ini hanya test notifikasi', 'created_at': '2024-09-01T09:45:44+07:00'}


def checkPlatform(data):
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


f = open('settings.json')
data = json.load(f)

print(checkPlatform(data1))
print(checkPlatform(data2))
print(checkPlatform(data3))

datatest = checkPlatform(data1)

for v in data:
      if datatest['nominal'] >= v['min_amount']:
         print(v['allowedCommand'])