#!/usr/bin/python

from collections import namedtuple
import requests
import random
import json
import sys
from service import restClient, userService
from config import config
import json

BASE = "api.github.com"
ACCESS_TOKEN = '3324d4c982c60ff33b213d2e76908e73c2e303c5'
PROJECT = 'spring-boot-heroku'
OWNER = 'Diegote58'

class RestClient():
    
    def get(self, uri, headers = None, base = None, access_token = None):

        if not base:
            base = BASE

        if uri.find('?') >= 0:
            accessTokenParam = "&access_token=%s" % (access_token)
        else:
            accessTokenParam = "?access_token=%s" % (access_token)

        uri = "https://%s/%s%s" % (base, uri, accessTokenParam)

        print("uri: %s" % (uri))

        jsonObj = requests.get(uri, headers=headers).json()

    

        return jsonObj

    def post(self, uri, headers = {}):
        jsonObj = requests.post("http://%s" % (uri), headers=headers).json()       
        return jsonObj

    def filterResponse(self, data):
        filters = [
                    {
                        'value': '_links',
                        'replace': 'links'
                    }
                ]

        for element in filters:
            output = data.replace(element['value'], element['replace'])

        return output
    
def getMilestones():
    restClient = RestClient()    
    milestones = restClient.get('repos/%s/%s/milestones' % (OWNER, PROJECT), None, None, ACCESS_TOKEN)
    return milestones

def getPRsFromMilestone(milestoneId):
    restClient = RestClient()    
    pullRequests = restClient.get('repos/%s/%s/issues?milestone=%s&state=all' % (OWNER, PROJECT, milestoneId),None, None, ACCESS_TOKEN)
    return pullRequests

def getPR(id):
    restClient = RestClient()    
    pr = restClient.get('repos/%s/%s/issues/2' % (OWNER, PROJECT), None, None, ACCESS_TOKEN)
    return pr

def assignPR(pr,  account):
    for user in  userService.getUsers():
        if user['account'] == account and user['account'] != pr['user']['login']:
            if len(pr['assignees']) == 0:
                userService.updateUserLoad(account, pr['user'])
                #RestClient().post('https://github.com/%s/%s/pull/%s' % (OWNER, PROJECT, pr['id'], None, None, ACCESS_TOKEN))
                break
            else:
                for assignee in  pr['assignees']:
                    if assignee['login'] != account:
                        userService.updateUserLoad()
                        #RestClient().post('https://github.com/%s/%s/pull/%s' % (OWNER, PROJECT, pr['id'], None, None, ACCESS_TOKEN))
                        break