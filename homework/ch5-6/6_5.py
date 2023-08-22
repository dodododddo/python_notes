def move(n, A, B, C):
    if n==1:
        print(f'Move {n} from {A} to {C}')
    else:
        move(n-1, A, C, B)
        move(1, A, B, C)
        move(n-1, B, A, C)
        
move(10, 'A','B','C')