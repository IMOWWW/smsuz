from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='smsuz',
    version='0.0.1',
    license='MIT',
    author='IMOWWW',
    author_email='imowww@yandex.ru',
    description='This is the API SMS Gateway Sayqal.uz',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://abexlab.uz',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'Django>=3.2',
        'djangorestframework>=3.12', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    keywords='sms gateway, django, api, smsuz, sms, uz',
    project_urls={
        'GitHub': 'https://github.com/IMOWWW/smsuz.git', 
    },
    python_requires='>=3.6',
)
