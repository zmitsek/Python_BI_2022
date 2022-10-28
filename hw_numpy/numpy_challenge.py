if __name__ == '__name__':
    arr1 = np.array([8, 800, 5, 5, 5, 5, 5, 3, 5])
    arr2 = np.arange(13,0)
    arr3 = np.linspace(0, np.pi, 4)

def matrix_multiplication(a,b):
    return a @ b

def multiplication_check(list_m):
    for i in range(0, len(list_m - 1)):
        if list_m[i].shape[1] != list_m[i + 1].shape[0]:
            return False
        else:
            return True

def multiply_matrices(list_m):
    if multiplication_check(list_m):
        return np.linalg.multi_dot(list_m)
    else:
        return

def compute_2d_distance(v1,v2):
    return np.sqrt(np.sum(np.square(v1 - v2)))

def compute_multidimensional_distance(v1,v2):
    return np.linalg.norm(v1 - v2)

def compute_pair_distances(matrix):
    return(np.linalg.norm(matrix[:,None, :] - matrix[None, :, :], axis=-1))
