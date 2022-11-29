def hello(s=None):
    if s is None or not len(s):
      return "Hello!"
    else:
      return "Hello, {}!".format(s)


def int_to_roman(n):
    ans = ''
    f = dict([(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
              (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
              (5, 'V'), (4, 'IV'), (1, 'I')])
    for arabic, roman in f.items():
        ans += n // arabic * roman
        n %= arabic
    return ans


def longest_common_prefix(inner_list):
    if not len(inner_list):
        return ''

    for s in inner_list:
        if not len(s):
            return ''

    for i in range(len(inner_list)):
        while len(inner_list[i]) and inner_list[i][0] in ['\n', '\t', ' ']:
            inner_list[i] = inner_list[i][1:]

    if not len(inner_list[0]):
        return ''

    pattern = inner_list[0]
    while len(pattern):
        for str in inner_list:
            if not str.startswith(pattern):
                pattern = pattern[:-1]
                break
        else:
            return pattern
    return pattern


class BankCard:
    def __init__(self, total_sum, balance_limit=None):
        self.__total_sum = total_sum
        self.__balance_limit = balance_limit

    @property
    def balance(self):

        if not self.__balance_limit and self.__balance_limit is not None:
            print("Balance check limits exceeded.")
            raise ValueError
        if self.__balance_limit is not None:
            self.__balance_limit -= 1
        return self.__total_sum

    def put(self, summa):
        print("You put {} dollars.".format(summa))
        self.__total_sum += summa

    def __add__(self, other):
        if other.__balance_limit is not None and self.__balance_limit is not None:
            ans = max(other.__balance_limit, self.__balance_limit)
        elif other.__balance_limit is None and self.__balance_limit is not None:
            ans = self.__balance_limit
        elif other.__balance_limit is not None and self.__balance_limit is None:
            ans = other.__balance_limit
        else:
            ans = None
        return BankCard(other.total_sum + self.__total_sum, ans)

    @property
    def balance_limit(self):
        return self.__balance_limit

    def __str__(self):
        return "To learn the balance call balance."

    def __call__(self, sum_spent):
        if self.__total_sum - sum_spent < 0:
            print("Can't spend {} dollars.".format(sum_spent))
            raise ValueError
        else:
            self.__total_sum -= sum_spent
        print("You spent {} dollars.".format(sum_spent))

    def __getattr__(self, name):
        if name == "total_sum":
            return self.__total_sum

def is_prime(n):
  for i in range(2, round(n**0.5) + 1):
    if not n % i:
      return 0
  return 1


def primes():
    i = 2
    while True:
      if is_prime(i):
        yield i
      i += 1  



longest_common_prefix(['', '  ', '   '])
