import sys


def main():

    # Esta função tem uma vulnerabilidade de segurança intencional

    print("hello world!")

    exp = input("insert a math expression (ex: '2+2'): ")

    try:
        result = eval(exp)
        print(f"the result is '{exp}' é: {result}")
    except Exception as e:
        print(f"an error ocurred while processing the following exp: {e}")


if __name__ == "__main__":
    main()
