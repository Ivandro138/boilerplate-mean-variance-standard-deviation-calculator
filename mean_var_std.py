import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(lista).reshape(3, 3)

    funcoes = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    result = {}
    for nome, func in funcoes.items():
        result[nome] = [
            func(matriz, axis=0).tolist(),
            func(matriz, axis=1).tolist(),
            func(matriz).item(),
        ]

    return result