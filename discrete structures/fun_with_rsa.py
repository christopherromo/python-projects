def GCD(a, b):
    r = a % b
    if r == 0: return b
    return GCD(b, r)

[GCD(72,7),GCD(24,30)]

import math

global r_list
global s_list
global t_list
global q_list

prevCheck = True

r_list = list()
s_list = list()
t_list = list()
q_list = list()

def egcd(a, b):

    global prevCheck
    if prevCheck:
        r_list.clear()
        s_list.clear()
        t_list.clear()
        q_list.clear()

        s_list.append(1)
        t_list.append(0)
        s_list.append(0)
        t_list.append(1)

        prevCheck = False

    r_list.append(a % b)
    q_list.append(a // b)

    if r_list[-1] == 0:
        prevCheck = True
        return [r_list[-2],s_list[-1],t_list[-1],q_list[-2]]
    else:

        new_mod = b % a    
        new_quo = b // a

        ri_1,si_1,ti_1,qi_1 = egcd(new_mod,a)
        
        ri_2 = q_list[-1] * ri_1 + r_list[-1]

        ri = ri_1
        si = ti_1 - new_quo * si_1
        ti = si_1
        qi = ri_2 // ri_1

        r_list.append(ri)
        s_list.append(si)
        t_list.append(ti)
        q_list.append(qi)

        return [ri, si, ti, qi]
    
assert egcd(72,7) == [1,-3, 31, 3]
assert egcd(24,30) == [6, -1, 1, 1]

def find_d(k,e):
    return egcd(k,e)[2]

assert find_d(72,7) == 31
assert find_d(1449000,7907) == 643043

def keyset(p, q, e):
    n = int(p * q)
    k = int((p - 1) * (q - 1))  

    d = int(find_d(k,e))
    
    return [n, e, d]

[n, e, d] = keyset(1381,1051,7907)
assert [n, e, d] == [1451431, 7907, 643043] 

M = 'hello there secret friend'
def encrypt(message, e, n):
    the_exp = e
    the_n = n
    C = list()

    the_length = len(message)
    index = 0

    while index < the_length:
        the_m = ord(message[index])
        the_num = pow(the_m, the_exp, the_n)
        C.append(the_num)

        index += 1

    return C

cipher = encrypt(M, e, n)
assert cipher == [1041244, 739369, 892978, 892978, 799576, 304346, 1398703, 1041244, 739369, 38960, 739369, 304346, 642935, 739369, 1079616, 38960, 739369, 1398703, 304346, 360690, 38960, 722667, 739369, 462214, 282605]

def decrypt(cipher, d, n):
    the_exp = d
    the_n = n
    decrypted_list = list()

    the_length = len(cipher)
    index = 0

    while index < the_length:
        the_c = cipher[index]
        the_num = pow(the_c, the_exp, the_n)
        the_char = chr(the_num)

        decrypted_list.append(the_char)
        index += 1

    decrypted_message = "".join(decrypted_list)
    
    return decrypted_message

message = decrypt(cipher, d, n)
assert message == M

def naivefactors(n):
    
    a = list()

    check = n // 2
    p = check - 1

    while p > 1:
        if n % p == 0:
            q = n / p
            a.append(q)
        p -= 1

    return a

assert naivefactors(21) == [3,7]
assert naivefactors(59444051) == [7703,7717]

[n, e] = [39217303, 7687]
C = [7473306,34860190,31360573,20968028,9070305,20827012,34743153,11419633,36622909,20827012,34743153,7882764,34860190,31360573,21566064,7163950,34860190,31360573,7163950,13366249,34860190,11419633,9070305,7163950,20827012,19210583,29100039,7882764,131312,12921995,131312,21521610,131312,31360573,34743153,4735271,7163950,9665260,7882764,34743153,29100039,7163950,131312,12921995,131312,9070305,13366249,7163950,20827012,19210583,19210583,34860190,21521610,10677701,36622909,7882764,21566064,29100039,21521610,131312,31360573,34743153,7467220,7163950,34743153,29100039,131312,9070305,131312,7163950,7882764,21566064,7163950,20827012,31360573,7163950,131312,31360573,18965078,4735271,7163950,9665260,7882764,34743153,29100039,7163950,131312,12921995,131312,9070305,13366249,7163950,131312,31360573,18965078,7163950,34743153,29100039,131312,9070305,131312,7163950,7882764,21566064,7163950,20827012,36622909,15592578,20827012,13366249,21566064,7163950,20827012,7163950,31360573,131312,15592578,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271,7163950,32047640,7882764,33864881,131312,7163950,19210583,34860190,31360573,34743153,7882764,31360573,11419633,20827012,36622909,36622909,13366249,7163950,21521610,34860190,12921995,131312,21566064,7163950,33864881,9070305,34860190,21521610,7163950,20827012,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271,4735271,4735271,7163950,34743153,34860190,7163950,20827012,31360573,7163950,131312,31360573,18965078,4735271,4735271,4735271,34743153,34860190,7163950,20827012,7163950,31360573,131312,15592578,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271]

p, q = naivefactors(n)
n,e,d = keyset(p,q,e)
message = decrypt(C, d, n)
print(message)