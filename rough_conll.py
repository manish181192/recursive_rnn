train = open('/home/mvidyasa/models/syntaxnet/train_conll.txt')
train_lines = train.readlines()

out = open('/home/mvidyasa/models/syntaxnet/ouput_train_conll.txt')
out_lines = out.readlines()

for lid, line in enumerate(train_lines):
    print lid
    # if lid == 41:
    #     print  ""
    if line == "\n":
        continue
    splitLine = line.split('\t')
    word = splitLine[1]

    out_splitLine = out_lines[lid].split('\t')
    out_word = splitLine[1]

    if word != out_word:
        print "Line id = "+str(lid)+" := "+line+"\t"+out_lines[lid]
        break
