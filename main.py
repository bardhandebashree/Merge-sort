# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def merge_sort(arr):
       if len(arr)>1:
        print("*************************")
        m = (len(arr)) // 2
        print(m)
        L = arr[:m]
        R = arr[m:]
        print(L)
        print(R)
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1

            k += 1
            print(arr)
            print("########")

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [32, 9, 67,42]
    print(arr)
    f = 0
    e = 4
    merge_sort(arr)
    print(arr)

