from modules.tree.expressionTree import LeafNode, InteriorNode
from modules.tree.tokens import Token


def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3)) - (2 + 3)) :", c.infix())
    print("Expect - * 4 + 2 3 + 2 3         :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -         :", c.postfix())
    print("Expect 15                        :", c.value())
    print(b)

if __name__ == "__main__":
    main()
