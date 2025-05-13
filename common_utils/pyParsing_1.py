#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.pyParsing_1
# @Calendar: 2025-05-12 20:24
# @Time: 20:24
# @Author: mammon, kiramario
import datetime
from pyparsing import Word, alphas, OneOrMore, Literal, oneOf, Group



def test1():
    """
    BNF:
        <greeting> ::= <salutation> + <comma> + <greetee> + <endpunc>
        <salutation> ::= <word>+
        <comma> ::= ","
        <greetee> ::= <word>+
        <word> ::= [A-Z] | [z-z] | "'" | "."
        <endpunc> ::= "!" | "?"

    :   return:
    """

    # 解析器
    word = Word(alphas + "'.")
    salutation = Group(OneOrMore(word))
    comma = Literal(",")
    greetee = Group(OneOrMore(word))
    endpunc = oneOf("! ?")  # 必须加空格分隔。与Literal("!") | Literal("?")等价。
    greeting = salutation + comma + greetee + endpunc

    tests = ["Hello, World!",
             "Hi, Mom!",
             "Good morning, Miss Crabtree!",
             "Yo, Adrian!",
             "Whattup, G?",
             "How's it goin', Dude?",
             "Hey, Jude!",
             "Goodbye, Mr. Chips!"]

    parse_res = [greeting.parseString(text) for text in tests]

    for text in parse_res:
        print(text)


def run():
    test1()


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
