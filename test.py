import clang.cindex as cc

index = cc.Index.create()
tu = index.parse('test.c', options=cc.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
for token in tu.cursor.get_tokens():
    print token.kind, token.cursor.kind, token.spelling, token.location.line, token.location.column