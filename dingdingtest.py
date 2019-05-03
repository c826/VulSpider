import json, urllib2
def sendDingTalkMessage(title,messageUrl)
    url = "https://oapi.dingtalk.com/robot/send?access_token=6e6b251ed6b41f331651904bf58e30af44943f485e1803ddb3ad599d5840ce12"
    data = {}
    data['msgtype'] = 'link'
    data['link'] = {}
    data['link']['title'] = title
    data['link']['text'] = ''
    data['link']['messageUrl'] = messageUrl
    data = json.dumps(data)
    head = {"Content-Type": "application/json"}
    request = urllib2.Request(url=url, headers=head)
    request.get_method = lambda: "POST"
    httpRes = urllib2.urlopen(request, data)
    content = httpRes.read()
    httpRes.close()
    print content