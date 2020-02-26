import boto3
import yaml

polly_client = boto3.Session().client('polly')

config_file = open("config.yml", "r")
config = yaml.load(config_file, Loader=yaml.BaseLoader)

s3_key = input("Key of the file in S3 to generate to: ")
text_file = input("Path of the book file: ")
input_file = open(text_file, "r")

polly_client.start_speech_synthesis_task(
  OutputS3BucketName=config["s3_bucket"],
  OutputS3KeyPrefix=s3_key,
  VoiceId=config["voice_id"],
  OutputFormat=config["output_format"],
  LexiconNames=config["lexicons"],
  Text=input_file.read(),
)

print("Synthesis started...")
