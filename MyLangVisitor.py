# Generated from c:/Users/izudd/Desktop/MyLanguage- (2)/MyLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MyLangParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#printStatement.
    def visitPrintStatement(self, ctx:MyLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileLimitStatement.
    def visitWhileLimitStatement(self, ctx:MyLangParser.WhileLimitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifElseStatement.
    def visitIfElseStatement(self, ctx:MyLangParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#switchStatement.
    def visitSwitchStatement(self, ctx:MyLangParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forEachStatement.
    def visitForEachStatement(self, ctx:MyLangParser.ForEachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forRangeStatement.
    def visitForRangeStatement(self, ctx:MyLangParser.ForRangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forStepStatement.
    def visitForStepStatement(self, ctx:MyLangParser.ForStepStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forLoopStatement.
    def visitForLoopStatement(self, ctx:MyLangParser.ForLoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#comment.
    def visitComment(self, ctx:MyLangParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#multilineComment.
    def visitMultilineComment(self, ctx:MyLangParser.MultilineCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#iterable.
    def visitIterable(self, ctx:MyLangParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array.
    def visitArray(self, ctx:MyLangParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#object.
    def visitObject(self, ctx:MyLangParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#pair.
    def visitPair(self, ctx:MyLangParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#condition.
    def visitCondition(self, ctx:MyLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expression.
    def visitExpression(self, ctx:MyLangParser.ExpressionContext):
        return self.visitChildren(ctx)



del MyLangParser