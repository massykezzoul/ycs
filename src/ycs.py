#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import json


def extract_comments(video_id, youtube_api_key=None, max_response=0):
    # max_response is not already implemented
    if youtube_api_key is None:
        print("You have to give a youtube API key")
        print("See how to get one there : 'https://www.youtube.com/watch?v=pP4zvduVAqo'")

    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_api_key)

    request = youtube.commentThreads().list(
        part="replies,snippet",
        maxResults=100,
        textFormat="plainText",
        videoId=video_id
    )
    response = request.execute()
    items = response['items']

    while 'nextPageToken' in response:
        request = youtube.commentThreads().list(
            part="replies,snippet",
            maxResults=100,
            textFormat="plainText",
            videoId=video_id,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        items = items + response['items']

    return items


def get_api_from_file(file_name='./api.key'):
    # get the API key from a file given by argument
    if not os.path.isfile(file_name):
        if os.path.isfile('./api.key'):
            file_name = './api.key'
        elif os.path.isfile('./src/api.key'):
            file_name = './src/api.key'
        else:
            print("The file "+file_name+" can't be found.")
            print("Please check the location of the file to get the API Key")
            exit(1)

    file = open(file_name, 'r')
    return file.readline()[:-1]


if __name__ == "__main__":
    api_key = get_api_from_file()
    video_id = 'pP4zvduVAqo'  # will be possible to give it by argument
    output_file = 'output.json'  # not implemented yet

    comments = extract_comments(video_id, api_key)

    print(json.dumps(comments))
    print(str(len(comments)) + " Comments extracted.")
