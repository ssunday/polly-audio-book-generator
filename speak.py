import boto3

polly_client = boto3.Session().client('polly')

VOICE_ID = 'Salli'
OUTPUT_FORMAT = 'mp3'

response = polly_client.synthesize_speech(
    VoiceId=VOICE_ID,
    OutputFormat=OUTPUT_FORMAT,
    Text=''
)

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
