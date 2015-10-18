from mobi6 import MinimalMobiUpdater

def fix_mobi_asin(book_src):

    def apply_fix(file_src):
            asin = 'B00PCJWIC2'

            # with lopen(file_src, 'wb') as f:
            #     db.copy_format_to(book_id, fmt, f, index_is_id=True)

            with open(file_src, 'r+b') as stream:
                mu = MinimalMobiUpdater(stream)
                mu.update(asin, b'EBOK')
                stream.seek(0)

    print 'Fixing'
    apply_fix('/Users/matthijs/ASINFixer/test.azw3')
    print 'Done.'

    return True

if __name__ == "__main__":
    fix_mobi_asin('test')