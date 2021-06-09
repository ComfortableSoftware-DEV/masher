#!/usr/bin/python


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# FM.py is copied, along with the appropriate FMxxxxxx.py file from CONFIGDIR to local by pythonUnitsLink.py
# make sure if you change the modules, you also update the stored copy FMxxxxxx.py TBGLST file when you update FM.py
# CF.py is always linked, make sure to update CFTOP.py and SCTN0102 when FM.py or CF.py are changed
# all other units are loaded dynamically by pythonUnitsLink.py using the SCTN16 structure, FMSCTNENABLED.py file locally, etc.
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeADict(dictName_, dictComment_, dictItems_):
# * def makeAList(listName_, listComment_, listItems_):
# * def makeATupDict(tupDictName_, tupDictItems_, tupDictSidecar_):
# * def makeAWideComment(comment_):
# * def makeCF():
# * def makeDBSQLT()
# * def makeDO():
# * def makeDOHBI():
# * def makeFM():
# * def makeFO():
# * def makeSP():
# * def parseTBGLST(FDTBGLST):
# * def readFileToStr(FILENAME_):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def __main__():


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0001 _CHR_ _CONST_
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BKQT = "`"  # BACK TICK
BKSLSH = "\\"  # BACKSLASH
CBRCE = "}"  # CLOSEBRACE
CBRKT = "]"  # CLOSEBRACKET
CPAREN = ")"  # CLOSE PARENTHESIS
CRSTR = "\r"  # carriage return
DBLQT = "\""  # DOUBLE QUOTE
ESC = "\x1b"
NEWLINE = "\n"  # NEWLINE
OBRCE = "{"  # OPENBRACE
OBRKT = "["  # OPENBRACKET
OPAREN = "("  # OPENPAREN
SGLQT = "'"  # simple ' character
SPCSTR = " "  # SPACE character"
TABSTR = "\t"  # TAB

CMNTLEN = 200
CONFIGDIR = "/rcr/0-units/python/"
FOLDLEN = 200
TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""
CACHE_DIR = "/home/will/.cache/"
CONFIG_DIR = "/home/will/.config/"


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


