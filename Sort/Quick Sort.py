class QuickSort:
    
    def __init__(self, list: list):
        
        self.list = list
    
    def getList(self):
        return self.list
    
    def sort(self, f:int ,l:int):
        # print(self.list)
        if f >= l: return
        x = self.list[f]
        i = f + 1
        j = l
        while i < j:
            while self.list[j] >= x and j >= f:
                j = j - 1
            while i <= l and self.list[i] <= x: #為避免 i > l 的情況，將 self.list[i] 放在後面
                i = i + 1
            if i < j:
                #swap
                self.list[i], self.list[j] = self.list[j], self.list[i]  
                
        self.list[f], self.list[j] = self.list[j], self.list[f]
        
        self.sort(f, j-1)
        
        self.sort(j+1, l)
        
if __name__ == '__main__':
    l = [7,5,1,4,3,2,6]
    QS = QuickSort(l)
    QS.sort(0, len(l)-1)
    print(QS.getList()) 
        