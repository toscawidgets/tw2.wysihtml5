from setuptools import setup, find_packages

setup(
    name='tw2.wysihtml5',
    version='0.3.1',
    description='WYSIHTML5 widget for ToscaWidgets2',
    author='Moritz Schlarb',
    author_email='moschlar@metalabs.de',
    url='https://github.com/toscawidgets/tw2.wysihtml5',
    license='BSD 2-clause',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        "Mako",
        ## Add other requirements here
        # "Genshi",
        ],
    extras_require={'bootstrap': 'tw2.bootstrap.forms'},
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=['tw2', 'tw2.bootstrap'],
    zip_safe=False,
    include_package_data=True,
    test_suite='nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets_plain = tw2.wysihtml5
        widgets_bootstrap = tw2.bootstrap.wysihtml5
    """,
    keywords=[
        'toscawidgets.widgets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
)
