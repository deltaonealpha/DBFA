import os, time, sqlite3
global isol, isolx
isol = sqlite3.connect(r'cponmgmtsys.db')
isolx = isol.cursor()
isolx.execute("""CREATE TABLE IF NOT EXISTS cponmaster
    (cponid CHAR,
    cponlim INTEGER,
    cponvalue INTEGER);""")

isol = sqlite3.connect('cponmgmtsys.db')
isolx = isol.cursor()
if os.path.exists(r'cponmgmtsys.db'):
    pass
else:
    isolx.execute("""CREATE TABLE IF NOT EXISTS cponmaster
        (cponid CHAR,
        cponlim INTEGER
        cponvalue INTEGER);""")



def cponissuer(cponid, cponlim, cponvalue):
    isol = sqlite3.connect('cponmgmtsys.db')
    str = "insert into cponmaster(cponid, cponlim, cponvalue) values('%s', '%s', '%s')"
    iox = (cponid, cponlim, cponvalue)
    isolx.execute(str % iox)
    isol.commit()
    print("DSNN: Coupon", cponid, "having discount %", cponvalue, "created for", cponlim, "times of usage.")


def cponuse(cponid):
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    mod = """UPDATE cponmaster SET cponlim = cponlim - 1 WHERE cponid = ?"""
    idler = (cponid, )
    isolx.execute(mod, idler)
    isol.commit()


def cpon_singlefetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponid, cponlim, cponvalue FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ','.join(str(v) for v in rows)
    print("DNSS Coupon ", values)

def cpon_valfetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponvalue FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ''.join(str(v) for v in rows)
    print(values[1:-2])
    

def cpon_limfetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponlim FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ''.join(str(v) for v in rows)
    print(values[1:-2])

def cpon_masterfetch():
    isol = sqlite3.connect(r'cponmgmtsys.db')
    isolx = isol.cursor()
    isolx.execute("SELECT DISTINCT cponid, cponlim FROM cponmaster")
    rows = isolx.fetchall()
    for row in rows:
        print(row)
        #print(" ")

def cpon_ischeck(cponid):
    isol = sqlite3.connect(r'cponmgmtsys.db')
    isolx = isol.cursor()
    query='select exists(select 1 from cponmaster where cponid=? collate nocase) limit 1'
    # 'query' RETURNS 1 IF USERNAME EXISTS OR 0 IF NOT, AS INTEGER(MAYBE). 'collate nocase'= CASE INSENSITIVE, IT'S OPTIONAL
    cponidx = (cponid, )
    check=isolx.execute(query,cponidx) 
    if check.fetchone()[0]==0:
        print('DNSS VOUCHER VALID')

    else:
        print("DNSS Voucher is not valid/ has expired.")
        #try_again=input('Username is not available, try again (any key)/stop (s): ').lower() 
        #if try_again=='s':
            #break

cpon_ischeck("ADsssssssdadfadfeadf eaf weafsX")
cponissuer("ADSX", 50, 5)
cpon_ischeck("ADsSX")