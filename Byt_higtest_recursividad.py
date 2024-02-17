# Global mutable state
contador = 0
#accumulated_sum = 0
def find_highest(lst):
    global contador
    print(lst)

    if len(lst) == 1 :
        #print("caso base")
        return lst[0]
    else :#recursive caso aqui tambien lo llamas
        r = find_highest(lst[1:])
        #lo compara con el promero de la liesta 
    return r if r >= lst[0] else lst[0]



other_list = [-1, 3, 5, 6, 99, 12, 2]
my_list = [3, 8, 1, 6, 2, 5]
result = find_highest(my_list)

print(f"el objeto mayor es {result}")
result = find_highest(other_list)
print(f"otro resultado : {result}")

#find_highest([-1,3,5,6,99,12,2])
#return find_highest([3,5,6,99,12,2])
#       return find_highest([5,6,99,12,2])
#           return find_highest([6,99,12,2])
#               return find_highest([99,12,2])
#                   return  99
#                       return 99
#                           return 99

