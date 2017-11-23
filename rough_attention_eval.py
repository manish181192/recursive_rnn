def binary_insert(tuple_list, tuple, start, end):

    length = end - start
    if length == 0:
        tuple_list.insert(start, tuple)
        print start
        return
    mid = start+ (length/2)

    if tuple[0]>tuple_list[mid]:
        if mid-1 <start:
            tuple_list.insert(start, tuple)
            print start
            return
        print 'Left'
        binary_insert(tuple_list, tuple, start, mid-1)
    elif tuple[0]<tuple_list[mid]:
        if mid+1>=end:
            tuple_list.insert(end, tuple)
            print end
            return
        print 'right'
        binary_insert(tuple_list, tuple, mid+1, end)


at_file = open('/home/mvidyasa/Documents/attention_output')

relation_scoreSentTuple = {}

current_rel = None
for line in at_file.readlines():
    print line
    if line.__contains__('\t'):
        splitline = line.split('\t')
        score = float(splitline[0])
        sent = splitline[1]
        scoresentTuple = (score, sent)
        binary_insert(relation_scoreSentTuple[current_rel], scoresentTuple, 0, len(relation_scoreSentTuple[current_rel]))
    else:
        rel = line.strip('\n')
        if not relation_scoreSentTuple.has_key(rel):
            relation_scoreSentTuple[rel] = []
        current_rel = rel

att_file = open('Attention_Consolidated','w')
for relation in relation_scoreSentTuple:
    scoreSentList = relation_scoreSentTuple[relation]
    att_file.write(relation+'\n')
    for scoresentTuple in scoreSentList:
        att_file.write(str(scoresentTuple[0])+'\t'+scoresentTuple[1]+'\n')
    att_file.write('\n\n')
att_file.close()