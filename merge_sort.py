def merge_lists(lst1, lst2):
    # Write your code here
    merged_lst = []
    if len(lst1) == 0 and len(lst2) == 0:
        return  merged_lst
    elif len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
        
    l1 = l2 = 0 

    for i in range(len(lst1 + lst2)):
        if lst1[l1] > lst2[l2]:
            merged_lst.append(lst2[l2])
            l2 = l2 + 1
            if len(lst2) == l2:
                merged_lst = merged_lst + lst1[l1:]
                return merged_lst

        elif lst1[l1] < lst2[l2]:
            merged_lst.append(lst1[l1])
            l1 = l1 + 1
            if len(lst1) == l1:
                merged_lst = merged_lst + lst2[l2:]
                return merged_lst
        
        else:
            merged_lst.append(lst1[l1])
            merged_lst.append(lst2[l2])
            l1 = l1 + 1
            l2 = l2 + 1
            if len(lst1) == l1:
                merged_lst = merged_lst + lst2[l2:]
                return merged_lst
                
            elif len(lst2) == l2:
                merged_lst = merged_lst + lst1[l1:]
                return merged_lst
            

    return merged_lst


def merge_sort(lst):
  if len(lst) == 0:
    return []
  if len(lst) == 1:
    return lst
  
  a = merge_sort(lst[0:int(len(lst)/2)])
  b = merge_sort(lst[int(len(lst)/2): ])
  return merge_lists(a,b)
