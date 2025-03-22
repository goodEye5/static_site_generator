import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node_split = split_nodes_delimiter([node], "`", TextType.CODE)
        node_answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(node_split,node_answer)