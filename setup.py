from setuptools import setup, find_packages

setup(
    name='tw2.wysihtml5',
    version='0.2',
    description='WYSIHTML5 widget for ToscaWidgets2',
    author='Moritz Schlarb',
    author_email='mail@moritz-schlarb.de',
    url='https://github.com/toscawidgets/tw2.wysihtml5',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        'tw2.bootstrap.forms',
        "Mako",
        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=['tw2', 'tw2.bootstrap'],
    zip_safe=False,
    include_package_data=True,
    test_suite='nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.wysihtml5
        bootstrap = tw2.bootstrap.wysihtml5
    """,
    keywords=[
        'toscawidgets.widgets',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
