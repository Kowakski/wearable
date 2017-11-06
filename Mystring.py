'''
@comments: get you wanted
'''
def GetWantedPartH(Str, StaCharacter, EndCharacter):
    i = 0
    Sta = 0
    End = 0
    # print("GetWantedParth Str is {0}".format(Str))

    while i < len(Str):
        # print("i is {0}, Str is {1} {2} {3}".format(i, Str[i], StaCharacter, EndCharacter))
        if Str[i] == StaCharacter:
            Sta = i+1
            # print ("Sta {0}".format(i))
        if Str[i] == EndCharacter:
            End = i
            # print ("End {0}".format(i))
        i += 1
    result = Str[Sta:End]
    return result