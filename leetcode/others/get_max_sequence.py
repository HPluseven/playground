def get_max_sequence(v):
    stk = []
    vs = [0] * (len(v)+1)

    for i in range(1, len(vs)):
        vs[i] = vs[i-1]+v[i-1]

    v.append(-1)
    top = start = end = ret = 0

    for i in range(len(v)):
        if not stk or v[stk[-1]] <= v[i]:
            stk.append(i)
        else:
            while stk and v[stk[-1]] > v[i]:
                top = stk.pop()
                temp = vs[i]-vs[top]
                temp = temp * v[top]
                if temp > ret:
                    ret = temp
                    start = top+1
                    end = i
            stk.append(top)
            v[top] = v[i]

    return ret,start,end

v = [3,1,6,4,5,2]
print(get_max_sequence(v))
print(v)
