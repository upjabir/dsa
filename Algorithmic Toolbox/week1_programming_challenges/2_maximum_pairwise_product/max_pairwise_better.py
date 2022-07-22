
def max_pairwise_product(numbers):
    if len(numbers) > 1:
        first_largest=0
        second_largest=0
        if numbers[0] > numbers[1]:
            first_largest=numbers[0]
            second_largest=numbers[1]
        else:
            first_largest=numbers[1]
            second_largest=numbers[0]

        for i in range(2,len(numbers)):
            if numbers[i] > first_largest:
                second_largest=first_largest
                first_largest=numbers[i]
            elif first_largest > numbers[i] > second_largest:
                second_largest=numbers[i]


        return first_largest*second_largest
    else:
        return numbers[0]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    #l​ist(map(int,input().split())  same as above
    print(max_pairwise_product(input_numbers))