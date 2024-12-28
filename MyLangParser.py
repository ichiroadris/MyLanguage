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
        4,1,41,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,82,8,4,11,4,12,
        4,83,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,94,8,5,10,5,12,5,97,9,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,112,8,6,
        10,6,12,6,115,9,6,1,6,1,6,3,6,119,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,4,7,129,8,7,11,7,12,7,130,5,7,133,8,7,10,7,12,7,136,9,7,1,
        7,1,7,4,7,140,8,7,11,7,12,7,141,3,7,144,8,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,5,8,157,8,8,10,8,12,8,160,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,174,8,9,10,9,12,9,177,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,5,11,197,8,11,10,11,12,11,200,9,11,1,
        11,1,11,1,12,1,12,5,12,206,8,12,10,12,12,12,209,9,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,5,13,219,8,13,10,13,12,13,222,9,13,1,
        13,1,13,1,14,1,14,1,14,5,14,229,8,14,10,14,12,14,232,9,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,15,1,15,5,15,242,8,15,10,15,12,15,245,9,
        15,1,16,1,16,5,16,249,8,16,10,16,12,16,252,9,16,1,16,1,16,1,17,1,
        17,1,17,1,17,3,17,260,8,17,1,18,1,18,1,18,1,18,5,18,266,8,18,10,
        18,12,18,269,9,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,277,8,19,10,
        19,12,19,280,9,19,3,19,282,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,3,21,295,8,21,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,310,8,22,1,22,1,22,1,
        22,1,22,1,22,1,22,5,22,318,8,22,10,22,12,22,321,9,22,1,22,0,1,44,
        23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,0,0,341,0,47,1,0,0,0,2,63,1,0,0,0,4,65,1,0,0,0,6,70,1,0,0,0,8,
        73,1,0,0,0,10,87,1,0,0,0,12,100,1,0,0,0,14,120,1,0,0,0,16,148,1,
        0,0,0,18,163,1,0,0,0,20,180,1,0,0,0,22,190,1,0,0,0,24,203,1,0,0,
        0,26,212,1,0,0,0,28,225,1,0,0,0,30,239,1,0,0,0,32,246,1,0,0,0,34,
        259,1,0,0,0,36,261,1,0,0,0,38,272,1,0,0,0,40,285,1,0,0,0,42,294,
        1,0,0,0,44,309,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,1,0,0,0,
        49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,64,3,4,2,0,52,64,3,6,
        3,0,53,64,3,8,4,0,54,64,3,10,5,0,55,64,3,12,6,0,56,64,3,16,8,0,57,
        64,3,18,9,0,58,64,3,20,10,0,59,64,3,22,11,0,60,64,3,26,13,0,61,64,
        3,28,14,0,62,64,5,32,0,0,63,51,1,0,0,0,63,52,1,0,0,0,63,53,1,0,0,
        0,63,54,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,
        1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,
        64,3,1,0,0,0,65,66,5,22,0,0,66,67,5,38,0,0,67,68,5,1,0,0,68,69,3,
        44,22,0,69,5,1,0,0,0,70,71,5,24,0,0,71,72,3,44,22,0,72,7,1,0,0,0,
        73,74,5,20,0,0,74,75,5,2,0,0,75,76,3,42,21,0,76,77,5,19,0,0,77,78,
        5,36,0,0,78,79,5,3,0,0,79,81,5,4,0,0,80,82,3,2,1,0,81,80,1,0,0,0,
        82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,
        5,0,0,86,9,1,0,0,0,87,88,5,20,0,0,88,89,5,2,0,0,89,90,3,42,21,0,
        90,91,5,3,0,0,91,95,5,4,0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,97,1,
        0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,
        99,5,5,0,0,99,11,1,0,0,0,100,101,5,26,0,0,101,102,5,2,0,0,102,103,
        3,42,21,0,103,104,5,3,0,0,104,113,3,24,12,0,105,106,5,23,0,0,106,
        107,5,2,0,0,107,108,3,42,21,0,108,109,5,3,0,0,109,110,3,24,12,0,
        110,112,1,0,0,0,111,105,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,
        113,114,1,0,0,0,114,118,1,0,0,0,115,113,1,0,0,0,116,117,5,27,0,0,
        117,119,3,24,12,0,118,116,1,0,0,0,118,119,1,0,0,0,119,13,1,0,0,0,
        120,121,5,28,0,0,121,122,5,2,0,0,122,123,3,44,22,0,123,124,5,3,0,
        0,124,134,5,4,0,0,125,126,5,29,0,0,126,128,5,39,0,0,127,129,3,2,
        1,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,133,1,0,0,0,132,125,1,0,0,0,133,136,1,0,0,0,134,132,1,0,
        0,0,134,135,1,0,0,0,135,143,1,0,0,0,136,134,1,0,0,0,137,139,5,30,
        0,0,138,140,3,2,1,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,
        0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,137,1,0,0,0,143,144,1,0,
        0,0,144,145,1,0,0,0,145,146,5,5,0,0,146,147,5,31,0,0,147,15,1,0,
        0,0,148,149,5,21,0,0,149,150,5,2,0,0,150,151,5,38,0,0,151,152,5,
        6,0,0,152,153,3,34,17,0,153,154,5,3,0,0,154,158,5,4,0,0,155,157,
        3,2,1,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,5,5,0,0,162,17,1,
        0,0,0,163,164,5,21,0,0,164,165,5,2,0,0,165,166,5,38,0,0,166,167,
        5,7,0,0,167,168,5,36,0,0,168,169,5,8,0,0,169,170,5,36,0,0,170,171,
        5,3,0,0,171,175,5,4,0,0,172,174,3,2,1,0,173,172,1,0,0,0,174,177,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,175,
        1,0,0,0,178,179,5,5,0,0,179,19,1,0,0,0,180,181,5,21,0,0,181,182,
        5,2,0,0,182,183,5,36,0,0,183,184,5,8,0,0,184,185,5,36,0,0,185,186,
        5,9,0,0,186,187,5,36,0,0,187,188,5,3,0,0,188,189,3,24,12,0,189,21,
        1,0,0,0,190,191,5,21,0,0,191,192,5,2,0,0,192,193,5,36,0,0,193,194,
        5,3,0,0,194,198,5,4,0,0,195,197,3,2,1,0,196,195,1,0,0,0,197,200,
        1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,
        1,0,0,0,201,202,5,5,0,0,202,23,1,0,0,0,203,207,5,4,0,0,204,206,3,
        2,1,0,205,204,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,
        0,0,0,208,210,1,0,0,0,209,207,1,0,0,0,210,211,5,5,0,0,211,25,1,0,
        0,0,212,213,5,10,0,0,213,214,5,2,0,0,214,215,3,42,21,0,215,216,5,
        3,0,0,216,220,5,4,0,0,217,219,3,2,1,0,218,217,1,0,0,0,219,222,1,
        0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,
        0,0,0,223,224,5,5,0,0,224,27,1,0,0,0,225,226,5,11,0,0,226,230,5,
        4,0,0,227,229,3,2,1,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,
        0,0,0,230,231,1,0,0,0,231,233,1,0,0,0,232,230,1,0,0,0,233,234,5,
        5,0,0,234,235,5,20,0,0,235,236,5,2,0,0,236,237,3,42,21,0,237,238,
        5,3,0,0,238,29,1,0,0,0,239,243,5,12,0,0,240,242,5,37,0,0,241,240,
        1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,31,1,
        0,0,0,245,243,1,0,0,0,246,250,5,13,0,0,247,249,5,37,0,0,248,247,
        1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,253,
        1,0,0,0,252,250,1,0,0,0,253,254,5,13,0,0,254,33,1,0,0,0,255,260,
        3,36,18,0,256,260,3,38,19,0,257,260,5,36,0,0,258,260,5,38,0,0,259,
        255,1,0,0,0,259,256,1,0,0,0,259,257,1,0,0,0,259,258,1,0,0,0,260,
        35,1,0,0,0,261,262,5,14,0,0,262,267,3,44,22,0,263,264,5,15,0,0,264,
        266,3,44,22,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,0,0,270,271,5,16,0,0,271,
        37,1,0,0,0,272,281,5,4,0,0,273,278,3,40,20,0,274,275,5,15,0,0,275,
        277,3,40,20,0,276,274,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,281,273,1,0,0,0,281,
        282,1,0,0,0,282,283,1,0,0,0,283,284,5,5,0,0,284,39,1,0,0,0,285,286,
        5,37,0,0,286,287,5,17,0,0,287,288,3,44,22,0,288,41,1,0,0,0,289,290,
        3,44,22,0,290,291,5,34,0,0,291,292,3,44,22,0,292,295,1,0,0,0,293,
        295,5,35,0,0,294,289,1,0,0,0,294,293,1,0,0,0,295,43,1,0,0,0,296,
        297,6,22,-1,0,297,310,5,36,0,0,298,310,5,37,0,0,299,310,5,38,0,0,
        300,310,5,35,0,0,301,310,3,36,18,0,302,310,3,38,19,0,303,304,5,2,
        0,0,304,305,3,44,22,0,305,306,5,33,0,0,306,307,3,44,22,0,307,308,
        5,3,0,0,308,310,1,0,0,0,309,296,1,0,0,0,309,298,1,0,0,0,309,299,
        1,0,0,0,309,300,1,0,0,0,309,301,1,0,0,0,309,302,1,0,0,0,309,303,
        1,0,0,0,310,319,1,0,0,0,311,312,10,1,0,0,312,313,5,18,0,0,313,314,
        3,44,22,0,314,315,5,17,0,0,315,316,3,44,22,2,316,318,1,0,0,0,317,
        311,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,
        45,1,0,0,0,321,319,1,0,0,0,25,49,63,83,95,113,118,130,134,141,143,
        158,175,198,207,220,230,243,250,259,267,278,281,294,309,319
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
            self.match(MyLangParser.T__3)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.statement()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
                    break

            self.state = 85
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
            self.state = 87
            self.match(MyLangParser.WHILE)
            self.state = 88
            self.match(MyLangParser.T__1)
            self.state = 89
            self.condition()
            self.state = 90
            self.match(MyLangParser.T__2)
            self.state = 91
            self.match(MyLangParser.T__3)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 92
                self.statement()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
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
            self.state = 100
            self.match(MyLangParser.IF)
            self.state = 101
            self.match(MyLangParser.T__1)
            self.state = 102
            self.condition()
            self.state = 103
            self.match(MyLangParser.T__2)
            self.state = 104
            self.block()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 105
                self.match(MyLangParser.ELIF)
                self.state = 106
                self.match(MyLangParser.T__1)
                self.state = 107
                self.condition()
                self.state = 108
                self.match(MyLangParser.T__2)
                self.state = 109
                self.block()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 116
                self.match(MyLangParser.ELSE)
                self.state = 117
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
            self.state = 120
            self.match(MyLangParser.SWITCH)
            self.state = 121
            self.match(MyLangParser.T__1)
            self.state = 122
            self.expression(0)
            self.state = 123
            self.match(MyLangParser.T__2)
            self.state = 124
            self.match(MyLangParser.T__3)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 125
                self.match(MyLangParser.CASE)
                self.state = 126
                self.match(MyLangParser.LITERAL)
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 127
                    self.statement()
                    self.state = 130 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
                        break

                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 137
                self.match(MyLangParser.DEFAULT)
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.statement()
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0)):
                        break



            self.state = 145
            self.match(MyLangParser.T__4)
            self.state = 146
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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MyLangParser.FOR)
            self.state = 149
            self.match(MyLangParser.T__1)
            self.state = 150
            self.match(MyLangParser.ID)
            self.state = 151
            self.match(MyLangParser.T__5)
            self.state = 152
            self.iterable()
            self.state = 153
            self.match(MyLangParser.T__2)
            self.state = 154
            self.match(MyLangParser.T__3)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 155
                self.statement()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(MyLangParser.T__4)
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MyLangParser.FOR)
            self.state = 164
            self.match(MyLangParser.T__1)
            self.state = 165
            self.match(MyLangParser.ID)
            self.state = 166
            self.match(MyLangParser.T__6)
            self.state = 167
            self.match(MyLangParser.INT)
            self.state = 168
            self.match(MyLangParser.T__7)
            self.state = 169
            self.match(MyLangParser.INT)
            self.state = 170
            self.match(MyLangParser.T__2)
            self.state = 171
            self.match(MyLangParser.T__3)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 172
                self.statement()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(MyLangParser.T__4)
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
            self.state = 180
            self.match(MyLangParser.FOR)
            self.state = 181
            self.match(MyLangParser.T__1)
            self.state = 182
            localctx.start = self.match(MyLangParser.INT)
            self.state = 183
            self.match(MyLangParser.T__7)
            self.state = 184
            localctx.goal = self.match(MyLangParser.INT)
            self.state = 185
            self.match(MyLangParser.T__8)
            self.state = 186
            localctx.step = self.match(MyLangParser.INT)
            self.state = 187
            self.match(MyLangParser.T__2)
            self.state = 188
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
        self.enterRule(localctx, 22, self.RULE_forLoopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MyLangParser.FOR)
            self.state = 191
            self.match(MyLangParser.T__1)
            self.state = 192
            self.match(MyLangParser.INT)
            self.state = 193
            self.match(MyLangParser.T__2)
            self.state = 194
            self.match(MyLangParser.T__3)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 195
                self.statement()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(MyLangParser.T__4)
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
            self.state = 203
            self.match(MyLangParser.T__3)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 204
                self.statement()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
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
            self.state = 212
            self.match(MyLangParser.T__9)
            self.state = 213
            self.match(MyLangParser.T__1)
            self.state = 214
            self.condition()
            self.state = 215
            self.match(MyLangParser.T__2)
            self.state = 216
            self.match(MyLangParser.T__3)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 217
                self.statement()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
            self.state = 225
            self.match(MyLangParser.T__10)
            self.state = 226
            self.match(MyLangParser.T__3)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4386196480) != 0):
                self.state = 227
                self.statement()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            self.match(MyLangParser.T__4)
            self.state = 234
            self.match(MyLangParser.WHILE)
            self.state = 235
            self.match(MyLangParser.T__1)
            self.state = 236
            self.condition()
            self.state = 237
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
            self.state = 239
            self.match(MyLangParser.T__11)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 240
                self.match(MyLangParser.STRING)
                self.state = 245
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
            self.state = 246
            self.match(MyLangParser.T__12)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 247
                self.match(MyLangParser.STRING)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
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
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.object_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(MyLangParser.INT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
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
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MyLangParser.T__13)
            self.state = 262
            self.expression(0)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 263
                self.match(MyLangParser.T__14)
                self.state = 264
                self.expression(0)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self.match(MyLangParser.T__15)
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
            self.state = 272
            self.match(MyLangParser.T__3)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 273
                self.pair()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 274
                    self.match(MyLangParser.T__14)
                    self.state = 275
                    self.pair()
                    self.state = 280
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 283
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
            self.state = 285
            self.match(MyLangParser.STRING)
            self.state = 286
            self.match(MyLangParser.T__16)
            self.state = 287
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.expression(0)
                self.state = 290
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 291
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.state = 297
                self.match(MyLangParser.INT)
                pass
            elif token in [37]:
                self.state = 298
                self.match(MyLangParser.STRING)
                pass
            elif token in [38]:
                self.state = 299
                self.match(MyLangParser.ID)
                pass
            elif token in [35]:
                self.state = 300
                self.match(MyLangParser.BOOLEAN)
                pass
            elif token in [14]:
                self.state = 301
                self.array()
                pass
            elif token in [4]:
                self.state = 302
                self.object_()
                pass
            elif token in [2]:
                self.state = 303
                self.match(MyLangParser.T__1)
                self.state = 304
                self.expression(0)
                self.state = 305
                self.match(MyLangParser.OPERATOR)
                self.state = 306
                self.expression(0)
                self.state = 307
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 311
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 312
                    self.match(MyLangParser.T__17)
                    self.state = 313
                    self.expression(0)
                    self.state = 314
                    self.match(MyLangParser.T__16)
                    self.state = 315
                    self.expression(2) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
         




