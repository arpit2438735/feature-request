from setuptools import setup, find_packages

requirements = [
    'Flask==0.11.1',
    'Flask-OAuthlib==0.9.3',
    'SQLAlchemy==1.0.13',
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