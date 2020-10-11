def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n // i
       i += 1
   if n > 1:
       primfac.append(n)
   return primfac

def counter(mult, half):
    global ans, cash, n
    if len(mult) == 1:
        return
    for i in range(1, len(mult)):
        counter(mult[:i], mult[i:])
        counter(mult[i:], mult[:i])
        if mult[:i] != mult[i:]:
            if (mult[i:], mult[:i]) in cash or (mult[:i], mult[i:]) in cash:
                continue

            if half != 0:
                if half == mult[i:] or half == mult[:i]:
                    continue
                m1 = 1
                m2 = 1
                m3 = 1
                for i in mult[:i]:
                    m1 *= i
                for i in mult[i:]:
                    m2 *= i
                for i in half:
                    m3 *= i

                if m1*m2*m3 != n:
                    continue

            cash.append((mult[:i], mult[i:]))
            ans += 1

n = int(input())

cash = []
ans = 1

mult = primfacs(n)

counter(mult, 0)
print(ans)

