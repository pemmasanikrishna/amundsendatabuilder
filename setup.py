import os
from setuptools import setup, find_packages


__version__ = '2.5.1'

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

kafka = ['confluent-kafka==1.0.0']

cassandra = ['cassandra-driver==3.20.1']

glue = ['boto3==1.10.1']

snowflake = [
    'snowflake-connector-python',
    'snowflake-sqlalchemy'
]

athena = ['PyAthena[SQLAlchemy]>=1.0.0']

# Python API client for google
# License: Apache Software License
# Upstream url: https://github.com/googleapis/google-api-python-client
bigquery = [
    'google-api-python-client>=1.6.0, <2.0.0dev',
    'google-auth-httplib2>=0.0.1'
    'google-auth>=1.0.0, <2.0.0dev'
]

jsonpath = ['jsonpath_rw==1.4.0']

all_deps = requirements + kafka + cassandra + glue + snowflake + athena + bigquery + jsonpath

setup(
    name='amundsen-databuilder',
    version=__version__,
    description='Amundsen Data builder',
    url='https://www.github.com/lyft/amundsendatabuilder',
    maintainer='Lyft',
    maintainer_email='dev@lyft.com',
    packages=find_packages(exclude=['tests*']),
    dependency_links=[],
    install_requires=requirements,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',
    extras_require={
        ':python_version=="2.7"': ['typing>=3.6'],  # allow typehinting PY2
        'all': all_deps,
        'kafka': kafka,  # To use with Kafka source extractor
        'cassandra': cassandra,
        'glue': glue,
        'snowflake': snowflake,
        'athena': athena,
        'bigquery': bigquery,
        'jsonpath': jsonpath
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
