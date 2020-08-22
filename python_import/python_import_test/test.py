
test = 'quackqquuaacckk'
test1 = 'quack'
test2 = 'wweaea'

def check_quack(s:str):
    count = 0
    index = 0
    new_str = ''
    for i in range(len(s)):
        if s[i] == 'q':
            [has, new_str] = helper(s, i)
            index = i
            if has:
                count += 1
            break
    
    while new_str:
        has_q = False
        for i in range(len(new_str)):
            if new_str[i] == 'q':
                [has, new_str] = helper(new_str, i)
                if has:
                    count += 1
                has_q = True
                break
        if not has_q:
            break
    return count
        
    

def helper(s:str, i:int):
    if len(s) < 5:
        return ''
    out_str = s
    queue = ['q','u', 'a', 'c', 'k']
    for j in range(i, len(out_str)):
        if queue and s[j] == queue[0]:
            queue.pop(0)
            # print('before', out_str)
            out_str = out_str[:j] + 'b' + out_str[j+1:]
            # print('after ', out_str)
            # 
            
            # 
        if not queue:
            # print(out_str[1:])
            return [True, out_str]
    
    return [False, s] if queue else [True, out_str]


 






if __name__ == "__main__":
    print(check_quack(test2))