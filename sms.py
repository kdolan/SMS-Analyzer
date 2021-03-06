"""
    
    Author: Kevin J Dolan
    Project: SMS Analysis 
    File Name: sms.py
    Purpose: Take an sms.xml file generated by the android app SMS Backup and Restore by Ritesh Sahu and can do various analysis using custom
	data structures.    
    
"""

from xml.dom import minidom

class MessageLst():
    """Object to hold a lst of message objects and the total number of messages in the lst as well an optional description of what the lst contains."""
    __slots__="messageCount","messages","description"

class Message():
	"""Object that holds all of the data of a message. The message object is the put into a MessageLst object for easy access."""
    __slots__="address","date","readableDate","contactName","type","body"

def mkMessage(address, date, readableDate, contactName, type, body):
	"""Builder function for Message object."""
    message = Message()
    message.address = address
    message.date = date
    message.contactName = contactName
    message.readableDate = readableDate
    message.type = type
    message.body = body
    return message

def mkMessageLst(messageCount, messages, description):
	"""Builder function for MessageLst object."""
    messageLst = MessageLst()
    messageLst.messageCount = messageCount
    messageLst.messages = messages
    messageLst.description = description
    return messageLst

def getListOfRecivedMessages(smsXMLPath, lstExcludeContactNames=["*"], lstContactNames=["*"]):
	"""Given a path of an smsXML file this function returns a MessageLst of all messages recived. lstExcludeContactNames is a list containing the contact names of people who should not be included. lstContactNames is a lst of people to include in the search. All others excluded."""
    xmldoc = minidom.parse(smsXMLPath)
    itemlist = xmldoc.getElementsByTagName('sms')
    totalMessages = 0
    messageLst = []
    for s in itemlist:
        if(s.attributes['type'].value=="1"):
            if(s.attributes['contact_name'].value in lstExcludeContactNames):
                continue
            elif(lstContactNames==["*"]):
                messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
                totalMessages+=1
            elif(s.attributes['contact_name'].value in lstContactNames):
                messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
                totalMessages=totalMessages+1
    return mkMessageLst(totalMessages, messageLst, "Description")
            

def getListOfSentMessages(smsXMLPath, lstExcludeContactNames=["*"], lstContactNames=["*"]):
	"""Given a path of an smsXML file this function returns a MessageLst of all messages sent. lstExcludeContactNames is a list containing the contact names of people who should not be included. lstContactNames is a lst of people to include in the search. All others excluded."""
    xmldoc = minidom.parse(smsXMLPath)
    itemlist = xmldoc.getElementsByTagName('sms')
    totalMessages = 0
    messageLst = []
    for s in itemlist:
        if(s.attributes['type'].value=="2"):
            if(s.attributes['contact_name'].value in lstExcludeContactNames):
                continue
            elif(lstContactNames==["*"]):
                messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
                totalMessages+=1
            elif(s.attributes['contact_name'].value in lstContactNames):
                messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
                totalMessages+=1
    return  mkMessageLst(totalMessages, messageLst, "Description")

def getListOfAllMessages(smsXMLPath, lstExcludeContactNames=["*"], lstContactNames=["*"]):
	"""Given a path of an smsXML file this function returns a MessageLst of all messages. lstExcludeContactNames is a list containing the contact names of people who should not be included. lstContactNames is a lst of people to include in the search. All others excluded."""
    xmldoc = minidom.parse(smsXMLPath)
    itemlist = xmldoc.getElementsByTagName('sms')
    totalMessages = 0
    messageLst = []
    for s in itemlist:
        if(s.attributes['contact_name'].value in lstExcludeContactNames):
            continue
        elif(lstContactNames==["*"]):
            messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
            totalMessages+=1
        elif(s.attributes['contact_name'].value in lstContactNames):
            messageLst.append(mkMessage(s.attributes['address'].value, s.attributes['date'].value, s.attributes['readable_date'].value, s.attributes['contact_name'].value, s.attributes['type'].value, s.attributes['body'].value))
            totalMessages+=1
    return mkMessageLst(totalMessages, messageLst, "Description")