AO_NAME = "newAO.py"
AOTOP_NAME = f"""{CONFIGDIR}AOTOP.py"""
BIN04 = lambda __X__: f"""{__X__:04b}"""
BIN08 = lambda __X__: f"""{__X__:08b}"""
BIN16 = lambda __X__: f"""{__X__:016b}"""
BIN32 = lambda __X__: f"""{__X__:032b}"""
BIN64 = lambda __X__: f"""{__X__:064b}"""
CF_NAME = "newCF.py"
CFTOP_NAME = f"""{CONFIGDIR}CFTOP.py"""
CLRALL = f"""{ESC}[2J"""
CLRDOWN = f"""{ESC}[J"""
CLREOL = f"""{ESC}[K"""
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DBSQLT_NAME = "newDBSQLT.py"
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
DO_NAME = "newDO.py"
DOHBI_NAME = "newDOHBI.py"
DOHBIBTM_NAME = f"""{CONFIGDIR}DO_HBIBTM.py"""
DOHBITOP_NAME = f"""{CONFIGDIR}DO_HBITOP.py"""
DOTOP_NAME = f"""{CONFIGDIR}DOTOP.py"""
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTY_TUPLE = ()
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
FM_NAME = "newFM.py"
FMTOP_NAME = f"""{CONFIGDIR}FMTOP.py"""
FO_NAME = "newFO.py"
FOLD1ENDHERE = f"""# fold here {"⥣1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⥣1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⥥1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⥥1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⥣2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⥣2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⥥2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⥥2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⥣3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⥣3" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⥥3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⥥3" * (FOLDLEN // 2)}{NEWLINE}"""
FOTOP_NAME = f"""{CONFIGDIR}FOTOP.py"""
HEX08 = lambda __X__: f"""{__X__:02H}"""  # {thisComment_}
HEX16 = lambda __X__: f"""{__X__:04H}"""  # {thisComment_}
HEX32 = lambda __X__: f"""{__X__:08H}"""  # {thisComment_}
HEX64 = lambda __X__: f"""{__X__:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line
IO_NAME = "newIO.py"
IOTOP_NAME = f"""{CONFIGDIR}IOTOP.py"""
LINESUP = lambda __NUM__: f"""{ESC}[{__NUM__}A"""
MARK1END = lambda __TAG__: f"""# {"⥣1 " * (CMNTLEN // 3)} {__TAG__}"""
MARK1ENDLN = lambda __TAG__: f"""# {"⥣1 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK1MID = lambda __TAG__: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK1MIDLN = lambda __TAG__: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK1START = lambda __TAG__: f"""# {"1⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK1STARTLN = lambda __TAG__: f"""# {"1⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2END = lambda __TAG__: f"""# {"⥣2 " * (CMNTLEN // 3)} {__TAG__}"""
MARK2ENDLN = lambda __TAG__: f"""# {"⥣2 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2MID = lambda __TAG__: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK2MIDLN = lambda __TAG__: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK2START = lambda __TAG__: f"""# {"2⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK2STARTLN = lambda __TAG__: f"""# {"2⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3END = lambda __TAG__: f"""# {"⥣3 " * (CMNTLEN // 3)} {__TAG__}"""
MARK3ENDLN = lambda __TAG__: f"""# {"⥣3 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3MID = lambda __TAG__: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK3MIDLN = lambda __TAG__: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK3START = lambda __TAG__: f"""# {"3⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK3STARTLN = lambda __TAG__: f"""# {"3⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4END = lambda __TAG__: f"""# {"⥣4 " * (CMNTLEN // 3)} {__TAG__}"""
MARK4ENDLN = lambda __TAG__: f"""# {"⥣4 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4MID = lambda __TAG__: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK4MIDLN = lambda __TAG__: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK4START = lambda __TAG__: f"""# {"4⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK4STARTLN = lambda __TAG__: f"""# {"4⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5END = lambda __TAG__: f"""# {"⥣5 " * (CMNTLEN // 3)} {__TAG__}"""
MARK5ENDLN = lambda __TAG__: f"""# {"⥣5 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5MID = lambda __TAG__: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK5MIDLN = lambda __TAG__: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK5START = lambda __TAG__: f"""# {"5⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK5STARTLN = lambda __TAG__: f"""# {"5⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6END = lambda __TAG__: f"""# {"⥣6 " * (CMNTLEN // 3)} {__TAG__}"""
MARK6ENDLN = lambda __TAG__: f"""# {"⥣6 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6MID = lambda __TAG__: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK6MIDLN = lambda __TAG__: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK6START = lambda __TAG__: f"""# {"6⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK6STARTLN = lambda __TAG__: f"""# {"6⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7END = lambda __TAG__: f"""# {"⥣7 " * (CMNTLEN // 3)} {__TAG__}"""
MARK7ENDLN = lambda __TAG__: f"""# {"⥣7 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7MID = lambda __TAG__: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK7MIDLN = lambda __TAG__: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK7START = lambda __TAG__: f"""# {"7⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK7STARTLN = lambda __TAG__: f"""# {"7⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8END = lambda __TAG__: f"""# {"⥣8 " * (CMNTLEN // 3)} {__TAG__}"""
MARK8ENDLN = lambda __TAG__: f"""# {"⥣8 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8MID = lambda __TAG__: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK8MIDLN = lambda __TAG__: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK8START = lambda __TAG__: f"""# {"8⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK8STARTLN = lambda __TAG__: f"""# {"8⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9END = lambda __TAG__: f"""# {"⥣9 " * (CMNTLEN // 3)} {__TAG__}"""
MARK9ENDLN = lambda __TAG__: f"""# {"⥣9 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9MID = lambda __TAG__: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK9MIDLN = lambda __TAG__: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK9START = lambda __TAG__: f"""# {"9⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK9STARTLN = lambda __TAG__: f"""# {"9⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARKLINES_NAME = f"""{CONFIGDIR}MARKLINES.py"""
MOVELEFT = lambda __NUM__: f"""{ESC}[{__NUM__}D"""
MOVETO = lambda __LN__, __COL__: f"""{ESC}[{__LN__};{__COL__}H"""
NCR = lambda __NUM__: f"""{CRSTR * __NUM__}"""
NNL = lambda __NUM__: f"""{NEWLINE * __NUM__}"""
NSPC = lambda __NUM__: f"""{SPCSTR * __NUM__}"""  # returns a string with __NUM__ SPC
NTAB = lambda __NUM__: f"""{TABSTR * __NUM__}"""  # returns a string with __NUM__ TAB
PSG_NAME = f"""newPSG.py"""
PSGTOP_NAME = f"""{CONFIGDIR}PSGTOP.py"""
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SCTN0102NAME = f"""{CONFIGDIR}SCTN0102.py"""
SCTNSNAME = f"""{CONFIGDIR}SCTNS.md"""
SERIALNUMBER = lambda __NUM__: f"""{(__NUM__ % 0XFFFFFFFF):08X}"""
SP_NAME = "newSP.py"
SPTOP_NAME = f"""{CONFIGDIR}SPTOP.py"""
TBGLST_NAME = "TBGLST.py"
USER_CACHE_URL = lambda __FILENAME__: f"""{USER_CACHE_DIR}{__FILENAME__}"""
USER_CONFIG_URL = lambda __FILENAME__: f"""{USER_CONFIG_DIR}{__FILENAME__}"""
VO_NAME = "newVO.py"
VOTOP_NAME = f"""{CONFIGDIR}VOTOP.py"""
WHIRLCOUNT = 0
WHIRLSTR = f"""-{BKSLSH}|/*"""


DAYMS = (60 * 60 * 24 * 1000)  # 86400000
DAYSECS = (60 * 60 * 24)  # 86400
HALFDAYSECS = (60 * 60 * 12)  # 43200
HALFHOURSECS = (60 * 30)  # 1800
HOURSECS = (60 * 60)  # 3600
MINUTESECS = 60 # 60
QUARTERDAYSECS = (60 * 60 * 6)
QUARTERHOURSECS = (60 * 15)  # 900
TIME995959 = (60 * 60 * 100)  # 360000


STR_SUBST_DICT = {
	"%CBRCE%": f"""{CBRCE}""",
	"%CBRKT%": f"""{CBRKT}""",
	"%CPAREN%": f"""{CPAREN}""",
	"%DQ%": f"""{DBLQT}""",
	"%ESCLN%": f""" {BKSLSH}{NEWLINE}""",
	"%FOLDLN1E%": f"""{FOLD1ENDHERELN}""",
	"%FOLDLN2E%": f"""{FOLD2ENDHERELN}""",
	"%FOLDLN3E%": f"""{FOLD3ENDHERELN}""",
	"%FOLDLN1S%": f"""{FOLD1STARTHERELN}""",
	"%FOLDLN2S%": f"""{FOLD2STARTHERELN}""",
	"%FOLDLN3S%": f"""{FOLD3STARTHERELN}""",
	"%FTQ%": f"""f{TRIQT}""",
	"%FTQTQ%": f"""f{TRIQT}{TRIQT}""",
	"%NEWLINE%": f"""{NEWLINE}""",
	"%OBRCE%": f"""{OBRCE}""",
	"%OBRKT%": f"""{OBRKT}""",
	"%OPAREN%": f"""{OPAREN}""",
	"%SQ%": f"""{SGLQT}""",
	"%TAB1%": f"""{NTAB(1)}""",
	"%TAB2%": f"""{NTAB(2)}""",
	"%TAB3%": f"""{NTAB(3)}""",
	"%TAB4%": f"""{NTAB(4)}""",
	"%TAB5%": f"""{NTAB(5)}""",
	"%TAB6%": f"""{NTAB(6)}""",
	"%TAB7%": f"""{NTAB(7)}""",
	"%TAB8%": f"""{NTAB(8)}""",
	"%TAB9%": f"""{NTAB(9)}""",
	"%TABA%": f"""{NTAB(10)}""",
	"%TQ%": f"""{TRIQT}""",
}


CODES2STRIP = [  # {'CODES2STRIP': "dict holding all of the things to strip from 'text' strings like color codes"}
	f"{ESC}[0m",  # entry for ESC-[0m
	f"{ESC}[1m",  # entry for ESC-[1m
	f"{ESC}[32m",  # entry for ESC-[32m
	f"{ESC}[35m",  # entry for ESC-[35m
	f"{ESC}[36m",  # entry for ESC-[36m
]
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0003 TYPEs and lambda
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0004 BTNS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BTNGHAT_DN = "BTNGHAT_DN"  # artificial button for the hat on gamepads
BTNGHAT_DNLT = "BTNGHAT_DNLT"  # artificial button for the hat on gamepads
BTNGHAT_DNRT = "BTNGHAT_DNRT"  # artificial button for the hat on gamepads
BTNGHAT_LT = "BTNGHAT_LT"  # artificial button for the hat on gamepads
BTNGHAT_RLS = "BTNGHAT_RLS"  # artifical button release for hat on gamepads
BTNGHAT_RT = "BTNGHAT_RT"  # artificial button for the hat on gamepads
BTNGHAT_UP = "BTNGHAT_UP"  # artificial button for the hat on gamepads
BTNGHAT_UPLT = "BTNGHAT_UPLT"  # artificial button for the hat on gamepads
BTNGHAT_UPRT = "BTNGHAT_UPRT"  # artificial button for the hat on gamepads
BTNGLTSTK_DN = "BTNGLTSTK_DN"  # artificial button for left stick on gamepads
BTNGLTSTK_DNLT = "BTNGLTSTK_DNLT"  # artificial button for left stick on gamepads
BTNGLTSTK_DNRT = "BTNGLTSTK_DNRT"  # artificial button for left stick on gamepads
BTNGLTSTK_LT = "BTNGLTSTK_LT"  # artificial button for left stick on gamepads
BTNGLTSTK_RLS = "BTNGLTSTK_RLS"  # artificial button release for LTSTK on gamepads
BTNGLTSTK_RT = "BTNGLTSTK_RT"  # artificial button for left stick on gamepads
BTNGLTSTK_UP = "BTNGLTSTK_UP"  # artificial button for left stick on gamepads
BTNGLTSTK_UPLT = "BTNGLTSTK_UPLT"  # artificial button for left stick on gamepads
BTNGLTSTK_UPRT = "BTNGLTSTK_UPRT"  # artificial button for left stick on gamepads
BTNGRTSTK_DN = "BTNGRTSTK_DN"  # artificial button for left stick on gamepads
BTNGRTSTK_DNLT = "BTNGRTSTK_DNLT"  # artificial button for left stick on gamepads
BTNGRTSTK_DNRT = "BTNGRTSTK_DNRT"  # artificial button for left stick on gamepads
BTNGRTSTK_LT = "BTNGRTSTK_LT"  # artificial button for left stick on gamepads
BTNGRTSTK_RLS = "BTNGRTSTK_RLS"  # artificial button release for RTSTK on gamepads
BTNGRTSTK_RT = "BTNGRTSTK_RT"  # artificial button for left stick on gamepads
BTNGRTSTK_UP = "BTNGRTSTK_UP"  # artificial button for left stick on gamepads
BTNGRTSTK_UPLT = "BTNGRTSTK_UPLT"  # artificial button for left stick on gamepads
BTNGRTSTK_UPRT = "BTNGRTSTK_UPRT"  # artificial button for left stick on gamepads
BTNG_01 = "BTNG_01"  # BTNG001/X on gamepads
BTNG_02 = "BTNG_02"  # BTNG002/A on gamepads
BTNG_03 = "BTNG_03"  # BTNG003/B on gamepads
BTNG_04 = "BTNG_04"  # BTNG004/Y on gamepads
BTNG_05 = "BTNG_05"  # BTNG005/left shoulder on gamepads
BTNG_06 = "BTNG_06"  # BTNG006/right shoulder on gamepads
BTNG_07 = "BTNG_07"  # BTNG007/left trigger on gamepads
BTNG_08 = "BTNG_08"  # BTNG008/right trigger on gamepads
BTNG_09 = "BTNG_09"  # BTNG009/left face on gamepads
BTNG_10 = "BTNG_10"  # BTNG_010/right face on gamepads
BTNG_11LTSTK = "BTNG_11LTSTK"  # BTN011/left stick on gamepads
BTNG_12RTSTK = "BTNG_12RTSTK"  # BTN012/right stick on gamepads
BTNG_13 = "BTNG_13"  # BTN013/home/select on gamepads
BTNK_00 = "BTNK_00"  # BTN000 on a knob
BTNMODE_01 = "BTNMODE_01"  # switch through MODE1 move/wheel for mouse actions
BTNMODE_02 = "BTNMODE_02"  # switch through MODE2 normal/draglock for mouse actions
BTNMWH_DN = "BTNMWH_DN"  # BTNMWHLDN/MSE_DN on mice
BTNMWH_DNLT = "BTNMWH_DNLT"  # BTNMWHLDN/MSE_DNLT on mice
BTNMWH_DNRT = "BTNMWH_DNRT"  # BTNMWHLDN/MSE_DNRT on mice
BTNMWH_LT = "BTNMWH_LT"  # BTNMWHLLT/MSE_LT on mice
BTNMWH_RLS = "BTNMWH_RLS"  # BTNMWHLRLS/MSE_RLS on mice
BTNMWH_RT = "BTNMWH_RT"  # BTNMWHLRT/MSE_RT on mice
BTNMWH_UP = "BTNMWH_UP"  # BTNMWHLUP/MSE_UP on mice
BTNMWH_UPLT = "BTNMWH_UPLT"  # BTNMWHLUP/MSE_UPLT on mice
BTNMWH_UPRT = "BTNMWH_UPRT"  # BTNMWHLUP/MSE_UPRT on mice
BTNM_01LT = "BTNM_01LT"  # BTN01/LEFT on mice
BTNM_02MD = "BTNM_02MD"  # BTN02/MIDDLE on mice
BTNM_03RT = "BTNM_03RT"  # BTN03/RIGHT on mice
BTNM_04WHUP = "BTNM_04WHUP"  # BTNM04/MSEWHL_UP on mice
BTNM_05WHDN = "BTNM_05WHDN"  # BTNM05/MSEWHL_DN on mice
BTNM_06WHLT = "BTNM_06WHLT"  # BTNM06/MSEWHL_LT on mice
BTNM_07WHRT = "BTNM_07WHRT"  # BTNM07/MSEWHL_RT on mice
BTNM_08 = "BTNM_08"  # BTNM_08/NW most additional BTN on mice
BTNM_09 = "BTNM_09"  # BTNM_09 additional on mice
BTNM_10 = "BTNM_10"  # BTNM_10 additional on mice
BTNM_11 = "BTNM_11"  # BTNM_11 additional BTN on mice
BTNM_12 = "BTNM_12"  # BTNM_12/SE most additional BTN on mice
BTNM_MDN = "BTNM_MDN"  # BTNMDN/MSE_DN on mice
BTNM_MDNLT = "BTNM_MDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_MDNRT = "BTNM_MDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_MLT = "BTNM_MLT"  # BTNMLT/MSE_LT on mice
BTNM_MRLS = "BTNM_MRLS"  # MSE_MRLS on mice
BTNM_MRT = "BTNM_MRT"  # BTNMRT/MSE_RT on mice
BTNM_MUP = "BTNM_MUP"  # BTNMUP/MSE_UP on mice
BTNM_MUPLT = "BTNM_MUPLT"  # BTNMUP/MSE_UPLT on mice
BTNM_MUPRT = "BTNM_MUPRT"  # BTNMUP/MSE_UPRT on mice
BTNM_WHDN = "BTNM_WHDN"  # BTNMDN/MSE_DN on mice
BTNM_WHDNLT = "BTNM_WHDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_WHDNRT = "BTNM_WHDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_WHLT = "BTNM_WHLT"  # BTNMLT/MSE_LT on mice
BTNM_WHRT = "BTNM_WHRT"  # BTNMRT/MSE_RT on mice
BTNM_WHUP = "BTNM_WHUP"  # BTNMUP/MSE_UP on mice
BTNM_WHUPLT = "BTNM_WHUPLT"  # BTNMUP/MSE_UPLT on mice
BTNM_WHUPRT = "BTNM_WHUPRT"  # BTNMUP/MSE_UPRT on mice
BTNST_00 = "BTNST_00"  # BTN000 on a Saitek commander


BTNSHOLDABLELIST = [
]

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0101 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMAXCF_SCTN0003_LAMBDA_DEF = "FMAXCF_SCTN0003_LAMBDA_DEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN0003_TYPE_DEF = "FMAXCF_SCTN0003_TYPE_DEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN0201_STR_DEF = "FMAXCF_SCTN0201_STR_DEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN0201_VAL_DEF = "FMAXCF_SCTN0201_VAL_DEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD"  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD"  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
FMAXCF_SCTN0202_OPTIONS_VAL_ADD = "FMAXCF_SCTN0202_OPTIONS_VAL_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
FMAXCF_SCTN0203_DICT_DEF = "FMAXCF_SCTN0203_DICT_DEF"  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICT_VS_ADD = "FMAXCF_SCTN0203_DICT_VS_ADD"  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICT_VV_ADD = "FMAXCF_SCTN0203_DICT_VV_ADD"  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LIST_DEF = "FMAXCF_SCTN0204_LIST_DEF"  # define a list in SCTN24 <NAC><LISTNAME>
FMAXCF_SCTN0204_LIST_STR_ADD = "FMAXCF_SCTN0204_LIST_STR_ADD"  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LIST_VAL_ADD = "FMAXCF_SCTN0204_LIST_VAL_ADD"  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
FMAXDO_SCTN0401_DEVICEDEF = "FMAXDO_SCTN0401_DEVICEDEF"  # define a device in PROF <NAC><MYNAME><DEV_NAME>
FMAXDO_SCTN0401_DICTKEYDEF = "FMAXDO_SCTN0401_DICTKEYDEF"  # define a profile dict key <NAC><KEY>
FMAXDO_SCTN0401_LAMBDADEF = "FMAXDO_SCTN0401_LAMBDADEF"  # define a profile lambda <NAC><NAME><LAMBDA>
FMAXDO_SCTN0401_STRDEF = "FMAXDO_SCTN0401_STRDEF"  # define a profile STR <NAC><NAME><VAL>
FMAXDO_SCTN0401_VALDEF = "FMAXDO_SCTN0401_VALDEF"  # define a profile value <NAC><NAME><VAL>
FMAXDO_SCTN0402_LDIEABSDEF = "FMAXDO_SCTN0402_LDIEABSDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0402_LDIEBTNDEF = "FMAXDO_SCTN0402_LDIEBTNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0402_LDIEFUNCDEF = "FMAXDO_SCTN0402_LDIEFUNCDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0402_LDIEKEYDEF = "FMAXDO_SCTN0402_LDIEKEYDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0402_LDIERELDEF = "FMAXDO_SCTN0402_LDIERELDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0402_LDIESPCLDEF = "FMAXDO_SCTN0402_LDIESPCLDEF"  # define IE psuedo entry for special events
FMAXDO_SCTN0402_LDIESYNDEF = "FMAXDO_SCTN0402_LDIESYNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN0403_AXDEF = "FMAXDO_SCTN0403_AXDEF"  # define a profile action <NAC>
FMAXDO_SCTN0403_AXVALADD = "FMAXDO_SCTN0403_AXVALADD"  # add an item to an action <NAC><AX><VAL>
FMAXDO_SCTN0404_DEVICEENTRYSTRADD = "FMAXDO_SCTN0404_DEVICEENTRYSTRADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
FMAXDO_SCTN0404_DEVICEENTRYVALADD = "FMAXDO_SCTN0404_DEVICEENTRYVALADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
FMAXDO_SCTN0405_HOLDABLEADD1 = "FMAXDO_SCTN0405_HOLDABLEADD1"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
FMAXDO_SCTN0405_HOLDABLEADD2 = "FMAXDO_SCTN0405_HOLDABLEADD2"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
FMAXDO_SCTN0405_NOTHOLDABLEADD1 = "FMAXDO_SCTN0405_NOTHOLDABLEADD1"  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
FMAXDO_SCTN0405_NOTHOLDABLEMODEDADD1 = "FMAXDO_SCTN0405_NOTHOLDABLEMODEDADD1"  # not holdable PROF items with a mode <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><MODENAME><NOTHOLDABLE><Ax>
FMAXDO_SCTN0406_XLATEADD = "FMAXDO_SCTN0406_XLATEADD"  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
FMAXDO_SCTN0407_BTNSDEF = "FMAXDO_SCTN0407_BTNSDEF"  # define buttons all around <NAC><BTNNAME><HOLDABLE>
FMAXDO_SCTN0408_EVTYPEDEF = "FMAXDO_SCTN0408_EVTYPEDEF"  # define a device type list type<NAC>
FMAXDO_SCTN0408_EVTYPELST = "FMAXDO_SCTN0408_EVTYPELST"  # add a device list entry<NAC>
FMAXDO_SCTN0409_DIRTRANSDEVDEF = "FMAXDO_SCTN0409_DIRTRANSDEVDEF"  # add a dict to DO.py <NAV><DEVNAME>
FMAXDO_SCTN0409_DIRTRANSSTRADD = "FMAXDO_SCTN0409_DIRTRANSSTRADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXDO_SCTN0409_DIRTRANSVALADD = "FMAXDO_SCTN0409_DIRTRANSVALADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXDO_SCTN040A_HBIABSADD = "FMAXDO_SCTN040A_HBIABSADD"  # enable ABS entry for IDB
FMAXDO_SCTN040A_HBIBTNADD = "FMAXDO_SCTN040A_HBIBTNADD"  # enable BTN entry for IDB
FMAXDO_SCTN040A_HBIKEYADD = "FMAXDO_SCTN040A_HBIKEYADD"  # enable KEY entry for IDB
FMAXDO_SCTN040A_HBIRELADD = "FMAXDO_SCTN040A_HBIRELADD"  # enable REL entry for IDB
FMAXDO_SCTN040B_DICTDEF = "FMAXDO_SCTN040B_DICTDEF"  # define a dict in DO.py
FMAXFM_SCTN0101_AX_DEF = "FMAXFM_SCTN0101_AX_DEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STR_DEF = "FMAXFM_SCTN0102_STR_DEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VAL_DEF = "FMAXFM_SCTN0102_VAL_DEF"  # define a FM value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICT_DEF = "FMAXFM_SCTN0103_DICT_DEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LIST_DEF = "FMAXFM_SCTN0104_LIST_DEF"  # define a list in FM <NAC>
FMAX_NOP = "FMAX_NOP"  # skip this entry


FMAXFM_AXLST = [
	FMAXCF_SCTN0003_LAMBDA_DEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN0003_TYPE_DEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN0201_STR_DEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN0201_VAL_DEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD,  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
	FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD,  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONS_VAL_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
	FMAXCF_SCTN0203_DICT_DEF,  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICT_VS_ADD,  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICT_VV_ADD,  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LIST_DEF,  # define a list in SCTN24 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LIST_STR_ADD,  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LIST_VAL_ADD,  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
	FMAXDO_SCTN0401_DEVICEDEF,  # define a device in PROF <NAC><MYNAME><DEV_NAME>
	FMAXDO_SCTN0401_DICTKEYDEF,  # define a profile dict key <NAC><KEY>
	FMAXDO_SCTN0401_LAMBDADEF,  # define a profile lambda <NAC><NAME><LAMBDA>
	FMAXDO_SCTN0401_STRDEF,  # define a profile STR <NAC><NAME><VAL>
	FMAXDO_SCTN0401_VALDEF,  # define a profile value <NAC><NAME><VAL>
	FMAXDO_SCTN0402_LDIEABSDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0402_LDIEBTNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0402_LDIEFUNCDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0402_LDIEKEYDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0402_LDIERELDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0402_LDIESPCLDEF,  # define IE psuedo entry for special events
	FMAXDO_SCTN0402_LDIESYNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN0403_AXDEF,  # define a profile action <NAC>
	FMAXDO_SCTN0403_AXVALADD,  # add an item to an action <NAC><AX><VAL>
	FMAXDO_SCTN0404_DEVICEENTRYSTRADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
	FMAXDO_SCTN0404_DEVICEENTRYVALADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
	FMAXDO_SCTN0405_HOLDABLEADD1,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN0405_HOLDABLEADD2,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
	FMAXDO_SCTN0405_NOTHOLDABLEADD1,  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN0405_NOTHOLDABLEMODEDADD1,  # not holdable PROF items with a mode <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><MODENAME><NOTHOLDABLE><Ax>
	FMAXDO_SCTN0406_XLATEADD,  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
	FMAXDO_SCTN0407_BTNSDEF,  # define buttons all around <NAC><BTNNAME><HOLDABLE>
	FMAXDO_SCTN0408_EVTYPEDEF,  # define a device type list type<NAC>
	FMAXDO_SCTN0408_EVTYPELST,  # add a device list entry<NAC>
	FMAXDO_SCTN0409_DIRTRANSDEVDEF,  # add a dict to DO.py <NAV><DEVNAME>
	FMAXDO_SCTN0409_DIRTRANSSTRADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXDO_SCTN0409_DIRTRANSVALADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXDO_SCTN040A_HBIABSADD,  # enable ABS entry for IDB
	FMAXDO_SCTN040A_HBIBTNADD,  # enable BTN entry for IDB
	FMAXDO_SCTN040A_HBIKEYADD,  # enable KEY entry for IDB
	FMAXDO_SCTN040A_HBIRELADD,  # enable REL entry for IDB
	FMAXDO_SCTN040B_DICTDEF,  # define a dict in DO.py
	FMAXFM_SCTN0101_AX_DEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STR_DEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VAL_DEF,  # define a FM value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICT_DEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LIST_DEF,  # define a list in FM <NAC>
	FMAX_NOP,  # skip this entry
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0102 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0103 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN0003_TYPE_CMNT_DICT = {}  # SCTN009 types comments
FMCF_SCTN0003_TYPE_DICT = {}  # SCTN003 types
FMCF_SCTN0201_DEF_CMNT_DICT = {}  # SCTN201 defines comments dict
FMCF_SCTN0201_DEF_DICT = {}  # SCTN201 defines dict
FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT = {}  # SCTN202 OPTIONSDICT comments dict
FMCF_SCTN0202_OPTIONSDICT_DICT = {}  # SCTN202 OPTIONSDICT
FMCF_SCTN0202_OPTIONSHELPDICT_DICT = {}  # SCTN202 OPTIONS HELPDICT
FMCF_SCTN0202_OPTIONS_CMNT_DICT = {}  # SCTN202 OPTIONS comments dict
FMCF_SCTN0202_OPTIONS_DICT = {}  # SCTN202 OPTIONS dict
FMCF_SCTN0203_DICT_CMNT_DICT = {}  # SCTN203 dict comments dict
FMCF_SCTN0203_DICT_DICT = {}  # SCTN203 dict dict
FMCF_SCTN0204_LIST_CMNT_DICT = {}  # SCTN204 list comments dict
FMCF_SCTN0204_LIST_DICT = {}  # SCTN204 list dict
FMDO_SCTN0401_DEVICEDEFCMNTDICT = {}  # SCTN21 device defines
FMDO_SCTN0401_DEVICEDEFDICT = {}  # SCTN21 device defines
FMDO_SCTN0402_LDIECMNTDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN0402_LDIEDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN0403_AXDEFCMNTDICT = {}  # SCTN23 output actions AX comments
FMDO_SCTN0403_AXDEFDICT = {}  # SCTN23 output actions AX
FMDO_SCTN0404_DEVICESCMNTDICT = {}  # SCTN24 device comments
FMDO_SCTN0404_DEVICESDICT = {}  # SCTN24 devices dict
FMDO_SCTN0405_BTNNDXDICT = {}  # SCTN45 device BTNTYPE dict
FMDO_SCTN0405_BTNTYPEDICT = {}  # SCTN45 device BTNTYPE dict
FMDO_SCTN0405_PROFDICT = {}  # SCTN45 device profile dict
FMDO_SCTN0405_RPTDICT = {}  # SCTN45 device RPT dict
FMDO_SCTN0406_XLATECMNTDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN0406_XLATEDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN0407_BTNSCMNTDICT = {}  # SCTN04 buttons
FMDO_SCTN0407_BTNSDICT = {}  # SCTN04 buttons
FMDO_SCTN0408_DEFCMNTDICT = {}  # define a device types list type
FMDO_SCTN0408_DEFDICT = {}  # define a device types list type
FMDO_SCTN0408_TYPESCMNTDICT = {}  # define a device types list type
FMDO_SCTN0408_TYPESDICT = {}  # define a device types list type
FMDO_SCTN0409_DIRTRANSCMNTDICT = {}  # holds dict for DO.py
FMDO_SCTN0409_DIRTRANSDICT = {}  # holds dict for DO.py
FMFM_SCTN0101_AX_CMNT_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0101_AX_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0102_VAL_CMNT_DICT = {}  # SCTN102 val
FMFM_SCTN0102_VAL_DICT = {}  # SCTN102 val
FMFM_SCTN0103_DICT_CMNT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0103_DICT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0104_LIST_CMNT_DICT = {}  # SCTN201 device defines
FMFM_SCTN0104_LIST_DICT = {}  # SCTN201 device defines


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0104 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMDO_SCTN0402_LDIERELLIST = []  # SCTN22 LDIE relative evdev actions defined
FMDO_SCTN0402_LDIESPCLLIST = []  # SCTN22 LDIE defined
FMDO_SCTN0407_BTNSHOLDABLELIST = []  # buttons holdable list
FMDO_SCTN040A_HBIABSLIST = []  # SCTN50 list
FMDO_SCTN040A_HBIBTNLIST = []  # SCTN51 list
FMDO_SCTN040A_HBIKEYLIST = []  # SCTN52 list
FMDO_SCTN040A_HBIRELLIST = []  # SCTN53 list
FMFM_SCTN0004_BTNS_HOLDABLE_LIST = []  # buttons holdable list


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


	global \
		FMCF_SCTN0003_TYPE_CMNT_DICT, \
		FMCF_SCTN0003_TYPE_DICT, \
		FMCF_SCTN0201_DEF_CMNT_DICT, \
		FMCF_SCTN0201_DEF_DICT, \
		FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT, \
		FMCF_SCTN0202_OPTIONSDICT_DICT, \
		FMCF_SCTN0202_OPTIONSHELPDICT_DICT, \
		FMCF_SCTN0202_OPTIONS_CMNT_DICT, \
		FMCF_SCTN0202_OPTIONS_DICT, \
		FMCF_SCTN0203_DICT_CMNT_DICT, \
		FMCF_SCTN0203_DICT_DICT, \
		FMCF_SCTN0204_LIST_CMNT_DICT, \
		FMCF_SCTN0204_LIST_DICT, \
		FMDO_SCTN0401_DEVICEDEFCMNTDICT, \
		FMDO_SCTN0401_DEVICEDEFDICT, \
		FMDO_SCTN0402_LDIECMNTDICT, \
		FMDO_SCTN0402_LDIEDICT, \
		FMDO_SCTN0403_AXDEFCMNTDICT, \
		FMDO_SCTN0403_AXDEFDICT, \
		FMDO_SCTN0404_DEVICESCMNTDICT, \
		FMDO_SCTN0404_DEVICESDICT, \
		FMDO_SCTN0405_BTNNDXDICT, \
		FMDO_SCTN0405_BTNTYPEDICT, \
		FMDO_SCTN0405_PROFDICT, \
		FMDO_SCTN0405_RPTDICT, \
		FMDO_SCTN0406_XLATECMNTDICT, \
		FMDO_SCTN0406_XLATEDICT, \
		FMDO_SCTN0407_BTNSCMNTDICT, \
		FMDO_SCTN0407_BTNSDICT, \
		FMDO_SCTN0408_DEFCMNTDICT, \
		FMDO_SCTN0408_DEFDICT, \
		FMDO_SCTN0408_TYPESCMNTDICT, \
		FMDO_SCTN0408_TYPESDICT, \
		FMDO_SCTN0409_DIRTRANSCMNTDICT, \
		FMDO_SCTN0409_DIRTRANSDICT, \
		FMFM_SCTN0101_AX_CMNT_DICT, \
		FMFM_SCTN0101_AX_DICT, \
		FMFM_SCTN0102_VAL_CMNT_DICT, \
		FMFM_SCTN0102_VAL_DICT, \
		FMFM_SCTN0103_DICT_CMNT_DICT, \
		FMFM_SCTN0103_DICT_DICT, \
		FMFM_SCTN0104_LIST_CMNT_DICT, \
		FMFM_SCTN0104_LIST_DICT, \
		FMDO_SCTN0402_LDIERELLIST, \
		FMDO_SCTN0402_LDIESPCLLIST, \
		FMDO_SCTN0407_BTNSHOLDABLELIST, \
		FMDO_SCTN040A_HBIABSLIST, \
		FMDO_SCTN040A_HBIBTNLIST, \
		FMDO_SCTN040A_HBIKEYLIST, \
		FMDO_SCTN040A_HBIRELLIST, \
		FMFM_SCTN0004_BTNS_HOLDABLE_LIST
