import numpy as np


# try:
#     def calculate():

#         def create_dictionary():
#             d=dict();
#             d['mean']=[(mean(reshape(3,3),axis=0)),(mean(reshape(3,3),axis=1)),mean() ]
#             d['variance']=[(statistics.variance(reshape(3,3),axis=0)),(statistics.variance(reshape(3,3),axis=1)),statistics.variance() ]
#             d['standard deviation']=[(statistics.stdev(reshape(3,3),axis=0)),(statistics.stdev(reshape(3,3),axis=1)),statistics.stdev() ]
#             d['max']=[(max(reshape(3,3),axis=0)),(max(reshape(3,3),axis=1)),max() ]
#             d['min']=[(min(reshape(3,3),axis=0)),(min(reshape(3,3),axis=1)),min()]
#             d['sum']=[(sum(reshape(3,3),axis=0)),(sum(reshape(3,3),axis=1)),sum() ]

#         return calculations
#         print(''mean': ', create_dictionary(mean))
#         print(''variance': ', create_dictionary(statistics.variance))
#         print(''standard deviation': ',create_dictionary(statistics.stdev))
#         print(''max':',create_dictionary(max))
#         print(''min':',create_dictionary(min))
#         print(''sum':',create_dictionary(sum))
# except ValueError:
#     print("List must contain nine numbers.")


def calculate(input_list):
    if len(input_list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        input_list = np.array(input_list)
        input_modified = input_list.reshape(3, 3)

        d = {}
        d['mean'] = [input_modified.mean(axis=0).tolist(), input_modified.mean(axis=1).tolist(), input_list.mean()]
        d['variance'] = [input_modified.var(axis=0).tolist(), input_modified.var(axis=1).tolist(), input_list.var()]
        d['standard deviation'] = [input_modified.std(axis=0).tolist(), input_modified.std(axis=1).tolist(),
                                   input_list.std()]
        d['max'] = [input_modified.max(axis=0).tolist(), input_modified.max(axis=1).tolist(), input_list.max()]
        d['min'] = [input_modified.min(axis=0).tolist(), input_modified.min(axis=1).tolist(), input_list.min()]
        d['sum'] = [input_modified.sum(axis=0).tolist(), input_modified.sum(axis=1).tolist(), input_list.sum()]

        # print("'mean'",": ", d["mean"])   this is the correct version

        # print(''mean': ', d['mean'])
        # print(''variance': ', d['variance'])
        # print(''standard deviation': ', d['standard deviation'])
        # print(''max':', d['max'])
        # print(''min':', d['min'])
        # print(''sum':', d['sum'])

        return d
