from decimal import Decimal

values = {"mile": 1609, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "km": 1000, \
          "cm": 0.01, "mm": 0.001, "m": 1}
m = {"cm": 0.01, "mm": 0.001, "km": 1000, "m": 1}

def convert_in_meter(v, fr):
    return float(v) * float(values[fr])

def convert_m_k_c(x,y):
    return x / m[y]

def convert_y_m_f_i(x,sr):
    return float(x) / float(values[sr])

# v, fr, trash, sr = input().split(" ")
v, fr, trash, sr = '15.5 m in yard'.split(" ")
v_m = convert_in_meter(v, fr)
if sr in ['m', 'mm', 'cm', 'km']:
    res = convert_m_k_c(v_m, sr)
elif sr in ['yard', 'mile', 'foot', 'inch']:
    res = convert_y_m_f_i(v_m,sr)
print(v, fr, sr)
print(res, '%.2e' % Decimal(res))


