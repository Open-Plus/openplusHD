AC_INIT([enigma2-plugin-skins-openplushd],[4.3.0],[www.dreambox-tools.info])
AM_INIT_AUTOMAKE([foreign])

AM_SILENT_RULES([yes])

AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE

AC_PROG_CXX
LT_INIT
AC_CONFIG_MACRO_DIR([m4])

AM_PATH_PYTHON
AX_PYTHON_DEVEL
AX_PTHREAD

PKG_CHECK_MODULES(ENIGMA2, enigma2)
PKG_CHECK_MODULES(LIBCRYPTO, libcrypto)

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
AC_OUTPUT
