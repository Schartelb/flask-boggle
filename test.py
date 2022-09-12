from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import numpy as np


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUpClass(cls):
        boggle_game = Boggle()

    def test_read_dict(self):
        """Checks all words are string"""
        check = Boggle.words.dtype
        self.assertTrue(check[1], "U")

    def test_make_board(self):
        """Check that all characters are ASCII Uppercase"""
        board = []
        for y in range(0, 5):
            for x in range(0, 5):
                self.assertTrue(ord(Boggle.board[y][x]) >= 65)
                self.assertTrue(ord(Boggle.board[y][x]) <= 90)

    def test_check_valid_word(self):
        # not sure how to test this without being able to see a board to check for valid words.
