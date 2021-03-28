def larger_power(base,exponent):
    result = base ** exponent
    if result >=5000:
        return True
    else:
        return False

print(larger_power(2,12))
