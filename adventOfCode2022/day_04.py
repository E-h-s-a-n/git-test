# edit by youtube
data = open('day_04.txt').read().strip()
lines = [i for i in data.split('\n')]

# pairs = [(i[0],i[1]) for i in (l.strip().split(',') for l in open('day_04.txt'))]
# for p_1, p_2 in pairs:
#   pass

total_overlap = 0 # =528
any_overlap = 0 # =881

for line in lines:
    # 11-73, 29-73
    # line
    # one  , two
    # o1 o2, t1 t2
    one, two = line.split(',')
    o1, o2 = one.split('-')
    t1, t2 = two.split('-')
    o1, o2, t1, t2 = (int(i) for i in [o1, o2, t1, t2])
    # A total overlap
    #  o1  o2
    # t1       t2
    #  
    # o1       o2
    #   t1    t2
    if (o1 >= t1 and o2 <= t2) or (t1 >= o1 and t2 <= o2):
        total_overlap += 1
    # No overlap 
    # o1  o2
    #        t1   t1
    # 
    #  t1  t2
    #         o1  o2
    if not(t1 > o2 or o1 > t2):
        any_overlap += 1

    '''
    section_1 = [int(num) for num in p_1.split('-')]
    section_2 = [int(num) for num in p_2.split('-')]

    sections = set(range(section_1[0],section_1[1]+1)).intersection(range(section_2[0],section_2[1]+1))
    if len(sections) > 0:
        any_overlap += 1
    

    # if section2 is contained in section 1 
    if section_2[0] >= section_1[0]:
        if section_2[1] <= section_1[1]:
            total_overlap += 1
            # print(2222, i,j)
            continue
    
    # if section1 is fully contained in section 2 
    if section_1[0] >= section_2[0]:
        if section_1[1] <= section_2[1]:
            total_overlap += 1
            # print(1111, i,j)
    '''

print(total_overlap, any_overlap)