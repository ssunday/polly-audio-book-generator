import boto3
import os

VOICE_ID = 'Salli'
OUTPUT_FORMAT = 'mp3'
LEXICONS = [
  'races'
]

polly_client = boto3.Session().client('polly')

s3_key = input("Key of the file in S3 to generate to: ")


def synthesize_speech(key, text):
    polly_client.start_speech_synthesis_task(
       OutputS3BucketName=os.environ["S3_BUCKET"],
       OutputS3KeyPrefix=s3_key,
       VoiceId=VOICE_ID,
       OutputFormat=OUTPUT_FORMAT,
       LexiconNames=LEXICONS,
       Text=text,
     )


text_file = input("Path of the book file: ")
input_file = open(text_file, "r")

synthesize_speech(s3_key, input_file.read())
