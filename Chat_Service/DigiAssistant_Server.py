from google.protobuf.json_format import MessageToJson
import json
import requests


#BEServer = 'http://localhost:8082/'
BEServer = 'http://120.77.158.159:3389/'
def detect_intent_texts(project_id, session_id, texts, language_code):
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)
    print('text_input:')
    print(text_input)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print('query_input:')
    print(query_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    print('response:')
    print(response)
    jsonObj = MessageToJson(response)
    return jsonObj

def act_for_response(queryResponse):
    intentName = json.loads(queryResponse)['queryResult']['intent']['displayName']
    print("intentName:")
    print(intentName)

    action = json.loads(queryResponse)['queryResult']['action']
    print("Action:")
    print(action)

    #ObjectName = json.loads(queryResponse)['queryResult']['parameters']['InsObject']
    #print("ObjectName:")
    #print(ObjectName)
    
    stringResponse=json.loads(queryResponse)['queryResult']['fulfillmentText']
    print("stringResponse:")
    print(stringResponse)
    print(type(json.loads(queryResponse)))

    if action=='PolicyEnquiry':
        result=requests.get(BEServer+'getPolicy/?policy=22222222').text
        #result="Dummy BE result"
        #with open("InsuranceTest.json",encoding='utf-8',errors='ignore') as tweetfile:
        #    print (tweetfile.read())
        #    print (type(tweetfile.read()))
        #    f = json.dumps(tweetfile.read())
        #    print(type(f))
        #    result = json.loads(f, strict=False)
        #    print (result)
        #    print (type(result))
    else:
        #if action=='ObjectEnquiry':
        result=requests.get(BEServer+'getInfo/?question='+stringResponse).text
        #result="Dummy BE result"
        
    print("result:")
    print(result)
    #return action,result.text,stringResponse
    return '{"action":"'+action+'","result":"'+result+'","stringResponse":"'+stringResponse+'"}'
               



