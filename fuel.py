def main():
    a = input("Fraction: " )
    b=convert(a)
    print(gauge(b))


def convert(fraction):
    while True:
        try:
            n, d = fraction.split("/")
            nn = int(n)
            dd = int(d)
            if nn<=dd:
                p = round((nn / dd) * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(str(percentage)+"%")

if __name__=="__main__":
    main()

