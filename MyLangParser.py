# Generated from ../../MyLang/MyLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,1,1,1,1,1,1,3,1,41,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        57,8,4,10,4,12,4,60,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,70,8,
        5,10,5,12,5,73,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,82,8,5,10,5,12,
        5,85,9,5,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,5,1,5,1,5,5,5,97,
        8,5,10,5,12,5,100,9,5,1,5,3,5,103,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,4,6,113,8,6,11,6,12,6,114,5,6,117,8,6,10,6,12,6,120,9,6,1,
        6,1,6,4,6,124,8,6,11,6,12,6,125,3,6,128,8,6,1,6,1,6,1,6,1,7,1,7,
        5,7,135,8,7,10,7,12,7,138,9,7,1,8,1,8,5,8,142,8,8,10,8,12,8,145,
        9,8,1,8,1,8,1,9,1,9,1,9,3,9,152,8,9,1,10,1,10,1,10,1,10,5,10,158,
        8,10,10,10,12,10,161,9,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,169,
        8,11,10,11,12,11,172,9,11,3,11,174,8,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,3,13,187,8,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,201,8,14,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,209,8,14,10,14,12,14,212,9,14,1,14,0,1,
        28,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,0,227,0,31,1,0,0,
        0,2,40,1,0,0,0,4,42,1,0,0,0,6,47,1,0,0,0,8,50,1,0,0,0,10,63,1,0,
        0,0,12,104,1,0,0,0,14,132,1,0,0,0,16,139,1,0,0,0,18,151,1,0,0,0,
        20,153,1,0,0,0,22,164,1,0,0,0,24,177,1,0,0,0,26,186,1,0,0,0,28,200,
        1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,1,1,0,0,0,35,41,3,4,2,0,36,41,3,6,3,0,37,41,3,8,
        4,0,38,41,3,10,5,0,39,41,5,24,0,0,40,35,1,0,0,0,40,36,1,0,0,0,40,
        37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,14,0,
        0,43,44,5,32,0,0,44,45,5,1,0,0,45,46,3,28,14,0,46,5,1,0,0,0,47,48,
        5,16,0,0,48,49,3,28,14,0,49,7,1,0,0,0,50,51,5,13,0,0,51,52,5,2,0,
        0,52,53,3,26,13,0,53,54,5,3,0,0,54,58,5,4,0,0,55,57,3,2,1,0,56,55,
        1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,
        60,58,1,0,0,0,61,62,5,5,0,0,62,9,1,0,0,0,63,64,5,18,0,0,64,65,5,
        2,0,0,65,66,3,26,13,0,66,67,5,3,0,0,67,71,5,4,0,0,68,70,3,2,1,0,
        69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,
        0,0,0,73,71,1,0,0,0,74,90,5,5,0,0,75,76,5,15,0,0,76,77,5,2,0,0,77,
        78,3,26,13,0,78,79,5,3,0,0,79,83,5,4,0,0,80,82,3,2,1,0,81,80,1,0,
        0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,
        1,0,0,0,86,87,5,5,0,0,87,89,1,0,0,0,88,75,1,0,0,0,89,92,1,0,0,0,
        90,88,1,0,0,0,90,91,1,0,0,0,91,102,1,0,0,0,92,90,1,0,0,0,93,94,5,
        19,0,0,94,98,5,4,0,0,95,97,3,2,1,0,96,95,1,0,0,0,97,100,1,0,0,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,103,
        5,5,0,0,102,93,1,0,0,0,102,103,1,0,0,0,103,11,1,0,0,0,104,105,5,
        20,0,0,105,106,5,2,0,0,106,107,3,28,14,0,107,108,5,3,0,0,108,118,
        5,4,0,0,109,110,5,21,0,0,110,112,5,33,0,0,111,113,3,2,1,0,112,111,
        1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,
        1,0,0,0,116,109,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,127,1,0,0,0,120,118,1,0,0,0,121,123,5,22,0,0,122,124,
        3,2,1,0,123,122,1,0,0,0,124,125,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,121,1,0,0,0,127,128,1,0,0,0,128,129,
        1,0,0,0,129,130,5,5,0,0,130,131,5,23,0,0,131,13,1,0,0,0,132,136,
        5,6,0,0,133,135,5,29,0,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,15,1,0,0,0,138,136,1,0,0,0,139,143,5,
        7,0,0,140,142,5,29,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,
        0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,5,
        7,0,0,147,17,1,0,0,0,148,152,3,20,10,0,149,152,3,22,11,0,150,152,
        5,32,0,0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,19,
        1,0,0,0,153,154,5,8,0,0,154,159,3,28,14,0,155,156,5,9,0,0,156,158,
        3,28,14,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,10,0,0,163,21,
        1,0,0,0,164,173,5,4,0,0,165,170,3,24,12,0,166,167,5,9,0,0,167,169,
        3,24,12,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,173,165,1,0,0,0,173,174,
        1,0,0,0,174,175,1,0,0,0,175,176,5,5,0,0,176,23,1,0,0,0,177,178,5,
        29,0,0,178,179,5,11,0,0,179,180,3,28,14,0,180,25,1,0,0,0,181,182,
        3,28,14,0,182,183,5,26,0,0,183,184,3,28,14,0,184,187,1,0,0,0,185,
        187,5,27,0,0,186,181,1,0,0,0,186,185,1,0,0,0,187,27,1,0,0,0,188,
        189,6,14,-1,0,189,201,5,28,0,0,190,201,5,32,0,0,191,201,5,29,0,0,
        192,201,3,20,10,0,193,201,3,22,11,0,194,195,5,2,0,0,195,196,3,28,
        14,0,196,197,5,25,0,0,197,198,3,28,14,0,198,199,5,3,0,0,199,201,
        1,0,0,0,200,188,1,0,0,0,200,190,1,0,0,0,200,191,1,0,0,0,200,192,
        1,0,0,0,200,193,1,0,0,0,200,194,1,0,0,0,201,210,1,0,0,0,202,203,
        10,1,0,0,203,204,5,12,0,0,204,205,3,28,14,0,205,206,5,11,0,0,206,
        207,3,28,14,2,207,209,1,0,0,0,208,202,1,0,0,0,209,212,1,0,0,0,210,
        208,1,0,0,0,210,211,1,0,0,0,211,29,1,0,0,0,212,210,1,0,0,0,21,33,
        40,58,71,83,90,98,102,114,118,125,127,136,143,151,159,170,173,186,
        200,210
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "'//'", 
                     "'///'", "'['", "','", "']'", "':'", "'?'", "'while'", 
                     "'let'", "'else if'", "'print'", "'return'", "'if'", 
                     "'else'", "'switch'", "'case'", "'default'", "'end switch'", 
                     "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHILE", "LET", "ELIF", "PRINT", "RETURN", 
                      "IF", "ELSE", "SWITCH", "CASE", "DEFAULT", "END_SWITCH", 
                      "PASS", "OPERATOR", "COMPARISON_OP", "BOOLEAN", "INT", 
                      "STRING", "LETTER", "DIGIT", "ID", "LITERAL", "WS", 
                      "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_printStatement = 3
    RULE_whileStatement = 4
    RULE_ifElseStatement = 5
    RULE_switchStatement = 6
    RULE_comment = 7
    RULE_multilineComment = 8
    RULE_iterable = 9
    RULE_array = 10
    RULE_object = 11
    RULE_pair = 12
    RULE_condition = 13
    RULE_expression = 14

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "whileStatement", "ifElseStatement", "switchStatement", 
                   "comment", "multilineComment", "iterable", "array", "object", 
                   "pair", "condition", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    WHILE=13
    LET=14
    ELIF=15
    PRINT=16
    RETURN=17
    IF=18
    ELSE=19
    SWITCH=20
    CASE=21
    DEFAULT=22
    END_SWITCH=23
    PASS=24
    OPERATOR=25
    COMPARISON_OP=26
    BOOLEAN=27
    INT=28
    STRING=29
    LETTER=30
    DIGIT=31
    ID=32
    LITERAL=33
    WS=34
    NEWLINE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MyLangParser.VariableDeclarationContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MyLangParser.PrintStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def ifElseStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfElseStatementContext,0)


        def PASS(self):
            return self.getToken(MyLangParser.PASS, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.variableDeclaration()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.printStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.whileStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.ifElseStatement()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.match(MyLangParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(MyLangParser.LET, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = MyLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MyLangParser.LET)
            self.state = 43
            self.match(MyLangParser.ID)
            self.state = 44
            self.match(MyLangParser.T__0)
            self.state = 45
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyLangParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = MyLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MyLangParser.PRINT)
            self.state = 48
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = MyLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MyLangParser.WHILE)
            self.state = 51
            self.match(MyLangParser.T__1)
            self.state = 52
            self.condition()
            self.state = 53
            self.match(MyLangParser.T__2)
            self.state = 54
            self.match(MyLangParser.T__3)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ConditionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ELIF)
            else:
                return self.getToken(MyLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_ifElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)




    def ifElseStatement(self):

        localctx = MyLangParser.IfElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifElseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MyLangParser.IF)
            self.state = 64
            self.match(MyLangParser.T__1)
            self.state = 65
            self.condition()
            self.state = 66
            self.match(MyLangParser.T__2)
            self.state = 67
            self.match(MyLangParser.T__3)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(MyLangParser.T__4)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 75
                self.match(MyLangParser.ELIF)
                self.state = 76
                self.match(MyLangParser.T__1)
                self.state = 77
                self.condition()
                self.state = 78
                self.match(MyLangParser.T__2)
                self.state = 79
                self.match(MyLangParser.T__3)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0):
                    self.state = 80
                    self.statement()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(MyLangParser.T__4)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 93
                self.match(MyLangParser.ELSE)
                self.state = 94
                self.match(MyLangParser.T__3)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0):
                    self.state = 95
                    self.statement()
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self.match(MyLangParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(MyLangParser.SWITCH, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def END_SWITCH(self):
            return self.getToken(MyLangParser.END_SWITCH, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.CASE)
            else:
                return self.getToken(MyLangParser.CASE, i)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.LITERAL)
            else:
                return self.getToken(MyLangParser.LITERAL, i)

        def DEFAULT(self):
            return self.getToken(MyLangParser.DEFAULT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = MyLangParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MyLangParser.SWITCH)
            self.state = 105
            self.match(MyLangParser.T__1)
            self.state = 106
            self.expression(0)
            self.state = 107
            self.match(MyLangParser.T__2)
            self.state = 108
            self.match(MyLangParser.T__3)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 109
                self.match(MyLangParser.CASE)
                self.state = 110
                self.match(MyLangParser.LITERAL)
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 111
                    self.statement()
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0)):
                        break

                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 121
                self.match(MyLangParser.DEFAULT)
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 122
                    self.statement()
                    self.state = 125 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17129472) != 0)):
                        break



            self.state = 129
            self.match(MyLangParser.T__4)
            self.state = 130
            self.match(MyLangParser.END_SWITCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = MyLangParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(MyLangParser.T__5)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 133
                self.match(MyLangParser.STRING)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultilineCommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_multilineComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultilineComment" ):
                listener.enterMultilineComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultilineComment" ):
                listener.exitMultilineComment(self)




    def multilineComment(self):

        localctx = MyLangParser.MultilineCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multilineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MyLangParser.T__6)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 140
                self.match(MyLangParser.STRING)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(MyLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(MyLangParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(MyLangParser.ObjectContext,0)


        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = MyLangParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_iterable)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.object_()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(MyLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = MyLangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MyLangParser.T__7)
            self.state = 154
            self.expression(0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 155
                self.match(MyLangParser.T__8)
                self.state = 156
                self.expression(0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(MyLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.PairContext)
            else:
                return self.getTypedRuleContext(MyLangParser.PairContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)




    def object_(self):

        localctx = MyLangParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MyLangParser.T__3)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 165
                self.pair()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 166
                    self.match(MyLangParser.T__8)
                    self.state = 167
                    self.pair()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 175
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = MyLangParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MyLangParser.STRING)
            self.state = 178
            self.match(MyLangParser.T__10)
            self.state = 179
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def COMPARISON_OP(self):
            return self.getToken(MyLangParser.COMPARISON_OP, 0)

        def BOOLEAN(self):
            return self.getToken(MyLangParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MyLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4, 8, 28, 29, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expression(0)
                self.state = 182
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 183
                self.expression(0)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(MyLangParser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(MyLangParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(MyLangParser.ObjectContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def OPERATOR(self):
            return self.getToken(MyLangParser.OPERATOR, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 189
                self.match(MyLangParser.INT)
                pass
            elif token in [32]:
                self.state = 190
                self.match(MyLangParser.ID)
                pass
            elif token in [29]:
                self.state = 191
                self.match(MyLangParser.STRING)
                pass
            elif token in [8]:
                self.state = 192
                self.array()
                pass
            elif token in [4]:
                self.state = 193
                self.object_()
                pass
            elif token in [2]:
                self.state = 194
                self.match(MyLangParser.T__1)
                self.state = 195
                self.expression(0)
                self.state = 196
                self.match(MyLangParser.OPERATOR)
                self.state = 197
                self.expression(0)
                self.state = 198
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 202
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 203
                    self.match(MyLangParser.T__11)
                    self.state = 204
                    self.expression(0)
                    self.state = 205
                    self.match(MyLangParser.T__10)
                    self.state = 206
                    self.expression(2) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




