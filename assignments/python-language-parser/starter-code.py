"""Starter code for a recursive-descent arithmetic expression parser."""

TOKEN_TYPES = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "(": "LPAREN",
    ")": "RPAREN",
}


def tokenize(source):
    """Return (token_type, value) pairs for the source expression."""
    raise NotImplementedError("Implement tokenization")


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        """Return the current token, or None when all tokens are consumed."""
        raise NotImplementedError("Return the current token")

    def consume(self, expected_type):
        """Consume and return a token, or report an unexpected token."""
        raise NotImplementedError("Check and consume the expected token")

    def parse(self):
        """Parse one complete expression and return its AST."""
        raise NotImplementedError("Parse the expression and check for extra tokens")

    def parse_expression(self):
        """Parse addition and subtraction."""
        raise NotImplementedError("Implement the expression grammar rule")

    def parse_term(self):
        """Parse multiplication and division."""
        raise NotImplementedError("Implement the term grammar rule")

    def parse_factor(self):
        """Parse an integer or a parenthesized expression."""
        raise NotImplementedError("Implement the factor grammar rule")


def parse(source):
    """Tokenize and parse source, returning its AST."""
    return Parser(tokenize(source)).parse()