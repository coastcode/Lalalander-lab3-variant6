class Lambda(object):
    def __init__(self):
        self.node = Node()
        self.node.label = "start"
        self.node.children = []

    def FACT(self, n):
        cur = self.node
        while cur.next is not None:
            cur = cur.next
        cur.next = Node()
        cur = cur.next
        cur.label = "FACT"
        while cur.next is not None:
            cur = cur.next
        fact = (lambda a: lambda v: a(a, v))(
            lambda s, x: 1 if x == 0 else x * s(s, x - 1))
        a = fact(n)
        while n > 1:
            cur.addkid(f'{n}')
            n -= 1
        cur.addkid('1')
        cur.addkid(f'{a}')
        return a

    def visualize(self):
        cur = self.node
        res = []
        res.append("digraph G {")
        res.append(" rankdir=LR;")
        res.append('    start')
        while cur is not None:
            if cur.label == "start":
                cur = cur.next
            elif cur.label == "FACT":
                print(cur.label)
                for n in range(0, len(cur.children) - 2):
                    print(f'((λf.λx.n=0?1:n*f(n-1))(Y M)){cur.children[n]}')
                    print(f'=>(λn.n=0?1:n * ((Y M)(n - 1)))){cur.children[n]}')
                    print(f'=>{cur.children[n]}*((Y M)({cur.children[n]}- 1))')
                    print(f'=>{cur.children[n]}*((Y M){cur.children[n + 1]})')
                for i in range(0, len(cur.children) - 2):
                    res.append(f'{cur.children[i]}*')
                res.append('1')
                res.append(f'{cur.children[i + 2]}')
                cur = cur.next
        res.append("}")
        # print(res)
        return "\n".join(res)


class Node:

    def __init__(self, label=None, children=None):
        self.label = label
        self.children = children if children is not None else list()
        self.next = None

    def addkid(self, n):
        self.children.append(n)
        return self
