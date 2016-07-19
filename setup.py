from setuptools import setup, find_packages

setup(
    name="django-prefixfield",
    version="0.1.1",
    packages=['django_prefixfield'],
    install_requires=['django>=1.9'],
    author="Iskren Hadzhinedev",
    author_email="i.hadzhinedev@gmail.com",
    description="Adds a prefix field for use with Django models",
    url="https://github.com/Metalgrid/django-prefixfield",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Development',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
    ]
)
