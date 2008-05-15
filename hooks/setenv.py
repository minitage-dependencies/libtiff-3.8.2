import os

from minitage.core.common import append_env_var

os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'


def getlibtiffenv(options,buildout):
    for var in ['zlib','libjpeg', 'libiconv',]:
        append_env_var('LDFLAGS', ["-L%(lib)s/lib -Wl,-rpath -Wl,%(lib)s/lib %(os)s"%{'lib':buildout[var]['location'],'os':os_ldflags}],sep=' ',before=False)
        append_env_var('LD_RUN_PATH', ["%(lib)s/lib"%{'lib':buildout[var]['location']}],sep=':',before=False)
        append_env_var('CFLAGS',   ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        append_env_var('CPPFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        append_env_var('CXXFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)

# vim:set ts=4 sts=4 et  :
