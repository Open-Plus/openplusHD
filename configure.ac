AC_INIT(skins,0.0.1)
AC_INIT([enigma2-plugins],[3.0.0])
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])

TUXBOX_APPS_DIRECTORY
AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE
AM_PATH_PYTHON()
AC_PYTHON_DEVEL

AC_PROG_CC
AC_PROG_CXX
m4_ifdef([LT_INIT], [LT_INIT], [AC_PROG_LIBTOOL])
AC_CONFIG_MACRO_DIR([m4])

AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))

AM_PATH_PYTHON

CPPFLAGS="$CPPFLAGS $PYTHON_CPPFLAGS -include Python.h"
CFLAGS="$CFLAGS $DEBUG_CFLAGS -Wall"
CXXFLAGS="$CXXFLAGS $DEBUG_CFLAGS -Wall $ENIGMA2_CFLAGS $PTHREAD_CFLAGS"

AC_OUTPUT([
Makefile
opbitrate/Makefile
openplusHD/Makefile
openplusHD/buttons/Makefile
openplusHD/colors/Makefile
openplusHD/epg/Makefile
openplusHD/extensions/Makefile
openplusHD/fonts/Makefile
openplusHD/icons/Makefile
openplusHD/icons/picons/Makefile
openplusHD/icons/sound/Makefile
openplusHD/menu/Makefile
openplusHD/screens/Makefile
openplusHD/skin_default/Makefile
openplusHD/skin_default/buttons/Makefile
openplusHD/skin_default/icons/Makefile
components/Makefile
components/Converter/Makefile
components/Renderer/Makefile
])
