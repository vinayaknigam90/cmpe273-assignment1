# -*- coding: utf-8 -*-
import json
import sys
from github.GithubException import UnknownObjectException
from github import Github


temp = sys.argv[1]
fetch_url=temp.split('//')[1].split('/')
username = fetch_url[1]
repositoryname = fetch_url[2]
print username
print repositoryname
gitobject = Github()
current_user = gitobject.get_user(username)
current_repo = current_user.get_repo(repositoryname)
from flask import Flask
app = Flask(__name__)
@app.route('/v1/<filename>')
def get_File_Contents(filename):
    try:
       fileContent = current_repo.get_file_contents(filename)
       return fileContent.decoded_content
    except UnknownObjectException:
         return "File not found in repository"


@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"
             
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')




