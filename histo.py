def main(hista):
    maxi = 0
    lista = []
    
    def sideways(prev, lista, sizes={}):
        # import ipdb; ipdb.set_trace()
        if prev-1 != -1:
            curr_height = hista[prev]
            if hista[prev-1] >= hista[prev]:
                lista[curr_height] = lista[curr_height] + 1
                return sideways(prev-1, lista, sizes)
            if hista[prev-1] < hista[prev]:
                if not curr_height in lista.keys():
                    curr_height = max(lista.keys())
                
                curr_max = lista[curr_height]
                size = curr_height*curr_max
                sizes[size] = (curr_height, curr_max)
                listnew = {}
                listnew[hista[prev-1]] = lista[curr_height] + 1
                return sideways(prev-1, listnew, sizes)
        else:
            area = max(sizes.keys())
            return area, sizes[area] 
            
    print sideways(10, {5:0}) 
    
    for pos in reversed(hista.keys()):
        import ipdb; ipdb.set_trace()
        height = hista[pos]
        if maxi < height:
            maxi = height 
        size = sideways(pos, {height:0})  
        if maxi < size[0]:
            maxi = size[0] 
            
    print maxi 

if __name__ == "__main__":
    hista = {0:2, 1:3, 2:5, 3:2, 4:3, 5:2, 6:4, 7:6, 8:28, 9:5, 10:5}
    main(hista)