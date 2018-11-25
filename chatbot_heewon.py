# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:16:42 2018

@author: 82103
"""

responses = { 
    ("food", "eat", "eating"): ["Vegetables and fruits are rich in vitamins and minerals.", 
    "Eating evenly is good for your health.", "Avoid greasy food as much as possible."], 
    
    ("exercise", "workout", "sports"): ["Jogging increases basal metabolism and decreases body fat.", 
    "Squat is a strength exercise that strengthens whole body muscle and helps you to diet.", 
    "Exercise both strength and aerobic exercise."],  
    
    ("weight", "weight loss", "weigh", "fat", "diet"): ["Go on a healthy diet.", "Extreme diet is not good.", 
    "Starving is not good for your health.", "Regular exercise is important."],
    
    ("disease", "illness", "sickness", "sick"): ["Go to the hospital and be prescribed medicine.", 
    "Keep your body temperature warm.", "Drink lots of water to keep you hydrated."],
    
    "default" : "I don't get it. Any other question?"
    } 
  
 
import random
 
def respond(user_message):  
      for user_messages in responses:  
          for word in user_message.split(' '):
              if word.lower() in user_messages: 
                  return random.choice(responses[user_messages])
      return responses["default"]
  
 
  

while True: 
      user_message = input('Say Something About Health(Say "bye" to exit) : \n ') 
      if user_message == 'bye': 
          print("See you later ~") 
          break 
      print("Respond: \n", respond(user_message)) 