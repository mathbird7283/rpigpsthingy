def heapsort(xs):
    queue=[[]]
    def heap_insert(q,x):
        q[0]=[x]+q[0]
        percolate_down(q,0)