m = 'Goodline'
k = 'T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S'
k *= len(m) // len(k) + 1
c = ''
for i, j in enumerate(m):
    gg = (ord(j) + ord(k[i]))
    c += chr(gg % 26 + 65)
print(c)
a = c 
z = 'T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S' 
v = '' 
for i, j in enumerate(a):
    ll = (ord(j) - ord(z[i]))
    v += chr(ll % 26 + 65)
print(v)
