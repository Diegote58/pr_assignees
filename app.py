from flask import Flask, render_template, redirect, url_for
from flask_restful import Resource, Api
import json
import routes
from service import userService, restService
import requests

app = Flask(__name__)

#USERS
@app.route('/users')
def getUsers():
    return render_template('user_read.html', users=userService.getUsers())

@app.route('/users')
def createUser():
    userService.updateUser(id)
    return redirect(url_for('users'))

@app.route('/users/<int:id>')
def updateUser(id):
    userService.updateUser(id)
    return redirect(url_for('users'))

#MILESTONES
@app.route('/milestones')
def getMilestones():
    milestones = restService.getMilestones()
    app.logger.info('milestones_read response %s', milestones)
    return render_template('milestones_read.html', milestones=milestones)

@app.route('/milestones/pull_requests/<int:milestoneId>')
def getPrsFromMilestones(milestoneId):
    pullRequests = restService.getPRsFromMilestone(milestoneId)
    app.logger.info('pullRequests response %s', pullRequests)
    return render_template('pull_requests_read.html', pullRequests=pullRequests)

@app.route('/pull_request/<int:id>/assigne/<string:account>')
def assignePR(id, account):
    pr = restService.getPR(id)
    restService.assignPR(pr, account)
    app.logger.info('pullRequests response %s', pr)
    return render_template('user_read.html', users=userService.getUsers())

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=8002)