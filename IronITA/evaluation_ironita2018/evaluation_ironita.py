#!/usr/bin/env python
# usage: ./evaluation_ironita2018.py RESULT_FILE GOLD_FILE
import sys
import csv

result = {'irony': {'0': set(), '1': set()},
          'sarcasm': {'0': set(), '1': set()}}
with open(sys.argv[1]) as f:
    reader = csv.DictReader(f, dialect='excel-tab')
    for row in reader:
        result['irony'][row['irony']].add(row['idtwitter'])
        if row['sarcasm'] != None and row['sarcasm'] != '' and row['sarcasm'] != ' ':
            result['sarcasm'][row['sarcasm']].add(row['idtwitter'])

gold = {'irony': {'0': set(), '1': set()},
        'sarcasm': {'0': set(), '1': set()}}
with open(sys.argv[2]) as f:
    reader = csv.DictReader(f, dialect='excel-tab')
    for row in reader:
        gold['irony'][row['irony']].add(row['id'])
        gold['sarcasm'][row['sarcasm']].add(row['id'])

def metrics(result, gold):
    try:
        precision = float(len(result.intersection(gold)))/float(len(result))
    except:
        precision = 0.0
    try:
        recall = float(len(result.intersection(gold)))/float(len(gold))
    except:
        recall = 0.0
    try:
        fscore = (2.0 * precision * recall) / (precision + recall)
    except:
        fscore = 0.0
    return precision, recall, fscore


# evaluation Task A: Irony detection
result_non_ironic = result['irony']['0']
result_ironic = result['irony']['1']
gold_non_ironic = gold['irony']['0']
gold_ironic = gold['irony']['1']
precision_ironic, recall_ironic, fscore_ironic = metrics(result_ironic, gold_ironic)
precision_non_ironic, recall_non_ironic, fscore_non_ironic = metrics(result_non_ironic, gold_non_ironic)
average_fscore = (fscore_ironic + fscore_non_ironic) / 2.0
print "Task A, precision (non ironic): ", precision_non_ironic
print "Task A, recall (non ironic): ", recall_non_ironic
print "Task A, F1-score (non ironic): ", fscore_non_ironic
print "Task A, precision (ironic): ", precision_ironic
print "Task A, recall (ironic): ", recall_ironic
print "Task A, F1-score (ironic): ", fscore_ironic
print "Task A, average F1-score: ", average_fscore


# evaluation Task B: Sarcasm detection
result_non_ironic = result['irony']['0'].intersection(result['sarcasm']['0'])
result_ironic = result['irony']['1'].intersection(result['sarcasm']['0'])
result_sarcastic = result['irony']['1'].intersection(result['sarcasm']['1'])
gold_non_ironic = gold['irony']['0'].intersection(gold['sarcasm']['0'])
gold_ironic = gold['irony']['1'].intersection(gold['sarcasm']['0'])
gold_sarcastic = gold['irony']['1'].intersection(gold['sarcasm']['1'])

precision_non_ironic, recall_non_ironic, fscore_non_ironic = metrics(result_non_ironic, gold_non_ironic)
precision_ironic, recall_ironic, fscore_ironic = metrics(result_ironic, gold_ironic)
precision_sarcastic, recall_sarcastic, fscore_sarcastic = metrics(result_sarcastic, gold_sarcastic)
average_fscore = (fscore_ironic + fscore_non_ironic + fscore_sarcastic) / 3.0
print "Task B, precision (non ironic): ", precision_non_ironic
print "Task B, recall (non ironic): ", recall_non_ironic
print "Task B, F1-score (non ironic): ", fscore_non_ironic
print "Task B, precision (ironic): ", precision_ironic
print "Task B, recall (ironic): ", recall_ironic
print "Task B, F1-score (ironic): ", fscore_ironic
print "Task B, precision (sarcastic): ", precision_ironic
print "Task B, recall (sarcastic): ", recall_ironic
print "Task B, F1-score (sarcastic): ", fscore_ironic
print "Task B, average F1-score: ", average_fscore

