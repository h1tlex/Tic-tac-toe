def afficher_jeu(jeu):
    print('Etat du jeu :')
    print(jeu[0],'|',jeu[1],' |',jeu[2])
    print("--+","--","+--")
    print(jeu[3],'|',jeu[4],' |',jeu[5])
    print("--+","--","+--")
    print(jeu[6],'|',jeu[7],' |',jeu[8])

def saisir_case(jeu):
    print('Choisissez une case (1-9) :')
    case = int(input())
    i=0
    while i<=9:
        if i+1==case:
            if jeu[i]==' ':
                if PlayerO==0:     
                    jeu.insert(i,'X')
                    jeu.pop(i+1)
                else:
                    jeu.insert(i,'O')
                    jeu.pop(i+1)
                    
            elif jeu[i]=='X' or jeu[i]=='O':
                print("Cette case est remplis, chosis une autre case:")
                afficher_jeu(jeu)
                case=int(input())
                i=0
        
        i+=1                
def est_gagnant(jeu):
    x=0
    v=0
    y=0
    z=2
    
    while x<=8 and v<=3:
        if jeu[x]=='X' and jeu[x+1]=='X' and jeu[x+2]=='X':
            print('X gagne la partie!')
            return True   
        elif jeu[x]=='O' and jeu[x+1]=='O' and jeu[x+2]=='O':
            print('O gagne la partie!')
            return True
        if jeu[v]=='X' and jeu[v+3]=='X' and jeu[v+6]=='X':
            print('X gagne la partie!')
            return True
        elif jeu[v]=='O' and jeu[v+3]=='O' and jeu[v+6]=='O':
            print('O gagne la partie!')
            return True
        if jeu[y]=='X' and jeu[y+4]=='X' and jeu[y+8]=='X':
            print('X gagne la partie!')
            return True
        elif jeu[y]=='O' and jeu[y+4]=='O' and jeu[y+8]=='O':
            print('O gagne la partie!')
            return True
        if jeu[z]=='X' and jeu[z+2]=='X' and jeu[z+4]=='X':
            print('X gagne la partie!')
            return True
        if jeu[z]=='O' and jeu[z+2]=='O' and jeu[z+4]=='O':
            print('O gagne la partie!')
            return True

        else:
            x+=3
            v+=1                       
    return False            

jeu=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
PlayerX=0
PlayerO=1
while est_gagnant(jeu)==False:
    print(jeu)
    afficher_jeu(jeu)
    if PlayerX==0:
        print("Joueur X: ")
        PlayerX+=1
        PlayerO-=1
            
    elif PlayerO==0:
        print("Joueur O: ")
        PlayerO+=1
        PlayerX-=1
    saisir_case(jeu)
afficher_jeu(jeu)            
        

