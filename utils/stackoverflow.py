from stackapi import StackAPI

site = StackAPI('stackoverflow')

def doubtsearch(query):
    return site.fetch('search', intitle=query)["items"]

def suggestion(results):
    if results == []:
        return "Sorry I couldn't find anything related. You can google to find an answer on some other websites or post a question yourself."
    
    reply = u"""Here are some results:\n\n"""
    for i in range(min(5, len(results))):
        reply += """%s. <a href="%s">%s</a>\n\n""" % (
            str(i + 1), results[i]["link"], results[i]["title"])

    return reply
