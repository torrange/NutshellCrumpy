#!/usr/bin/env python2

import requests
import json
import repr

class Nutshell(object):
  response=None

  def __init__(self, user, api_key):
    self.user = user
    self.api_key = api_key
    self.uri = "https://app01.nutshell.com/api/v1/json"
    self.auth=(self.user, self.api_key)

  def add(self, num1, num2):
    self.payload=json.dumps(
        {"method" : "add",
          "params" : [num1, num2],
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteAccount(self, accountid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteAccount",
          "params" : {"accountId" : accountid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteActivity(self, activityid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteActivity",
          "params" : {"activityId" : activityid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteContact(self, contactid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteContact",
          "params" : {"contactId" : contactid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteLead(self, leadid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteLead",
          "params" : {"leadId" : leadid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteNote(self, noteid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteNote",
          "params" : {"noteId" : noteid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteProduct(self, productid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteProduct",
          "params" : {"productId" : productid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteTask(self, taskid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteTask",
          "params" : {"taskId" : taskid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteTeam(self, teamid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteTeam",
          "params" : {"teamId" : teamid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def deleteUser(self, userid, rev=None):
    self.payload=json.dumps(
        {"method" : "deleteUser",
          "params" : {"userId" : userid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editAccount(self, accountid, rev=None,
      name=None, phone=None,
      industryId=None,owner=None,
      note=None, tags=None):
    self.account={}
    if name != None:
      self.account["name"] = name
    if phone != None:
      self.account["phone"] = phone
    if industryId != None:
      self.account["industryId"] = industryId
    if owner != None:
      self.account["owner"] = owner
    if note != None:
      self.account["note"] = note
    if tags != None:
      self.account["tags"] = tags
    self.payload = json.dumps(
        {"method" : "editAccount",
          "params" : {"account":self.account,"accountId" : accountid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editActivity(self, activityId, rev=None,
      name=None, startTime=None, endTime=None,
      activityTypeId=None,participants=None,
      logNote=None, isAllDay=False,
      isFlagged=False, isTimed=False, description=None,
      leads=None,followupTo=None, status=None):
    self.activity={}
    if name != None:
      self.activity["name"] = name
    if startTime!= None:
      self.activity["startTime"] = startTime
    if endTime != None: #maybe some validation here
      self.activity["endTime"]= endTime
    if activityTypeId != None:
      self.activity["activityTypeId"] = activityTypeId
    if participants != None:
      self.activity["participants"] = participants
    if logNote != None:
      self.activity["logNote"] = logNote
    if isAllDay == True:
      self.activity["isAllDay"] = True
    if leads != None:
      self.activity["leads"] = leads
    if followupTo != None:
      self.activity["followupTo"] = followupTo
    if isFlagged == True:
      self.activity["isFlagged"] = True
    if isTimed == True:
      self.activity["isTimed"] = True
    if isinstance(status,(int, long)):
      self.activity["status"] = status
    self.payload = json.dumps(
        {"method" : "editActivity",
          "params" : {"activity":self.activity,"activityId" : activityId, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editContact(self, contactId, rev=None,
      name=None, phone=None,
      owner=None,note=None,
      description=None, tags=None):
    self.contact={}
    if name != None:
      self.contact["name"] = name
    if phone != None: #maybe some validation here
      self.contact["phone"]= phone
    if activityTypeId != None:
      self.contact["owner"] = owner
    if participants != None:
      self.contact["note"] = note
    if description != None:
      self.contact["description"] = description
    if tags != None:
      self.contact["tags"] = tags
    if leads != None:
      sel.contact["leads"] = leads
    self.payload = json.dumps(
        {"method" : "editContact",
          "params" : {"contact":self.contact,"contactId" : contactId, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editLead(self, leadId, rev=None,
      primary_account=None, market=None,
      tags=None,confidence=None,
      assignee=None, contacts=None,
      accounts=None,products=None,
      competitors=None, sources=None,
      note=None, customFields=None):
    self.lead={}
    if primary_account != None:
      self.lead["primary_account"] = primary_account
    if market != None: #maybe some validation here
      self.lead["market"]= market
    if tags != None:
      self.lead["tags"] = tags
    if confidence != None:
      self.lead["confidence"] = confidence
    if assignee != None:
      self.lead["assignee"] = assignee
    if contacts != None:
      self.lead["contacts"] = contacts
    if accounts != None:
      self.lead["accounts"] = accounts
    if products != None:
      self.lead["products"] = products
    if competitors != None:
      self.lead["competitors"] = competitors
    if sources != None:
      self.lead["sources"] = sources
    if note != None:
      self.lead["note"] = note
    if customFields != None:
      self.lead["customFields"] = customFields
    self.payload = json.dumps(
        {"method" : "editLead",
          "params" : {"lead":self.lead,"leadId" : leadId, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editLeadclose(self, leadId,
      id=None, rev=None,
      typeb=None, description=None,
      closedTime=None, isPending=False):
    self.rev = rev
    self.lead = {}
    self.outcome = {}
    self.outcome["entityType"] = "Lead_Outcomes"
    if id != None:
      self.outcome["id"] = id
    if rev != None:
      self.outcome["rev"] = rev
    if typeb != None:
      self.outcome["type"] = typeb
    if description != None:
      self.outcome["description"] = description
    if closedTime != None:
      self.lead["closedTime"] = closedTime
    if isPending == True:
      self.lead["isPending"] = True
    else:
      self.lead["outcome"] = self.outcome
    self.payload = json.dumps(
        {"method" : "editLead",
          "params" : {"lead":self.lead,"leadId" : leadId, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editNote(self, noteid, note, rev=None):
    self.payload = json.dumps(
        {"method" : "editNote",
          "params" : {"note": note,"noteId" : noteid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editProduct(self, productid, product=None, rev=None):
    self.payload = json.dumps(
        {"method" : "editProduct",
          "params" : {"product": product,"productId" : productid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editStep(self, stepid, assignee=None,
      status=None, choice=None, delay=None,
      rev=None):
    self.step={}
    if assignee != None:
      self.step["assignee"] = assignee
    if status != None:
      self.step["status"] = status
    if choice != None:
      self.step["choice"] = choice
    if delay != None:
      self.step["delay"] = delay
    self.payload = json.dumps(
        {"method" : "editStep",
          "params" : {"step": self.step,"stepId" : stepid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editTask(self, taskid, task=None, rev=None):
    self.payload = json.dumps(
        {"method" : "editTask",
          "params" : {"task": task,"taskId" : taskid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editTeam(self, teamid, team=None, rev=None):
    self.payload = json.dumps(
        {"method" : "editTeam",
          "params" : {"team": team,"teamId" : teamid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def editUser(self, userid, emails=None,
      teams=None, sendInvite=None,
      firstName=None, lastName=None,
      password=None, isEnabled=None,
      isAdministrator=None):
    self.user={}
    if emails != None:
      self.user["emails"] = emails
    if teams != None:
      self.user["teams"] = teams
    if sendInvite != None:
      self.user["sendInvite"] = sendInvite
    if firstName != None:
      self.user["firstName"] = firstName
    if lastName != None:
      self.user["lastName"] = lastName
    if password != None:
      self.user["password"] = password
    if isEnabled != None:
      self.user["isEnabled"] = isEnabled
    if isAdministrator != None:
      self.user["isAdministrator"] = isAdministrator
    if teams != None:
      self.user["teams"] = teams
    self.payload = json.dumps(
        {"method" : "editUser",
          "params" : {"user": self.user,"userId" : userid, "rev" : rev},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findAccounts(self, orderBy="name",
      orderDirection="ASC", limit=50,
      page=1, stubResponses=True,
      accountType=None, industry=None,
      origin=None, hasOpenLeads=None,
      tag=None):
    self.query={}
    if accountType != None:
      self.query["accountType"] = accountType
    if industry != None:
      self.query["industry"] = industry
    if origin != None:
      self.query["origin"] = origin
    if hasOpenLeads != None:
      self.query["hasOpenLeads"] = hasOpenLeads
    if tag != None:
      self.query["tag"] = tag
    self.payload = json.dumps(
        {"method" : "findAccounts",
          "params" : {
            "query": self.query,
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findAccountTypes(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findAccountTypes",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findActivities(self, orderBy="name",
      orderDirection="ASC", limit=50,
      page=1, stubResponses=True,
      leadId=None, contactId=None,
      userId=None, status=None,
      activityTypeId=None, isFlagged=None,
      startTime=None, endTime=None):
    self.query={}
    if leadId != None:
      self.query["leadId"] = leadId
    if contactId != None:
      self.query["contactId"] = contactId
    if userId != None:
      self.query["userId"] = userId
    if status != None:
      self.query["status"] = status
    if activityTypeId != None:
      self.query["activityTypeId"] = activityTypeId
    if isFlagged != None:
      self.query["isFlagged"] = isFlagged,
    if startTime != None:
      self.query["startTime"] = startTime
    if endTime != None:
      self.query["endTime"] = endTime
    self.payload = json.dumps(
        {"method" : "findActivities",
          "params" : {
            "query": self.query,
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findActivityTypes(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findActivityTypes",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findBackups(self):
    self.payload = json.dumps({"method" : "findBackups","id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findCompetitors(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findCompetitors",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findContacts(self, orderBy="id",
      orderDirection="ASC", limit=50,
      page=1, stubResponses=True,
      accountId=None, leadId=None,
      tag=None):
    self.query={}
    if accountId != None:
      self.query["accountId"] = accountId
    if leadId != None:
      self.query["leadId"] = leadId
    if tag != None:
      self.query["tag"] = tag
    self.payload = json.dumps(
        {"method" : "findContacts",
          "params" : {
            "query": self.query,
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findCustomFields(self):
    self.payload = json.dumps({"method" : "findCustomFields","id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findDelays(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findDelays",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findIndustries(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findIndustries",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findLead_Outcomes(self, orderBy="description",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findLead_Outcomes",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findLeads(self, orderBy="id",
      orderDirection="ASC", limit=50,
      page=1, stubResponses=True,
      accountType=None, industry=None,
      origin=None, hasOpenLeads=None,
      tag=None):
    self.query={}
    if accountType != None:
      self.query["accountType"] = accountType
    if industry != None:
      self.query["industry"] = industry
    if origin != None:
      self.query["origin"] = origin
    if hasOpenLeads != None:
      self.query["hasOpenLeads"] = hasOpenLeads
    if tag != None:
      self.query["tag"] = tag
    self.payload = json.dumps(
        {"method" : "findAccounts",
          "params" : {
            "query": self.query,
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findMarkets(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findMarkets",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findMilestones(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findMilestones",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findOrigins(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findOrigin",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findProcesses(self, query=None):
    self.payload = json.dumps(
        {"method" : "findProcesses",
          "params" : {"query" : query},
          "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findProducts(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1,
      stubResponses=True):
    self.payload = json.dumps(
        {"method" : "findProducts",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findSettings(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findSettings",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findSources(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findSources",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findTags(self):
    self.payload = json.dumps({"method" : "findTags","id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content


  def findTasks(self, query=None):
    self.payload = json.dumps({"method" : "findTasks", "params" : {"query" : query}, "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findTeams(self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findTeams",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findTerritories (self, orderBy="name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findTerritories",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findTimeline (self, orderBy="time",
      orderDirection="ASC", limit=50,page=1,
      stubResponses=True, query=None):
    self.payload = json.dumps(
        {"method" : "findTimeline",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            "stubResponses" : stubResponses,
            "query" : query
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def findUsers(self, orderBy="last_name",
      orderDirection="ASC", limit=50,page=1):
    self.payload = json.dumps(
        {"method" : "findUsers",
          "params" : {
            "orderBy" : orderBy,
            "orderDirection" : orderDirection,
            "limit" : limit,
            "page" : page,
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getAccount(self, accountId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getAccount",
          "params" : {
            "accountId" : accountId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getActivity(self, activityId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getActivity",
          "params" : {
            "activityId" : activityId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getAnalyticsReport(self, reportType=None,
      period=None, filter=None,options=None):
    self.payload = json.dumps(
        {"method" : "getAnalyticsReport",
          "params" : {
            "reportType" : reportType,
            "period": period,
            "filter" : filter,
            "options" : options
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getContact(self, contactId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getContact",
          "params" : {
            "contactId" : contactId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getEmail(self, emailId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getEmail",
          "params" : {
            "emailId" : emailId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getLead(self, leadId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getLead",
          "params" : {
            "leadId" : leadId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getNote(self, noteId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getNote",
          "params" : {
            "noteId" : noteId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getProduct(self, productId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getProduct",
          "params" : {
            "productId" : productId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getTask(self, taskId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getTask",
          "params" : {
            "taskId" : taskId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getTeam(self, teamId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getTeam",
          "params" : {
            "teamId" : teamId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getUpdateTimes(self):
    self.payload = json.dumps({"method" : "getUpdateTimes","id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def getUser(self, userId=None, rev=None):
    self.payload = json.dumps(
        {"method" : "getUser",
          "params" : {
            "userId" : userId,
            "rev" : rev
            },
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newAccount(self,
      name=None, owner=None,industryId=None,
      accountTypeId=None,territoryId=None,
      url=None, phone=None, leads=None,
      contacts=None, address=None,
      customFields=None):
    self.account={}
    if name != None:
      self.account["name"] = name
    if phone != None:
      self.account["phone"] = phone
    if industryId != None:
      self.account["industryId"] = industryId
    if owner != None:
      self.account["owner"] = owner
    if accountTypeId != None:
      self.account["accountTypeId"] = accountTypeId
    if territoryId != None:
      self.account["territoryId"] = territoryId
    if url != None:
      self.account["url"] = url
    if phone != None:
      self.account["phone"] = phone
    if leads != None:
      self.account["leads"] = leads
    if contacts != None:
      self.account["contacts"] = contacts
    if address != None:
      self.account["address"] = address
    if customFields != None:
      self.account["customFields"] = customFields

    self.payload = json.dumps(
        {"method" : "newAccount",
          "params" : {"account":self.account},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content


  def newActivity(self,
      name=None,startTime=None, endTime=None,
      activityTypeId=None,participants=None,
      isAllDay=True, location=None,
      isFlagged=False, isTimed=True,
      description=None,leads=None):
    self.activity={}
    if name != None:
      self.activity["name"] = name
    if startTime!= None:
      self.activity["startTime"] = startTime
    if endTime != None:
      self.activity["endTime"]= endTime
    if activityTypeId != None:
      self.activity["activityTypeId"] = activityTypeId
    if participants != None:
      self.activity["participants"] = participants
    if isAllDay == True:
      self.activity["isAllDay"] = True
    if location != None:
      self.activity["location"] = location
    if leads != None:
      self.activity["leads"] = leads
    if isFlagged == True:
      self.activity["isFlagged"] = True
    if isTimed == True:
      self.activity["isTimed"] = True
    if description != None:
      self.activity["description"] = description
    if participants != None:
      self.activity["participants"] = participants
    self.payload = json.dumps(
        {"method" : "newActivity",
          "params" : {"activity":self.activity},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newBackup(self):
    self.payload = json.dumps({"method" : "newBackup","id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newContact(self,
      name=None, owner=None,
      description=None,territoryId=None,
      url=None, phone=None, leads=None,
      accounts=None, address=None,
      customFields=None, email=None):
    self.contact={}
    if name != None:
      self.contact["name"] = name
    if phone != None:
      self.contact["phone"] = phone
    if description != None:
      self.contact["description"] = desciption
    if owner != None:
      self.contact["owner"] = owner
    if territoryId != None:
      self.contact["territoryId"] = territoryId
    if url != None:
      self.contact["url"] = url
    if email != None:
      self.contact["email"] = email
    if phone != None:
      self.contact["phone"] = phone
    if leads != None:
      self.contact["leads"] = leads
    if accounts != None:
      self.contact["accounts"] = accounts
    if address != None:
      self.contact["address"] = address
    if customFields != None:
      self.contact["customFields"] = customFields
    self.payload = json.dumps(
        {"method" : "newContact",
          "params" : {"contact": self.contact},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newEmail(self, emailString=None):
    self.payload = json.dumps({"method" : "newEmail",
      "params" : {"emailString" : emailString},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newLead(self, primaryAccount=None, dueTime=None,
      market=None, accounts=None, contacts=None,
      products=None, competitors=None, sources=None,
      confidence=None, assignee=None, customFields=None,
      note=None):
    self.lead={}
    if primaryAccount != None:
      self.lead["primaryAccount"] = primaryAccount
    if dueTime != None:
      self.lead["dueTime"] = dueTime
    if market != None:
      self.lead["market"] = market
    if accounts != None:
      self.lead["accounts"] = accounts
    if contacts != None:
      self.lead["contacts"] = contacts
    if products != None:
      self.lead["products"] = products
    if competitors != None:
      self.lead["competitors"] = competitors
    if sources != None:
      self.lead["sources"] = sources
    if confidence != None:
      self.lead["confidence"] = confidence
    if assignee != None:
      self.lead["assignee"] = assignee
    if customFields != None:
      self.lead["customFields"] = customFields
    if note != None:
      self.lead["note"] = note
    self.payload = json.dumps(
        {"method" : "newLead",
          "params" : {"lead":self.lead},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newNote(self, entity=None, note=None):
    self.payload = json.dumps({"method" : "newNote",
      "params" : {"entity" : entity, "note" : note},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newProduct(self, name=None, type=None,
      sku=None, unit=None, prices=None):
    self.product={}
    if name != None:
      self.product["name"] = name
    if type != None:
      self.product["type"] = type
    if sku != None:
      self.product["sku"] = sku
    if unit != None:
      self.product["unit"] = unit
    if prices != None:
      self.product["prices"] = prices
    self.payload = json.dumps(
        {"method" : "newProduct",
          "params" : {"product":self.product},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newSource(self, name=None):
    self.payload = json.dumps({"method" : "newSource",
      "params" : {"name" : name},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newTag(self, tag=None):
    self.payload = json.dumps({"method" : "newTag",
      "params" : {"tag" : tag},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newTask(self, task=None):
    self.payload = json.dumps({"method" : "newTask",
      "params" : {"task" : task},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newTeam(self, team=None):
    self.payload = json.dumps({"method" : "newTeam",
      "params" : {"team" : team},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def newUser(self,
      firstName=None, lastName=None,
      password=None, emails=None,
      isEnabled=True, isAdministrator=False,
      teams=None, sendInvite=False):
    self.user={}
    if firstName != None:
      self.user["firstName"] = firstName
    if lastName != None:
      self.user["lastName"] = lastName
    if password != None:
      self.user["password"] = password
    if emails != None:
      self.user["emails"] = emails
    if teams != None:
      self.user["teams"] = teams
    self.user["isEnabled"] = isEnabled
    self.user["isAdministrator"] = isAdministrator
    self.user["sendInvite"] = sendInvite
    self.payload = json.dumps(
        {"method" : "newUser",
          "params" : {"user":self.user},
          "id" : "apeye"
          }
        )
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchAccounts(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchAccounts",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchActivityParticipants(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchActivityParticipants",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchByEmail(self, emailAddressString=None):
    self.payload = json.dumps({"method" : "searchByEmail",
      "params" : {"emailAddressString" : emailAddressString},"id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchCompetitors(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchCompetitors",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchContacts(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchContacts",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchContactsAndUsers(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchContactsAndUsers",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchLeads(self, string=None, limit=40):
    self.payload = json.dumps({"method" : "searchLeads",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchProducts(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchProducts",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchSources(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchSources",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchUniversal(self, string=None):
    self.payload = json.dumps({"method" : "searchUniversal",
      "params" : {"string" : string},"id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content

  def searchUsersAndTeams(self, string=None, limit=10):
    self.payload = json.dumps({"method" : "searchUsersAndTeams",
      "params" : {"string" : string, "limit" : limit},
      "id" : "apeye"})
    self.r=requests.post(self.uri, auth=self.auth, data=self.payload)
    Nutshell.response=self.r.content
