# Generated from c:/Users/izudd/Desktop/MyLanguage- (4)/MyLang.g4 by ANTLR 4.13.1
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
        4,1,39,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,4,0,44,8,0,11,0,12,0,45,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,58,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,6,1,6,1,6,3,6,100,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,110,8,7,11,7,12,7,111,5,
        7,114,8,7,10,7,12,7,117,9,7,1,7,1,7,4,7,121,8,7,11,7,12,7,122,3,
        7,125,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,5,12,166,
        8,12,10,12,12,12,169,9,12,1,12,1,12,1,13,1,13,5,13,175,8,13,10,13,
        12,13,178,9,13,1,14,1,14,5,14,182,8,14,10,14,12,14,185,9,14,1,14,
        1,14,1,15,1,15,1,15,1,15,3,15,193,8,15,1,16,1,16,1,16,1,16,5,16,
        199,8,16,10,16,12,16,202,9,16,3,16,204,8,16,1,16,1,16,1,16,3,16,
        209,8,16,1,17,1,17,1,17,1,17,5,17,215,8,17,10,17,12,17,218,9,17,
        3,17,220,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,3,19,233,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,248,8,20,1,20,1,20,1,20,1,20,1,20,1,20,
        5,20,256,8,20,10,20,12,20,259,9,20,1,20,0,1,40,21,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,0,274,0,43,1,0,0,0,2,
        57,1,0,0,0,4,59,1,0,0,0,6,64,1,0,0,0,8,67,1,0,0,0,10,75,1,0,0,0,
        12,81,1,0,0,0,14,101,1,0,0,0,16,129,1,0,0,0,18,137,1,0,0,0,20,147,
        1,0,0,0,22,157,1,0,0,0,24,163,1,0,0,0,26,172,1,0,0,0,28,179,1,0,
        0,0,30,192,1,0,0,0,32,208,1,0,0,0,34,210,1,0,0,0,36,223,1,0,0,0,
        38,232,1,0,0,0,40,247,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,45,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,1,1,0,0,0,47,58,3,4,2,0,48,
        58,3,6,3,0,49,58,3,8,4,0,50,58,3,10,5,0,51,58,3,12,6,0,52,58,3,16,
        8,0,53,58,3,18,9,0,54,58,3,20,10,0,55,58,3,22,11,0,56,58,5,30,0,
        0,57,47,1,0,0,0,57,48,1,0,0,0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,
        1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,
        57,56,1,0,0,0,58,3,1,0,0,0,59,60,5,20,0,0,60,61,5,36,0,0,61,62,5,
        1,0,0,62,63,3,40,20,0,63,5,1,0,0,0,64,65,5,22,0,0,65,66,3,40,20,
        0,66,7,1,0,0,0,67,68,5,18,0,0,68,69,5,2,0,0,69,70,3,38,19,0,70,71,
        5,17,0,0,71,72,5,34,0,0,72,73,5,3,0,0,73,74,3,24,12,0,74,9,1,0,0,
        0,75,76,5,18,0,0,76,77,5,2,0,0,77,78,3,38,19,0,78,79,5,3,0,0,79,
        80,3,24,12,0,80,11,1,0,0,0,81,82,5,24,0,0,82,83,5,2,0,0,83,84,3,
        38,19,0,84,85,5,3,0,0,85,94,3,24,12,0,86,87,5,21,0,0,87,88,5,2,0,
        0,88,89,3,38,19,0,89,90,5,3,0,0,90,91,3,24,12,0,91,93,1,0,0,0,92,
        86,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,99,1,0,0,
        0,96,94,1,0,0,0,97,98,5,25,0,0,98,100,3,24,12,0,99,97,1,0,0,0,99,
        100,1,0,0,0,100,13,1,0,0,0,101,102,5,26,0,0,102,103,5,2,0,0,103,
        104,3,40,20,0,104,105,5,3,0,0,105,115,5,4,0,0,106,107,5,27,0,0,107,
        109,5,37,0,0,108,110,3,2,1,0,109,108,1,0,0,0,110,111,1,0,0,0,111,
        109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,106,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,124,1,0,0,0,117,
        115,1,0,0,0,118,120,5,28,0,0,119,121,3,2,1,0,120,119,1,0,0,0,121,
        122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,
        118,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,127,5,5,0,0,127,
        128,5,29,0,0,128,15,1,0,0,0,129,130,5,19,0,0,130,131,5,2,0,0,131,
        132,5,36,0,0,132,133,5,6,0,0,133,134,3,30,15,0,134,135,5,3,0,0,135,
        136,3,24,12,0,136,17,1,0,0,0,137,138,5,19,0,0,138,139,5,2,0,0,139,
        140,5,36,0,0,140,141,5,7,0,0,141,142,5,34,0,0,142,143,5,8,0,0,143,
        144,5,34,0,0,144,145,5,3,0,0,145,146,3,24,12,0,146,19,1,0,0,0,147,
        148,5,19,0,0,148,149,5,2,0,0,149,150,5,34,0,0,150,151,5,8,0,0,151,
        152,5,34,0,0,152,153,5,9,0,0,153,154,5,34,0,0,154,155,5,3,0,0,155,
        156,3,24,12,0,156,21,1,0,0,0,157,158,5,19,0,0,158,159,5,2,0,0,159,
        160,5,34,0,0,160,161,5,3,0,0,161,162,3,24,12,0,162,23,1,0,0,0,163,
        167,5,4,0,0,164,166,3,2,1,0,165,164,1,0,0,0,166,169,1,0,0,0,167,
        165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,
        171,5,5,0,0,171,25,1,0,0,0,172,176,5,10,0,0,173,175,5,35,0,0,174,
        173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,
        27,1,0,0,0,178,176,1,0,0,0,179,183,5,11,0,0,180,182,5,35,0,0,181,
        180,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,
        186,1,0,0,0,185,183,1,0,0,0,186,187,5,11,0,0,187,29,1,0,0,0,188,
        193,3,32,16,0,189,193,3,34,17,0,190,193,5,34,0,0,191,193,5,36,0,
        0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,
        0,193,31,1,0,0,0,194,203,5,12,0,0,195,200,3,40,20,0,196,197,5,13,
        0,0,197,199,3,40,20,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,
        0,0,0,200,201,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,203,195,1,
        0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,209,5,14,0,0,206,207,5,
        12,0,0,207,209,5,14,0,0,208,194,1,0,0,0,208,206,1,0,0,0,209,33,1,
        0,0,0,210,219,5,4,0,0,211,216,3,36,18,0,212,213,5,13,0,0,213,215,
        3,36,18,0,214,212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,219,211,1,0,0,0,219,220,
        1,0,0,0,220,221,1,0,0,0,221,222,5,5,0,0,222,35,1,0,0,0,223,224,5,
        35,0,0,224,225,5,15,0,0,225,226,3,40,20,0,226,37,1,0,0,0,227,228,
        3,40,20,0,228,229,5,32,0,0,229,230,3,40,20,0,230,233,1,0,0,0,231,
        233,5,33,0,0,232,227,1,0,0,0,232,231,1,0,0,0,233,39,1,0,0,0,234,
        235,6,20,-1,0,235,248,5,34,0,0,236,248,5,35,0,0,237,248,5,36,0,0,
        238,248,5,33,0,0,239,248,3,32,16,0,240,248,3,34,17,0,241,242,5,2,
        0,0,242,243,3,40,20,0,243,244,5,31,0,0,244,245,3,40,20,0,245,246,
        5,3,0,0,246,248,1,0,0,0,247,234,1,0,0,0,247,236,1,0,0,0,247,237,
        1,0,0,0,247,238,1,0,0,0,247,239,1,0,0,0,247,240,1,0,0,0,247,241,
        1,0,0,0,248,257,1,0,0,0,249,250,10,1,0,0,250,251,5,16,0,0,251,252,
        3,40,20,0,252,253,5,15,0,0,253,254,3,40,20,2,254,256,1,0,0,0,255,
        249,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,
        41,1,0,0,0,259,257,1,0,0,0,20,45,57,94,99,111,115,122,124,167,176,
        183,192,200,203,208,216,219,232,247,257
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "'in'", 
                     "'from'", "'to'", "'step'", "'unless'", "'do'", "'//'", 
                     "'///'", "'['", "','", "']'", "':'", "'?'", "'limit'", 
                     "'while'", "'for'", "'let'", "'else if'", "'print'", 
                     "'return'", "'if'", "'else'", "'switch'", "'case'", 
                     "'default'", "'end switch'", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LIMIT", "WHILE", 
                      "FOR", "LET", "ELIF", "PRINT", "RETURN", "IF", "ELSE", 
                      "SWITCH", "CASE", "DEFAULT", "END_SWITCH", "PASS", 
                      "OPERATOR", "COMPARISON_OP", "BOOLEAN", "INT", "STRING", 
                      "ID", "LITERAL", "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_printStatement = 3
    RULE_whileLimitStatement = 4
    RULE_whileStatement = 5
    RULE_ifElseStatement = 6
    RULE_switchStatement = 7
    RULE_forEachStatement = 8
    RULE_forRangeStatement = 9
    RULE_forStepStatement = 10
    RULE_forLoopStatement = 11
    RULE_block = 12
    RULE_unlessStatement = 13
    RULE_doWhileStatement = 14
    RULE_comment = 15
    RULE_multilineComment = 16
    RULE_iterable = 17
    RULE_array = 18
    RULE_object = 19
    RULE_pair = 20
    RULE_condition = 21
    RULE_expression = 22

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "whileLimitStatement", "whileStatement", "ifElseStatement", 
                   "switchStatement", "forEachStatement", "forRangeStatement", 
                   "forStepStatement", "forLoopStatement", "block", "unlessStatement", 
                   "doWhileStatement", "comment", "multilineComment", "iterable", 
                   "array", "object", "pair", "condition", "expression" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    LIMIT=19
    WHILE=20
    FOR=21
    LET=22
    ELIF=23
    PRINT=24
    RETURN=25
    IF=26
    ELSE=27
    SWITCH=28
    CASE=29
    DEFAULT=30
    END_SWITCH=31
    PASS=32
    OPERATOR=33
    COMPARISON_OP=34
    BOOLEAN=35
    INT=36
    STRING=37
    ID=38
    LITERAL=39
    WS=40
    NEWLINE=41

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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
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


        def forEachStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForEachStatementContext,0)


        def forRangeStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForRangeStatementContext,0)


        def forStepStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForStepStatementContext,0)


        def forLoopStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForLoopStatementContext,0)


        def unlessStatement(self):
            return self.getTypedRuleContext(MyLangParser.UnlessStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(MyLangParser.DoWhileStatementContext,0)


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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.whileLimitStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.ifElseStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.forEachStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.forRangeStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.forStepStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.forLoopStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
                self.unlessStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 61
                self.doWhileStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 62
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
            self.state = 65
            self.match(MyLangParser.LET)
            self.state = 66
            self.match(MyLangParser.ID)
            self.state = 67
            self.match(MyLangParser.T__0)
            self.state = 68
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
            self.state = 70
            self.match(MyLangParser.PRINT)
            self.state = 71
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

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MyLangParser.WHILE)
            self.state = 74
            self.match(MyLangParser.T__1)
            self.state = 75
            self.condition()
            self.state = 76
            self.match(MyLangParser.LIMIT)
            self.state = 77
            self.match(MyLangParser.INT)
            self.state = 78
            self.match(MyLangParser.T__2)
            self.state = 79
            self.block()
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


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MyLangParser.WHILE)
            self.state = 82
            self.match(MyLangParser.T__1)
            self.state = 83
            self.condition()
            self.state = 84
            self.match(MyLangParser.T__2)
            self.state = 85
            self.block()
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


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


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
            self.state = 87
            self.match(MyLangParser.IF)
            self.state = 88
            self.match(MyLangParser.T__1)
            self.state = 89
            self.condition()
            self.state = 90
            self.match(MyLangParser.T__2)
            self.state = 91
            self.block()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 92
                self.match(MyLangParser.ELIF)
                self.state = 93
                self.match(MyLangParser.T__1)
                self.state = 94
                self.condition()
                self.state = 95
                self.match(MyLangParser.T__2)
                self.state = 96
                self.block()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 103
                self.match(MyLangParser.ELSE)
                self.state = 104
                self.block()


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
            self.state = 107
            self.match(MyLangParser.SWITCH)
            self.state = 108
            self.match(MyLangParser.T__1)
            self.state = 109
            self.expression(0)
            self.state = 110
            self.match(MyLangParser.T__2)
            self.state = 111
            self.match(MyLangParser.T__3)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 112
                self.match(MyLangParser.CASE)
                self.state = 113
                self.match(MyLangParser.LITERAL)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.statement()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
                        break

                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 124
                self.match(MyLangParser.DEFAULT)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.statement()
                    self.state = 128 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
                        break



            self.state = 132
            self.match(MyLangParser.T__4)
            self.state = 133
            self.match(MyLangParser.END_SWITCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForEachStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def iterable(self):
            return self.getTypedRuleContext(MyLangParser.IterableContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forEachStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForEachStatement" ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForEachStatement" ):
                listener.exitForEachStatement(self)




    def forEachStatement(self):

        localctx = MyLangParser.ForEachStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forEachStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MyLangParser.FOR)
            self.state = 136
            self.match(MyLangParser.T__1)
            self.state = 137
            self.match(MyLangParser.ID)
            self.state = 138
            self.match(MyLangParser.T__5)
            self.state = 139
            self.iterable()
            self.state = 140
            self.match(MyLangParser.T__2)
            self.state = 141
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.INT)
            else:
                return self.getToken(MyLangParser.INT, i)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forRangeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForRangeStatement" ):
                listener.enterForRangeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForRangeStatement" ):
                listener.exitForRangeStatement(self)




    def forRangeStatement(self):

        localctx = MyLangParser.ForRangeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forRangeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MyLangParser.FOR)
            self.state = 144
            self.match(MyLangParser.T__1)
            self.state = 145
            self.match(MyLangParser.ID)
            self.state = 146
            self.match(MyLangParser.T__6)
            self.state = 147
            self.match(MyLangParser.INT)
            self.state = 148
            self.match(MyLangParser.T__7)
            self.state = 149
            self.match(MyLangParser.INT)
            self.state = 150
            self.match(MyLangParser.T__2)
            self.state = 151
            self.block()
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

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.INT)
            else:
                return self.getToken(MyLangParser.INT, i)

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
        self.enterRule(localctx, 20, self.RULE_forStepStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MyLangParser.FOR)
            self.state = 154
            self.match(MyLangParser.T__1)
            self.state = 155
            localctx.start = self.match(MyLangParser.INT)
            self.state = 156
            self.match(MyLangParser.T__7)
            self.state = 157
            localctx.goal = self.match(MyLangParser.INT)
            self.state = 158
            self.match(MyLangParser.T__8)
            self.state = 159
            localctx.step = self.match(MyLangParser.INT)
            self.state = 160
            self.match(MyLangParser.T__2)
            self.state = 161
            self.block()
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

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


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
        self.enterRule(localctx, 22, self.RULE_forLoopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MyLangParser.FOR)
            self.state = 164
            self.match(MyLangParser.T__1)
            self.state = 165
            self.match(MyLangParser.INT)
            self.state = 166
            self.match(MyLangParser.T__2)
            self.state = 167
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
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
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MyLangParser.T__3)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 170
                self.statement()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnlessStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_unlessStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlessStatement" ):
                listener.enterUnlessStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlessStatement" ):
                listener.exitUnlessStatement(self)




    def unlessStatement(self):

        localctx = MyLangParser.UnlessStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unlessStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MyLangParser.T__9)
            self.state = 179
            self.match(MyLangParser.T__1)
            self.state = 180
            self.condition()
            self.state = 181
            self.match(MyLangParser.T__2)
            self.state = 182
            self.match(MyLangParser.T__3)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 183
                self.statement()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
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
            return MyLangParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = MyLangParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_doWhileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MyLangParser.T__10)
            self.state = 192
            self.match(MyLangParser.T__3)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 193
                self.statement()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MyLangParser.T__4)
            self.state = 200
            self.match(MyLangParser.WHILE)
            self.state = 201
            self.match(MyLangParser.T__1)
            self.state = 202
            self.condition()
            self.state = 203
            self.match(MyLangParser.T__2)
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
        self.enterRule(localctx, 30, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MyLangParser.T__11)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 206
                self.match(MyLangParser.STRING)
                self.state = 211
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
        self.enterRule(localctx, 32, self.RULE_multilineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MyLangParser.T__12)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 213
                self.match(MyLangParser.STRING)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(MyLangParser.T__12)
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


        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

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
        self.enterRule(localctx, 34, self.RULE_iterable)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.object_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(MyLangParser.INT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
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
        self.enterRule(localctx, 36, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MyLangParser.T__11)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849022996) != 0):
                    self.state = 195
                    self.expression(0)
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==13:
                        self.state = 196
                        self.match(MyLangParser.T__12)
                        self.state = 197
                        self.expression(0)
                        self.state = 202
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 205
                self.match(MyLangParser.T__13)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(MyLangParser.T__11)
                self.state = 207
                self.match(MyLangParser.T__13)
                pass


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
        self.enterRule(localctx, 38, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MyLangParser.T__3)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 211
                self.pair()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 212
                    self.match(MyLangParser.T__12)
                    self.state = 213
                    self.pair()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 221
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
        self.enterRule(localctx, 40, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MyLangParser.STRING)
            self.state = 224
            self.match(MyLangParser.T__14)
            self.state = 225
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
        self.enterRule(localctx, 42, self.RULE_condition)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.expression(0)
                self.state = 228
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 229
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(MyLangParser.BOOLEAN)
                pass


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

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(MyLangParser.BOOLEAN, 0)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 235
                self.match(MyLangParser.INT)
                pass
            elif token in [35]:
                self.state = 236
                self.match(MyLangParser.STRING)
                pass
            elif token in [36]:
                self.state = 237
                self.match(MyLangParser.ID)
                pass
            elif token in [33]:
                self.state = 238
                self.match(MyLangParser.BOOLEAN)
                pass
            elif token in [12]:
                self.state = 239
                self.array()
                pass
            elif token in [4]:
                self.state = 240
                self.object_()
                pass
            elif token in [2]:
                self.state = 241
                self.match(MyLangParser.T__1)
                self.state = 242
                self.expression(0)
                self.state = 243
                self.match(MyLangParser.OPERATOR)
                self.state = 244
                self.expression(0)
                self.state = 245
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 249
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 250
                    self.match(MyLangParser.T__15)
                    self.state = 251
                    self.expression(0)
                    self.state = 252
                    self.match(MyLangParser.T__14)
                    self.state = 253
                    self.expression(2) 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self._predicates[22] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




