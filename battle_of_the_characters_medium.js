function battle(x, y) {
    let LetterPower = {A:1,B:2,C:3,D:4,E:5,F:6,G:7,H:8,I:9,J:10,K:11,L:12,M:13,N:14,O:15,P:16,Q:17,R:18,S:19,T:20,U:21,V:22,W:23,X:24,Y:25,Z:26,
  a:0.5,b:1,c:1.5,d:2,e:2.5,f:3,g:3.5,h:4,i:4.5,j:5,k:5.5,l:6,m:6.5,n:7,o:7.5,p:8,q:8.5,r:9,s:9.5,t:10,u:10.5,v:11,w:11.5,x:12,y:12.5,z:13}
    let group1=x.split('')
    let group2=y.split('')
    let sum1=0
    let sum2=0
    group1.forEach((letter)=>sum1+=LetterPower[letter])
    group2.forEach((letter)=>sum2+=LetterPower[letter])
    if(sum1>sum2){return x
    }else if(sum2>sum1){return y
    }else if(sum1===sum2){return "Tie!"} 
    }