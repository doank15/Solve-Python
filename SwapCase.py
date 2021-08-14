def swap_case(s):
    s=s.swapcase() # swapcase() chuyển hết chữ hoa về chữ thường và chữ thường về chữ hoa HELLo.swapcase() -> hellO
    return s;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)