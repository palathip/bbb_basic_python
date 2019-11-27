data = [
{"host1": [
["MS_AOTBTTEXCH01_DB7", "t", 12, 12],
["HP_D2_SATA_TRUE-CJ_01", "t", 2, 2],
["SPARC_TOPGUN_OS", "t", 64, 64]
]
},
{"host2": [
["MS_IDC1_MS_ACI3_PRD01_SAS01", "t", 28, 28],
["BTT_EX04_Prod_HMDB10GB01_AC", "t", 15, 15],
["HP_D1_SAS_SERISYS_2", "t", 68, 68]
]
}
]

for i in range(len(data)):
    for j in data[i]:
        print "host :",j
        for k in range(len(data[i][j])):
#           print data[i][j][k]
           if data[i][j][k][2] > 20:
               print "%s : Critical (%d)"%(data[i][j][k][0],data[i][j][k][2])
           else:
               print "%s : Normal (%d)"%(data[i][j][k][0],data[i][j][k][2])