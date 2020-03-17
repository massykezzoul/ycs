#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import json
import argparse


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


def simple_print_comment(comments):
    for comment in comments:
        print(comment['snippet']['topLevelComment']
              ['snippet']['authorDisplayName'] + " commented : '" +
              comment['snippet']['topLevelComment']
              ['snippet']['textDisplay']+"'\n")
        if 'replies' in comment:
            for replie in comment['replies']['comments']:
                print("\t-> "+replie['snippet']['authorDisplayName'] +
                      " replied : '"+replie['snippet']['textDisplay']+"'\n")


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "videoID", help="The ID of the video from which you want to extract the comments.", type=str)
    parser.add_argument(
        "-f", "--output-file", help="An output file, is set to stdout by default.", type=str)
    parser.add_argument(
        "-k", "--api-key", help="your youtube API key, or write it in 'src/api.key'", type=str)
    parser.add_argument(
        "-m", "--max-comments", help="max number of comments to extract.", type=int)
    parser.add_argument("-s", "--simple-comments",
                        help="if given,the script just print the comments in a human-readable format", action="store_true")
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    output_file = ""  # not implemented yet
    args = args()

    video_id = args.videoID
    if args.output_file:
        output_file = args.output_file
    if args.api_key:
        api_key = args.api_key
    else:
        api_key = get_api_from_file()
    if args.max_comments:
        max_comments = args.max_comments
    else:
        max_comments = -1

    comments = ""  # extract_comments(video_id, api_key)

    if args.simple_comments:
        simple_print_comment(comments)
    elif output_file == "":
        # JSON output
        print(json.dumps(comments, indent=4, sort_keys=True))
    # else print to file
