N = int(input())
po_l = []
si_st = []
for _ in range(6):
    which, size = map(int, input().split())
    po_l.append(which)
    si_st.append(size)

    empty = 0

if po_l.count(2) == 1 and po_l.count(4) == 1:
    for i in range(-1, len(po_l)-1):
        if po_l[i] == 1 and po_l[i+1] == 3:
            empty = si_st[i] * si_st[i+1]
    total = si_st[po_l.index(2)] * si_st[po_l.index(4)]
    ans = total -empty

elif po_l.count(1) == 1 and po_l.count(4) == 1:
    for i in range(-1, len(po_l)-1):
        if po_l[i] == 3 and po_l[i+1] == 2:
            empty = si_st[i] * si_st[i+1]
    total = si_st[po_l.index(1)] * si_st[po_l.index(4)]
    ans = total - empty

elif po_l.count(1) == 1 and po_l.count(3) == 1:
    for i in range(-1, len(po_l)-1):
        if po_l[i] == 2 and po_l[i+1] == 4:
            empty = si_st[i] * si_st[i+1]
    total = si_st[po_l.index(1)] * si_st[po_l.index(3)]
    ans = total - empty

elif po_l.count(2) == 1 and po_l.count(3) == 1:
    for i in range(-1, len(po_l)-1):
        if po_l[i] == 4 and po_l[i+1] == 1:
            empty = si_st[i] * si_st[i+1]
    total = si_st[po_l.index(2)] * si_st[po_l.index(3)]
    ans = total - empty

print(ans * N)