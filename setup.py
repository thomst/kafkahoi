from distutils.core import setup
import os

db = '.kafkahoisdb'
img_dir = os.walk('Img')
snd_dir = os.walk('Snd')
fnt_dir = os.walk('Fnt')
data_files = [(d[0], [os.path.join(d[0], f) for f in d[2]]) for d in img_dir]
data_files += [(d[0], [os.path.join(d[0], f) for f in d[2]]) for d in snd_dir]
data_files += [(d[0], [os.path.join(d[0], f) for f in d[2]]) for d in fnt_dir]
data_files += [('', [db])]

setup( 
    name = "kafkahoi",
    version = "1.0.2",
    author = "Thomas Leichtfuss",
    author_email = "thomaslfuss@gmx.de",
    required = ['pygame', 'Tkinter'],
    py_modules = [m[:-3] for m in os.listdir('Src') if m[-3:] == '.py'],
    package_dir = {'' : 'Src'},
    scripts = ["kafkahoi"],
    data_files = data_files,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Games/Entertainment',
    ],
    license='GPL',
    keywords='game shooter 2D alternative experimental poem poems',
    entry_points={'console_scripts': ['kafkahoi = kafkahoi:main', ]},
)

