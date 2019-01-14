"""A sandbox for making and testing Python code"""


#gonna create some class objects based on discrete math text (K. Rosen)

class Proposition:
    """statement in a propositional calculus
        attributes:
            statement (str)
            truth (bool or None) [default=None]
        methods:
            __init__ -- instantiation
                args:
                    statement (str)
                    truth (bool or None) [default=None]
            __repr__ -- representation
                returns:
                    rep (str)
            __neg__ -- negation
                returns
                    negation (Proposition)
            __and__ -- conjunction
                args:
                    other (Proposition)
                returns
                    conjunction (Proposition)
            __or__ -- disjunction
                args:
                    other (Proposition)
                returns
                    disjunction (Proposition)
    """

    # instantiation
    def __init__(self, statement, truth=None):
        """instantiate a statement in the propositional calculus
            args:
                statement (str)
                truth (bool or None) [default=None]
        """

        # assigning attributes
        self.statement = statement
        self.truth = truth

    # string representation
    def __repr__(self):
        """represent proposition as a string
            returns:
                rep (str)
        """

        return self.statement

    # negation
    def __neg__(self):
        """return negation of proposition
            returns:
                negation (Proposition)
        """

        # building object
        statement = "NOT {}".format(self.statement)
        truth = not self.truth
        negation = Proposition(statement, truth)

        return negation

    # conjunction
    def __and__(self, other):
        """return conjuction of two propositions
            args:
                other (Proposition)
            returns:
                conjuction (Proposition)
        """

        # building object
        statement = "{0} AND {1}".format(self.statement, other.statement)
        truth = self.truth and other.truth
        conjunction = Proposition(statement, truth)

        return conjunction

    # disjunction
    def __or__(self, other):
        """return disjuction of two propositions
            args:
                other (Proposition)
            returns:
                disjuction (Proposition)
        """

        # building object
        statement = "{0} OR {1}".format(self.statement, other.statement)
        truth = self.truth or other.truth
        disjunction = Proposition(statement, truth)

        return disjunction
        
