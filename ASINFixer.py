import sys
from mobi6 import MinimalMobiUpdater

def fix_mobi_asin(book_src, asin):
    def apply_fix(file_src, asin):

            # with lopen(file_src, 'wb') as f:
            #     db.copy_format_to(book_id, fmt, f, index_is_id=True)

            with open(file_src, 'r+b') as stream:
                mu = MinimalMobiUpdater(stream)
                mu.update(asin, b'EBOK')
                stream.seek(0)

    print 'Fixing %s with ASIN: %s' % (book_src, asin)
    apply_fix(book_src, asin)
    print 'Done.'

    return True

def main(argv):
    if len(argv) != 2:
        usage()
        sys.exit(2)

    fix_mobi_asin(argv[0], argv[1])

def usage():
    print 'ASINFixer.py source_path ASIN'

if __name__ == "__main__":
    main(sys.argv[1:])
