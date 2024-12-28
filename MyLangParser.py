# Generated from MyLang.g4 by ANTLR 4.13.2
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
        4,1,39,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,68,8,4,11,4,12,
        4,69,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,9,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,105,8,6,10,6,12,6,108,9,6,1,6,1,6,5,
        6,112,8,6,10,6,12,6,115,9,6,1,6,1,6,1,6,5,6,120,8,6,10,6,12,6,123,
        9,6,1,6,3,6,126,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,136,8,7,
        11,7,12,7,137,5,7,140,8,7,10,7,12,7,143,9,7,1,7,1,7,4,7,147,8,7,
        11,7,12,7,148,3,7,151,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,5,8,166,8,8,10,8,12,8,169,9,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,5,9,179,8,9,10,9,12,9,182,9,9,1,9,1,9,1,10,1,10,5,10,
        188,8,10,10,10,12,10,191,9,10,1,11,1,11,5,11,195,8,11,10,11,12,11,
        198,9,11,1,11,1,11,1,12,1,12,1,12,3,12,205,8,12,1,13,1,13,1,13,1,
        13,5,13,211,8,13,10,13,12,13,214,9,13,1,13,1,13,1,14,1,14,1,14,1,
        14,5,14,222,8,14,10,14,12,14,225,9,14,3,14,227,8,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,240,8,16,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,254,8,
        17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,262,8,17,10,17,12,17,265,9,
        17,1,17,0,1,34,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,0,0,283,0,37,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,56,1,0,0,0,8,
        59,1,0,0,0,10,73,1,0,0,0,12,86,1,0,0,0,14,127,1,0,0,0,16,155,1,0,
        0,0,18,172,1,0,0,0,20,185,1,0,0,0,22,192,1,0,0,0,24,204,1,0,0,0,
        26,206,1,0,0,0,28,217,1,0,0,0,30,230,1,0,0,0,32,239,1,0,0,0,34,253,
        1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,1,1,0,0,0,41,50,3,4,2,0,42,50,3,6,3,0,43,50,3,8,
        4,0,44,50,3,10,5,0,45,50,3,12,6,0,46,50,3,16,8,0,47,50,3,18,9,0,
        48,50,5,28,0,0,49,41,1,0,0,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,
        0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,
        3,1,0,0,0,51,52,5,18,0,0,52,53,5,36,0,0,53,54,5,1,0,0,54,55,3,34,
        17,0,55,5,1,0,0,0,56,57,5,20,0,0,57,58,3,34,17,0,58,7,1,0,0,0,59,
        60,5,16,0,0,60,61,5,2,0,0,61,62,3,32,16,0,62,63,5,15,0,0,63,64,5,
        32,0,0,64,65,5,3,0,0,65,67,5,4,0,0,66,68,3,2,1,0,67,66,1,0,0,0,68,
        69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,5,0,
        0,72,9,1,0,0,0,73,74,5,16,0,0,74,75,5,2,0,0,75,76,3,32,16,0,76,77,
        5,3,0,0,77,81,5,4,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,
        81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,
        5,0,0,85,11,1,0,0,0,86,87,5,22,0,0,87,88,5,2,0,0,88,89,3,32,16,0,
        89,90,5,3,0,0,90,94,5,4,0,0,91,93,3,2,1,0,92,91,1,0,0,0,93,96,1,
        0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,
        113,5,5,0,0,98,99,5,19,0,0,99,100,5,2,0,0,100,101,3,32,16,0,101,
        102,5,3,0,0,102,106,5,4,0,0,103,105,3,2,1,0,104,103,1,0,0,0,105,
        108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,
        106,1,0,0,0,109,110,5,5,0,0,110,112,1,0,0,0,111,98,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,125,1,0,0,0,115,113,
        1,0,0,0,116,117,5,23,0,0,117,121,5,4,0,0,118,120,3,2,1,0,119,118,
        1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,
        1,0,0,0,123,121,1,0,0,0,124,126,5,5,0,0,125,116,1,0,0,0,125,126,
        1,0,0,0,126,13,1,0,0,0,127,128,5,24,0,0,128,129,5,2,0,0,129,130,
        3,34,17,0,130,131,5,3,0,0,131,141,5,4,0,0,132,133,5,25,0,0,133,135,
        5,37,0,0,134,136,3,2,1,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,132,1,0,0,0,140,143,
        1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,150,1,0,0,0,143,141,
        1,0,0,0,144,146,5,26,0,0,145,147,3,2,1,0,146,145,1,0,0,0,147,148,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,144,
        1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,5,0,0,153,154,
        5,27,0,0,154,15,1,0,0,0,155,156,5,17,0,0,156,157,5,2,0,0,157,158,
        5,32,0,0,158,159,5,6,0,0,159,160,5,32,0,0,160,161,5,7,0,0,161,162,
        5,32,0,0,162,163,5,3,0,0,163,167,5,4,0,0,164,166,3,2,1,0,165,164,
        1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,170,
        1,0,0,0,169,167,1,0,0,0,170,171,5,5,0,0,171,17,1,0,0,0,172,173,5,
        17,0,0,173,174,5,2,0,0,174,175,5,32,0,0,175,176,5,3,0,0,176,180,
        5,4,0,0,177,179,3,2,1,0,178,177,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,180,1,0,0,0,183,184,
        5,5,0,0,184,19,1,0,0,0,185,189,5,8,0,0,186,188,5,33,0,0,187,186,
        1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,21,1,
        0,0,0,191,189,1,0,0,0,192,196,5,9,0,0,193,195,5,33,0,0,194,193,1,
        0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,
        0,0,0,198,196,1,0,0,0,199,200,5,9,0,0,200,23,1,0,0,0,201,205,3,26,
        13,0,202,205,3,28,14,0,203,205,5,36,0,0,204,201,1,0,0,0,204,202,
        1,0,0,0,204,203,1,0,0,0,205,25,1,0,0,0,206,207,5,10,0,0,207,212,
        3,34,17,0,208,209,5,11,0,0,209,211,3,34,17,0,210,208,1,0,0,0,211,
        214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,
        212,1,0,0,0,215,216,5,12,0,0,216,27,1,0,0,0,217,226,5,4,0,0,218,
        223,3,30,15,0,219,220,5,11,0,0,220,222,3,30,15,0,221,219,1,0,0,0,
        222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,227,1,0,0,0,
        225,223,1,0,0,0,226,218,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,
        228,229,5,5,0,0,229,29,1,0,0,0,230,231,5,33,0,0,231,232,5,13,0,0,
        232,233,3,34,17,0,233,31,1,0,0,0,234,235,3,34,17,0,235,236,5,30,
        0,0,236,237,3,34,17,0,237,240,1,0,0,0,238,240,5,31,0,0,239,234,1,
        0,0,0,239,238,1,0,0,0,240,33,1,0,0,0,241,242,6,17,-1,0,242,254,5,
        32,0,0,243,254,5,36,0,0,244,254,5,33,0,0,245,254,3,26,13,0,246,254,
        3,28,14,0,247,248,5,2,0,0,248,249,3,34,17,0,249,250,5,29,0,0,250,
        251,3,34,17,0,251,252,5,3,0,0,252,254,1,0,0,0,253,241,1,0,0,0,253,
        243,1,0,0,0,253,244,1,0,0,0,253,245,1,0,0,0,253,246,1,0,0,0,253,
        247,1,0,0,0,254,263,1,0,0,0,255,256,10,1,0,0,256,257,5,14,0,0,257,
        258,3,34,17,0,258,259,5,13,0,0,259,260,3,34,17,2,260,262,1,0,0,0,
        261,255,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,
        264,35,1,0,0,0,265,263,1,0,0,0,24,39,49,69,81,94,106,113,121,125,
        137,141,148,150,167,180,189,196,204,212,223,226,239,253,263
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "'to'", 
                     "'step'", "'//'", "'///'", "'['", "','", "']'", "':'", 
                     "'?'", "'limit'", "'while'", "'for'", "'let'", "'else if'", 
                     "'print'", "'return'", "'if'", "'else'", "'switch'", 
                     "'case'", "'default'", "'end switch'", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LIMIT", "WHILE", 
                      "FOR", "LET", "ELIF", "PRINT", "RETURN", "IF", "ELSE", 
                      "SWITCH", "CASE", "DEFAULT", "END_SWITCH", "PASS", 
                      "OPERATOR", "COMPARISON_OP", "BOOLEAN", "INT", "STRING", 
                      "LETTER", "DIGIT", "ID", "LITERAL", "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_printStatement = 3
    RULE_whileLimitStatement = 4
    RULE_whileStatement = 5
    RULE_ifElseStatement = 6
    RULE_switchStatement = 7
    RULE_forStepStatement = 8
    RULE_forLoopStatement = 9
    RULE_comment = 10
    RULE_multilineComment = 11
    RULE_iterable = 12
    RULE_array = 13
    RULE_object = 14
    RULE_pair = 15
    RULE_condition = 16
    RULE_expression = 17

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "whileLimitStatement", "whileStatement", "ifElseStatement", 
                   "switchStatement", "forStepStatement", "forLoopStatement", 
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
    T__12=13
    T__13=14
    LIMIT=15
    WHILE=16
    FOR=17
    LET=18
    ELIF=19
    PRINT=20
    RETURN=21
    IF=22
    ELSE=23
    SWITCH=24
    CASE=25
    DEFAULT=26
    END_SWITCH=27
    PASS=28
    OPERATOR=29
    COMPARISON_OP=30
    BOOLEAN=31
    INT=32
    STRING=33
    LETTER=34
    DIGIT=35
    ID=36
    LITERAL=37
    WS=38
    NEWLINE=39

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0)):
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


        def whileLimitStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileLimitStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def ifElseStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfElseStatementContext,0)


        def forStepStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForStepStatementContext,0)


        def forLoopStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForLoopStatementContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.whileLimitStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.ifElseStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.forStepStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.forLoopStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 48
                self.match(MyLangParser.PASS)
                pass


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
            self.state = 51
            self.match(MyLangParser.LET)
            self.state = 52
            self.match(MyLangParser.ID)
            self.state = 53
            self.match(MyLangParser.T__0)
            self.state = 54
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
            self.state = 56
            self.match(MyLangParser.PRINT)
            self.state = 57
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLimitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def LIMIT(self):
            return self.getToken(MyLangParser.LIMIT, 0)

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileLimitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLimitStatement" ):
                listener.enterWhileLimitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLimitStatement" ):
                listener.exitWhileLimitStatement(self)




    def whileLimitStatement(self):

        localctx = MyLangParser.WhileLimitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileLimitStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MyLangParser.WHILE)
            self.state = 60
            self.match(MyLangParser.T__1)
            self.state = 61
            self.condition()
            self.state = 62
            self.match(MyLangParser.LIMIT)
            self.state = 63
            self.match(MyLangParser.INT)
            self.state = 64
            self.match(MyLangParser.T__2)
            self.state = 65
            self.match(MyLangParser.T__3)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.statement()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0)):
                    break

            self.state = 71
            self.match(MyLangParser.T__4)
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
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MyLangParser.WHILE)
            self.state = 74
            self.match(MyLangParser.T__1)
            self.state = 75
            self.condition()
            self.state = 76
            self.match(MyLangParser.T__2)
            self.state = 77
            self.match(MyLangParser.T__3)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
        self.enterRule(localctx, 12, self.RULE_ifElseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MyLangParser.IF)
            self.state = 87
            self.match(MyLangParser.T__1)
            self.state = 88
            self.condition()
            self.state = 89
            self.match(MyLangParser.T__2)
            self.state = 90
            self.match(MyLangParser.T__3)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MyLangParser.T__4)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 98
                self.match(MyLangParser.ELIF)
                self.state = 99
                self.match(MyLangParser.T__1)
                self.state = 100
                self.condition()
                self.state = 101
                self.match(MyLangParser.T__2)
                self.state = 102
                self.match(MyLangParser.T__3)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                    self.state = 103
                    self.statement()
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.match(MyLangParser.T__4)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 116
                self.match(MyLangParser.ELSE)
                self.state = 117
                self.match(MyLangParser.T__3)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                    self.state = 118
                    self.statement()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
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
        self.enterRule(localctx, 14, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MyLangParser.SWITCH)
            self.state = 128
            self.match(MyLangParser.T__1)
            self.state = 129
            self.expression(0)
            self.state = 130
            self.match(MyLangParser.T__2)
            self.state = 131
            self.match(MyLangParser.T__3)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 132
                self.match(MyLangParser.CASE)
                self.state = 133
                self.match(MyLangParser.LITERAL)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 134
                    self.statement()
                    self.state = 137 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0)):
                        break

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 144
                self.match(MyLangParser.DEFAULT)
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 145
                    self.statement()
                    self.state = 148 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0)):
                        break



            self.state = 152
            self.match(MyLangParser.T__4)
            self.state = 153
            self.match(MyLangParser.END_SWITCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStepStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start = None # Token
            self.goal = None # Token
            self.step = None # Token

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.INT)
            else:
                return self.getToken(MyLangParser.INT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_forStepStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStepStatement" ):
                listener.enterForStepStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStepStatement" ):
                listener.exitForStepStatement(self)




    def forStepStatement(self):

        localctx = MyLangParser.ForStepStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStepStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MyLangParser.FOR)
            self.state = 156
            self.match(MyLangParser.T__1)
            self.state = 157
            localctx.start = self.match(MyLangParser.INT)
            self.state = 158
            self.match(MyLangParser.T__5)
            self.state = 159
            localctx.goal = self.match(MyLangParser.INT)
            self.state = 160
            self.match(MyLangParser.T__6)
            self.state = 161
            localctx.step = self.match(MyLangParser.INT)
            self.state = 162
            self.match(MyLangParser.T__2)
            self.state = 163
            self.match(MyLangParser.T__3)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                self.state = 164
                self.statement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_forLoopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoopStatement" ):
                listener.enterForLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoopStatement" ):
                listener.exitForLoopStatement(self)




    def forLoopStatement(self):

        localctx = MyLangParser.ForLoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forLoopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MyLangParser.FOR)
            self.state = 173
            self.match(MyLangParser.T__1)
            self.state = 174
            self.match(MyLangParser.INT)
            self.state = 175
            self.match(MyLangParser.T__2)
            self.state = 176
            self.match(MyLangParser.T__3)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274137088) != 0):
                self.state = 177
                self.statement()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self.match(MyLangParser.T__4)
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
        self.enterRule(localctx, 20, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(MyLangParser.T__7)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 186
                self.match(MyLangParser.STRING)
                self.state = 191
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
        self.enterRule(localctx, 22, self.RULE_multilineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MyLangParser.T__8)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 193
                self.match(MyLangParser.STRING)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MyLangParser.T__8)
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
        self.enterRule(localctx, 24, self.RULE_iterable)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.object_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
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
        self.enterRule(localctx, 26, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MyLangParser.T__9)
            self.state = 207
            self.expression(0)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 208
                self.match(MyLangParser.T__10)
                self.state = 209
                self.expression(0)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self.match(MyLangParser.T__11)
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
        self.enterRule(localctx, 28, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MyLangParser.T__3)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 218
                self.pair()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 219
                    self.match(MyLangParser.T__10)
                    self.state = 220
                    self.pair()
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 228
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
        self.enterRule(localctx, 30, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MyLangParser.STRING)
            self.state = 231
            self.match(MyLangParser.T__12)
            self.state = 232
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
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4, 10, 32, 33, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.expression(0)
                self.state = 235
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 236
                self.expression(0)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.state = 242
                self.match(MyLangParser.INT)
                pass
            elif token in [36]:
                self.state = 243
                self.match(MyLangParser.ID)
                pass
            elif token in [33]:
                self.state = 244
                self.match(MyLangParser.STRING)
                pass
            elif token in [10]:
                self.state = 245
                self.array()
                pass
            elif token in [4]:
                self.state = 246
                self.object_()
                pass
            elif token in [2]:
                self.state = 247
                self.match(MyLangParser.T__1)
                self.state = 248
                self.expression(0)
                self.state = 249
                self.match(MyLangParser.OPERATOR)
                self.state = 250
                self.expression(0)
                self.state = 251
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 255
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 256
                    self.match(MyLangParser.T__13)
                    self.state = 257
                    self.expression(0)
                    self.state = 258
                    self.match(MyLangParser.T__12)
                    self.state = 259
                    self.expression(2) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self._predicates[17] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




