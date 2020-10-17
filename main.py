# coding=gbk
import os
import json
import time
import datetime
import sys
def printf(text):
    print(text)
def files(locat, opt, txt):
    if opt == "read":
        o = 'r'
    elif opt == "ovwrite":
        o = 'w'
    elif opt == "write":
        o = 'a'
    else:
        return False
    
    if o == 'r':
        with open(locat, 'r') as fp:
            ret = fp.read()
        return ret
    elif o == 'w':
        with open(locat, 'w') as fp:
            fp.write(txt)
        return True
    elif o == 'a':
        with open(locat, 'a') as fp:
            fp.write(txt)
        return True
    else:
        return False
    printf("Process ended with True")

def jsonf(locat, opt, txt):
    if opt == "read":
        o = 'r'
    elif opt == "ovwrite":
        o = 'w'
    elif opt == "write":
        o = 'a'
    else:
        return False
    
    if o == 'r':
        with open(locat, 'r') as fp:
            ret = json.load(fp)
        return ret
    elif o == 'w':
        with open(locat, 'w') as fp:
            json.dump(txt, fp)
        return True
    elif o == 'a':
        with open(locat, 'a') as fp:
            json.dump(txt, fp)
        return True
    else:
        return False
    printf("Process ended with True")


def libmorse_e():
    printf("Type the raw text(All lowercase will be turned to uppercase.Please not using any symbols.):")
    rawtext = input("")
    try:
        printf("\n\n\nEncrypting...")
        db = jsonf("etc/morse/dat.json", "read", "")
        prc = rawtext.upper()
        stage_1 = prc.split()
        stg1_length = len(stage_1)
        if stg1_length <= 1:
            st = True
        else:
            st = False
        files("proc/morse_code.tmp", "ovwrite", "")
        if st == True:
            stage_2 = stage_1[0]
            stage_3 = stage_2[:]
            for stage_4 in stage_3:
                cur = db[stage_4]
                files("proc/morse_code.tmp", "write", cur)
                files("proc/morse_code.tmp", "write", "/")
            
            printf(files("proc/morse_code.tmp", "read", ""))
            return True
        elif st == False:
            for stage_2 in stage_1:
                current = 0
                while True:
                    global stg2_length
                    stg2_length = len(stage_2)
                    # printf(stg2_length)
                    # printf(current)
                    if current >= stg2_length:
                        break
                    cur = db[stage_2[current]]
                    files("proc/morse_code.tmp", "write", cur)
                    files("proc/morse_code.tmp", "write", "/")
                    current = current + 1
                    printf(files("proc/morse_code.tmp", "read", ""))
    except KeyError:
        printf("I said don't use any symbols. Idiot!")
        return False
    return True

def libmorse_d():
    files("proc/morse_code.tmp", "ovwrite", "")
    dic = jsonf("etc/morse/dat.json", "read", "")
    printf("Type the encrypted string(such as ./../..-../.): ")
    rawtext = input("")
    printf("Decrypting...")
    s1 = rawtext.split()
    s2 = s1[0]
    length = len(s2)
    length = length - 1
    global c
    ss3 = ''
    c = 0
    while True:
        if c > length:
            break
        s3 = s2[c]
        if s3 == '/':
            c =  c + 1
            try:
                plain = list (dic.keys()) [list (dic.values()).index (ss3)]
            except KeyError:
                printf("Are you sure your code is correct?")
                return False
            files("proc/morse_code.tmp", "write", plain)
            ss3 = ''
            continue
        ss3 += s3
        c = c + 1
    
    print(files("proc/morse_code.tmp", "read", ""))
    return True

def morse():
    printf("International Morse Code")
    printf("What do you want to do?")
    printf("1. Encrypt")
    printf("2. Decrypt")
    o = input("> ")
    if o == '1':
        libmorse_e()
        return True
    elif o == '2':
        libmorse_d()
        return True
    else:
        return False

morse()
