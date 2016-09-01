from setuptools import setup, find_packages

requirements = [
    'Flask==0.11.1',
    'Flask-OAuthlib==0.9.3',

    'SQLAlchemy==1.0.13',
    'Flask-SQLAlchemy==2.1',

    'Flask-Script==2.0.5',
    'Flask-Migrate==1.8.0',

    'PyYaml==3.11',
    'shortuuid==0.4.3',

    "Flask-Webpack>=0.0.7",
    'psycopg2==2.6.2',
]

setup(
    name='Feature Request',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)