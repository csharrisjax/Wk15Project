#!/usr/bin/python

import boto3


#Create an sqs client

sqs = boto3.client('sqs')


#Set the queue name

queue_name = 'sqs_lambda'


#Create a standard sqs queue

response = sqs.create_queue(
    QueueName=queue_name
)

#print the queue URL

print(f" The queue URL is: {response['QueueUrl']}")

