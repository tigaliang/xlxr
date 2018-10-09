import clang.cindex as cc

def foo(cursor):
    if cursor.kind.is_declaration():
        print 'Found %s [line=%s, col=%s]' % (cursor.spelling, cursor.location.line, cursor.location.column)
    for c in cursor.get_children():
        foo(c)

index = cc.Index.create()
tu = index.parse('test.c')
print 'Translation unit:', tu.spelling
foo(tu.cursor)