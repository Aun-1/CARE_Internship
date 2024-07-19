import numpy as np

class SlicedMatrixMultiplication:
    def __init__(self, arr1, arr2, vr2_length):
        self.VR0 = np.array(arr1)
        self.matrix = np.array(arr2)
        self.vr2_length = vr2_length
        self.result_vector = np.zeros((self.vr2_length), dtype=float)
        self.HBM = np.zeros((len(self.VR0)), dtype=float)
        self.count = 0

    def multiply_slices(self):
        for j in range(self.vr2_length, len(self.VR0) + 1, self.vr2_length):
            print('///////////////////')
            VR0 = self.VR0[j-self.vr2_length:j]  # Slice VR0
            print(f'VR0 is {VR0}')

            for i in range(len(self.VR0)):  # Iterate over columns of the square matrix
                print('............................................')
                VR2 = self.matrix[j-self.vr2_length:j, i]  # Slice matrix
                print(f'VR2 is {VR2}')

                # Perform element-wise multiplication
                self.result_vector[self.count] = np.dot(VR0, VR2)
                print(f'result_vector is {self.result_vector}')
                self.count += 1

                if self.count % self.vr2_length == 0:
                    # Adjust the slice of HBM to ensure it matches the shape of result_vector
                    self.HBM[i-self.vr2_length+1:i+1] = self.result_vector + self.HBM[i-self.vr2_length+1:i+1]
                    print(f'HBM is now {self.HBM}')
                    self.count = 0

        return self.HBM

# Example usage
arr1 = np.array([0.70928652, 0.87071695, 0.72051859, 0.7308162])
arr2 = np.array([[0.3411025, 0.91516912, 0.81978135, 0.08162627],
                 [0.19568124, 0.79557286, 0.6743828, 0.72187732],
                 [0.29362923, 0.95651546, 0.2513727, 0.7293611],
                 [0.41328716, 0.53398653, 0.63062406, 0.8773441]])
vr2_length = 2

matrix_multiplication = SlicedMatrixMultiplication(arr1, arr2, vr2_length)
final_result = matrix_multiplication.multiply_slices()
print("Returned final result:", final_result)
